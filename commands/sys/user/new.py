import os
import sys

user = sys.argv[2:3][0]
os.mkdir(f"/home/runner/CommandHandlerV3/root/users/{user}")
os.mkdir(f"/home/runner/CommandHandlerV3/root/users/{user}/bin")
os.mkdir(f"/home/runner/CommandHandlerV3/root/users/{user}/py")
os.mkdir(f"/home/runner/CommandHandlerV3/root/users/{user}/files")

print(f"Created user {user}")