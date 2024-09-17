import os
import platform
import subprocess
import socket
import threading
from ipaddress import ip_network, IPv4Network
import argparse
import json
import csv
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor


def ping_ip(ip, timeout=2):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", "-W", str(timeout), str(ip)]
    response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return response.returncode == 0


def scan_ports(ip, ports, timeout=1):
    open_ports = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            if s.connect_ex((str(ip), port)) == 0:
                open_ports.append(port)
    return open_ports


def resolve_hostname(ip):
    try:
        return socket.gethostbyaddr(str(ip))[0]
    except socket.herror:
        return None


def scan_ip(ip, ports=None, timeout=2):
    result = {
        "ip": str(ip),
        "status": "down",
        "hostname": None,
        "open_ports": []
    }
    if ping_ip(ip, timeout):
        result["status"] = "up"
        result["hostname"] = resolve_hostname(ip)
        if ports:
            result["open_ports"] = scan_ports(ip, ports, timeout)
    return result


def scan_ip_range(ip_range, ports=None, timeout=2, verbose=False):
    live_hosts = []
    ip_list = list(ip_network(ip_range).hosts())
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(scan_ip, ip, ports, timeout): ip for ip in ip_list}
        for future in tqdm(futures, total=len(futures), desc="Scanning IP Range"):
            result = future.result()
            if result["status"] == "up":
                live_hosts.append(result)
                
    return live_hosts


def save_results(live_hosts, output_file, file_format):
    if file_format == "json":
        with open(output_file, "w") as f:
            json.dump(live_hosts, f, indent=4)
    elif file_format == "csv":
        with open(output_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=live_hosts[0].keys())
            writer.writeheader()
            writer.writerows(live_hosts)


def main():
    parser = argparse.ArgumentParser(
        description="A CLI-based IP and Port Scanner",
        usage='%(prog)s --range <IP_RANGE> [options]',
        epilog="Example: python ip_scanner.py --range 192.168.1.0/24 --ports 22 80 443 --output results.json --format json --verbose"
    )
    
    parser.add_argument('--range', required=True, help="IP range in CIDR notation (e.g., 192.168.1.0/24)")
    parser.add_argument('--ports', nargs='+', type=int, help="Ports to scan (e.g., 22 80 443)")
    parser.add_argument('--timeout', type=int, default=2, help="Timeout in seconds for ping and port scans")
    parser.add_argument('--output', help="Save results to a file (e.g., results.json or results.csv)")
    parser.add_argument('--format', choices=['json', 'csv'], help="Output file format (json or csv)")
    parser.add_argument('--verbose', action='store_true', help="Show detailed output")
    parser.add_argument('--exclude', nargs='+', help="IP addresses to exclude from scanning")
    parser.add_argument('--active', action='store_true', help="Show only active (up) hosts")
    parser.add_argument('--inactive', action='store_true', help="Show only inactive (down) hosts")

    args = parser.parse_args()

    ip_range = args.range
    ports = args.ports if args.ports else []
    timeout = args.timeout
    verbose = args.verbose
    exclude_ips = set(args.exclude) if args.exclude else set()

    print(f"Starting scan on IP range: {ip_range}")
    live_hosts = scan_ip_range(ip_range, ports, timeout, verbose)

    # Filtering active/inactive hosts
    if args.active:
        live_hosts = [host for host in live_hosts if host['status'] == 'up']
    if args.inactive:
        live_hosts = [host for host in live_hosts if host['status'] == 'down']

    # Show the results on the command-line during runtime
    if live_hosts:
        for host in live_hosts:
            print(f"{host['ip']} - {host['status']} - Hostname: {host['hostname']} - Open Ports: {host['open_ports']}")
        
        # Save the results if output file and format are specified
        if args.output and args.format:
            save_results(live_hosts, args.output, args.format)
            print(f"\nResults have been saved to {args.output} in {args.format} format.")
    else:
        print("No live hosts found during the scan.")
        if args.output and args.format:
            print(f"No file was created as there are no live hosts found.")


if __name__ == "__main__":
    main()
