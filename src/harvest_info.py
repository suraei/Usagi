import subprocess
from config import THEHARVESTER_CONTAINER_NAME

def run_theharvester(target):
    cmd = ["docker", "run", "--rm", THEHARVESTER_CONTAINER_NAME, "-d", target, "-b", "all"]
    result = subprocess.check_output(cmd)
    print(result.decode('utf-8'))
