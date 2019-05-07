import os
import sys
import subprocess

def expand_escape_sequence(string):
    return bytes(string, "utf-8").decode("unicode_escape")

def kill_task(pid):
    """
    kills task via subprocess.Popen module
    
    params:
    @pid: pid 
    @return: None
    """
    if 'win' in sys.platform:
        dev_null = open(os.devnull, 'w')
        subprocess.Popen(['TASKKILL', '/PID', str(pid)], stdin=dev_null, stdout=sys.stdout, stderr=sys.stderr)
    else:
        subprocess.Popen(['kill', str(pid)], stdin=dev_null, stdout=sys.stdout, stderr=sys.stderr)