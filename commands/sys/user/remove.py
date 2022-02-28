import shutil
import sys

user = sys.argv[2:3]
shutil.rmtree(f'/home/runner/CommandHandlerV3/root/users/{user[0]}')
print(f"Removed user {user}")