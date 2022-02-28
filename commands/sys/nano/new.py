import sys
import os

data = []
dir = os.getcwd()
print("type '?nano exit' to save and close")

while True:
  line = input("?nano> ")
  if line == "?nano exit":
    break
  
  data.append(line)

with open(f"{dir}/{sys.argv[2:3][0]}", "a") as f:
  for i in data:
    f.write(f"{i}\n")