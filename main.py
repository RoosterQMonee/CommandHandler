import subprocess
import os

while True:
  direct = os.getcwd().split("/")[3:]
  user_in = input(f"{direct}> ")

  try:
    c_args = user_in.split("-a")[0]
    e_args = user_in.split("-a")[1]

    if "cd" in c_args:
      os.chdir(e_args.replace(" ",""))
      continue
    
    command = "commands"
  
    for cmd in c_args.split(" "):
      command = f"{command}/{cmd}"
  
    command = command[:len(command)-1]
    n_command = f"python /home/runner/CommandHandlerV3/{command}.py {e_args}"
    
    subprocess.call(n_command.split(" "))

  except Exception:
    print("-a argument required {command -a args}")