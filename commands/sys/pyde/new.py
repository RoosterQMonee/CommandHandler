import sys
import os

data = []
dir = os.getcwd()
print("type '?exit' to save and close")

while True:
  line = input("?pyDE> ")
  if line == "?exit":
    break
  
  data.append(line)

with open(f"{dir}/{sys.argv[2:3][0]}", "a") as f:
  for i in data:
    f.write(f"{i}\n")