import sys
import os

dir = os.getcwd()
os.remove(f"{dir}/{sys.argv[2:3][0]}")