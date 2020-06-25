import subprocess
def cmdline(cmd):
  res = subprocess.run(
    args=cmd,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    shell=True)
  return res.stdout