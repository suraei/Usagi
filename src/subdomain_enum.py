import subprocess
from config import SUBLIST3R_CONTAINER_NAME

def run_sublist3r(target):
    cmd = ["docker", "run", "--rm", SUBLIST3R_CONTAINER_NAME, "-d", target]
    result = subprocess.check_output(cmd)
    print(result.decode('utf-8'))
