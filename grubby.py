import os
import sys
import time

def clear(): os.system('clear')

def help_menu():
    print("--- Grubby Commands ---")
    print(".help   .exit   .clear  .hello  .date   .ping   .info   .sys    .whoami")
    print(".ls     .pwd    .banner .slap   .joke   .sleep  .count  .cowsay .sysinfo")
    print(".ip     .time   .color  .love   .bye    .calc   .hack   .dev    .wait")
    print(".echo   .host   .id     .shell  .os     .up     .random .start")

def main():
    clear()
    print("Grubby Terminal Tool Loaded. Type .help for commands.")
    while True:
        cmd = input("Grubby> ").strip().lower()
        
        if cmd == ".help": help_menu()
        elif cmd == ".exit": sys.exit()
        elif cmd == ".clear": clear()
        elif cmd == ".hello": print("Hello there, human!")
        elif cmd == ".date": os.system("date")
        elif cmd == ".ping": print("Pong!")
        elif cmd == ".info": print("Grubby v1.0 - Built for Termux")
        elif cmd == ".sys": os.system("uname -a")
        elif cmd == ".whoami": os.system("whoami")
        elif cmd == ".ls": os.system("ls")
        elif cmd == ".pwd": os.system("pwd")
        elif cmd == ".banner": print("  Grubby is Online!  ")
        elif cmd == ".slap": print("*slaps the terminal*")
        elif cmd == ".joke": print("Why do programmers prefer dark mode? Because light attracts bugs.")
        elif cmd == ".sleep": time.sleep(2); print("Woke up!")
        elif cmd == ".count": print(*(range(1, 6)))
        elif cmd == ".cowsay": os.system("cowsay 'Grubby is cool'")
        elif cmd == ".sysinfo": os.system("df -h")
        elif cmd == ".ip": os.system("ifconfig")
        elif cmd == ".time": print(time.ctime())
        elif cmd == ".color": print("\033[92m Green Mode Activated \033[0m")
        elif cmd == ".love": print("Code is love, code is life.")
        elif cmd == ".bye": print("See you later!"); sys.exit()
        elif cmd == ".calc": print(f"Result: {2+2}")
        elif cmd == ".hack": print("Accessing mainframe... Just kidding!")
        elif cmd == ".dev": print("Made by a 10-year-old coder!")
        elif cmd == ".wait": time.sleep(1); print("Done waiting.")
        elif cmd == ".echo": print(input("Say what? "))
        elif cmd == ".host": os.system("hostname")
        elif cmd == ".id": os.system("id")
        elif cmd == ".shell": os.system("/bin/bash")
        elif cmd == ".os": print("OS: Termux / Android")
        elif cmd == ".up": print("Uptime: It's running!")
        elif cmd == ".random": import random; print(random.randint(1, 100))
        elif cmd == ".start": print("Grubby engine started.")
        else: print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
