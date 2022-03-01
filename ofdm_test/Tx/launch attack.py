import subprocess
import time

if __name__ == '__main__':
    pro = subprocess.Popen('python ./attack.py', shell=True)
    time.sleep(10)
    pro.kill()