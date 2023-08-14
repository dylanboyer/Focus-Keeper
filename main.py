import time
import tkinter as tk

# This is a temporary list. Once functionality is tested, database storage will be implemented.
blocked_sites = []
host_path = "C:\Windows\System32\drivers\etc\hosts"
ip = "127.0.0.1"

def unblock_sites():
    with open(host_path, "r") as file:
        content = file.readlines()
    with open(host_path, "w") as file: # completely rewrite file to update changes
        for line in content:
            if line.strip() != blocked_sites:
                file.write(line)

def main():
    while True:
        with open(host_path, "r+") as file:
            content = file.read() # go to end of file
            for website in blocked_sites:
                if website in content:
                    pass
                else:
                    file.write(ip + " " + website + "\n") # redirect the blocked site to localhost
        time.sleep(5)

if __name__ == '__main__':
    main()