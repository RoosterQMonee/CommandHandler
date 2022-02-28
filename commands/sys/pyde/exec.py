import sys
import os

dir = os.getcwd()
with open(f"{dir}/{sys.argv[2:3][0]}", "r") as f:
  exec(f.read())