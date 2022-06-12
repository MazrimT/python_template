import subprocess
import os
from pathlib import Path

# create virtual environment if not exists
make_venv = "python -m venv venv"
print(make_venv)
os.system(make_venv)

# find the base path and set path to python binary
dir_path = Path(__file__).parent
python_bin = f"{dir_path}/venv/Scripts/python"

# commands to run
cmds = [
    '-m pip install --upgrade pip',
    '-m pip install wheel',
    '-m pip install -r requirements.txt',
]

for cmd in cmds:

    cmd = [python_bin] + cmd.split()
    print(' '.join(cmd))
    process = subprocess.Popen(cmd, shell=True) 
    # wait for process to run
    process.wait()
    # kill the process
    process.kill()
