import subprocess

def run_nmap_scan(target):
    cmd = ["docker", "run", "--rm", "nmap-container", "-F", target]
    result = subprocess.check_output(cmd)
    print(result.decode('utf-8'))
