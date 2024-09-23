<!DOCTYPE html>
<html lang="en">

<body>
    <h1>IPScanX - The IP Scanner</h1>
   
<h2>Table of Contents</h2>
    <ul>
        <li><a href="#introduction">Introduction</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#installation">Installation</a></li>
        <ul>
            <li><a href="#command-line-arguments">Command-Line Arguments</a></li>
            <li><a href="#examples">Examples</a></li>
        </ul>
        <li><a href="#configuration">Configuration</a></li>
        <li><a href="#contributing">Contributing</a></li>
        <li><a href="#license">License</a></li>
        
</ul>

<h2 id="introduction">Introduction</h2>
    <p><strong>IPScanX</strong> is a robust, command-line interface (CLI) tool designed for network administrators, security professionals, and enthusiasts to efficiently scan IP ranges and identify active hosts along with their open ports. Leveraging multithreading for speed and flexibility in configuration, IPScanX simplifies the process of network reconnaissance and vulnerability assessment.</p>

<h2 id="features">Features</h2>
    <ul>
        <li><strong>IP Range Scanning</strong>: Scan entire IP ranges specified in CIDR notation.</li>
        <li><strong>Port Scanning</strong>: Check specific ports or ranges of ports for each active host.</li>
        <li><strong>Multithreading</strong>: Utilize concurrent threads to accelerate scanning processes.</li>
        <li><strong>Hostname Resolution</strong>: Automatically resolve hostnames for active IPs.</li>
        <li><strong>Exclusion List</strong>: Exclude specific IP addresses from scanning.</li>
        <li><strong>Result Filtering</strong>: Display only active or inactive hosts based on user preference.</li>
        <li><strong>Output Options</strong>: Save scan results in JSON or CSV formats.</li>
        <li><strong>Verbose Mode</strong>: Get detailed output during the scanning process.</li>
        <li><strong>Cross-Platform Compatibility</strong>: Works on Windows, macOS, and Linux systems.</li>
    </ul>

<h2 id="installation">Installation</h2>
    <h3>Prerequisites</h3>
    <ul>
        <li><strong>Python 3.7+</strong>: Ensure you have Python installed. You can download it from <a href="https://www.python.org/downloads/">python.org</a>.</li>
        <li><strong>pip</strong>: Python package installer. It usually comes bundled with Python.</li>
    </ul>

<h3>Clone the Repository</h3>
    <pre><code>git clone https://github.com/yourusername/IPScanX.git
cd IPScanX
</code></pre>


<h3>Install Dependencies</h3>
    <pre><code>pip install -r requirements.txt
</code></pre>
    <p><em>If you don’t have <code>requirements.txt</code>, here are the dependencies:</em></p>
    <pre><code>pip install tqdm concurrent.futures argparse ipaddress
</code></pre>

<h2 id="usage">Usage</h2>
    <p>Run the <code>IPScanX.py</code> script with the desired arguments.</p>
    <pre><code>python IPScanX.py --range &lt;IP_RANGE&gt; [options]
</code></pre>

 <h3 id="command-line-arguments">Command-Line Arguments</h3>
    <table border="1">
        <tr>
            <th>Argument</th>
            <th>Description</th>
            <th>Required</th>
            <th>Example</th>
        </tr>
        <tr>
            <td><code>--range</code></td>
            <td><strong>(Required)</strong> IP range in CIDR notation to scan (e.g., <code>192.168.1.0/24</code>).</td>
            <td>Yes</td>
            <td><code>--range 192.168.1.0/24</code></td>
        </tr>
        <tr>
            <td><code>--ports</code></td>
            <td>Specify ports or port ranges to scan. Use commas to separate multiple ports or use hyphens for ranges (e.g., <code>22,80,443</code> or <code>20-1024</code>).</td>
            <td>No</td>
            <td><code>--ports 22,80,443</code> or <code>--ports 20-1024</code></td>
        </tr>
        <tr>
            <td><code>--timeout</code></td>
            <td>Timeout in seconds for ping and port scans. Default is <code>2</code> seconds.</td>
            <td>No</td>
            <td><code>--timeout 3</code></td>
        </tr>
        <tr>
            <td><code>--output</code></td>
            <td>Save scan results to a file. Specify the filename with extension (<code>.json</code> or <code>.csv</code>).</td>
            <td>No</td>
            <td><code>--output results.json</code></td>
        </tr>
        <tr>
            <td><code>--format</code></td>
            <td>Choose the output file format: <code>json</code> or <code>csv</code>. Must be used with <code>--output</code>.</td>
            <td>No</td>
            <td><code>--format csv</code></td>
        </tr>
        <tr>
            <td><code>--verbose</code></td>
            <td>Enable verbose mode to show detailed output during the scanning process.</td>
            <td>No</td>
            <td><code>--verbose</code></td>
        </tr>
        <tr>
            <td><code>--exclude</code></td>
            <td>Exclude specific IP addresses from the scan. Provide one or more IPs separated by space.</td>
            <td>No</td>
            <td><code>--exclude 192.168.1.1 192.168.1.2</code></td>
        </tr>
        <tr>
            <td><code>--active</code></td>
            <td>Show only active (up) hosts in the output.</td>
            <td>No</td>
            <td><code>--active</code></td>
        </tr>
        <tr>
            <td><code>--inactive</code></td>
            <td>Show only inactive (down) hosts in the output.</td>
            <td>No</td>
            <td><code>--inactive</code></td>
        </tr>
    </table>

 <h3 id="examples">Examples</h3>
    <pre><code>python IPScanX.py --range 192.168.1.0/24
python IPScanX.py --range 192.168.1.0/24 --ports 22,80,443
python IPScanX.py --range 10.0.0.0/16 --ports 20-1024 --timeout 3
python IPScanX.py --range 192.168.1.0/24 --exclude 192.168.1.5 192.168.1.10 --output scan_results.json --format json
python IPScanX.py --range 192.168.1.0/24 --active --verbose
python IPScanX.py --range 192.168.1.0/24 --inactive --output inactive_hosts.csv --format csv
</code></pre>

<h2 id="configuration">Configuration</h2>
    <p>No additional configuration is needed. Command-line arguments provide all the necessary settings.</p>

  
<h2 id="contributing">Contributing</h2>
    <p>Contributions are welcome! Please follow the guidelines below:</p>
    <ol>
        <li>Fork the repository.</li>
        <li>Create a new branch (<code>git checkout -b feature-branch</code>).</li>
        <li>Commit your changes (<code>git commit -m 'Add new feature'</code>).</li>
        <li>Push to the branch (<code>git push origin feature-branch</code>).</li>
        <li>Submit a pull request.</li>
    </ol>

<h2 id="license">License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>
</html>
