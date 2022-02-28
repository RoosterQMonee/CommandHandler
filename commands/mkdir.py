import sys
import os

args = sys.argv[2:]

if len(args) > 1:
  print(f"Error | too many arguments, {len(args)}")

try:
  
  if os.path.isfile(args[0]):
    print(f"Error | argument already exists")

  else:
    os.mkdir(args[0])

except Exception:
  print(f"Error | failed to make file {Exception}")