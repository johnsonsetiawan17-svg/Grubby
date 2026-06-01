import os
import sys
import time
import random

def clear(): os.system('clear')

def help_menu():
    print("--- Grubby Commands ---")
    commands = [
        ".help   - Show this menu",
        ".exit   - Close Grubby",
        ".clear  - Clear terminal",
        ".hello  - Greeting",
        ".date   - Show date",
        ".time   - Show time",
        ".calc   - Simple math",
        ".cowsay - Cow says something",
        ".joke   - Random joke",
        ".ip     - Show network info",
        ".sys    - System info",
        ".whoami - Current user",
        ".ls     - List files",
        ".pwd    - Print working dir",
        ".slap   - Fun command",
        ".hack   - Fake hack",
        ".random - Random number"
    ]
    for cmd in commands:
        print(cmd)

def main():
    clear()
    print("Grubby Terminal v1.0 | Type .help for a list of commands.")
    while True:
        user_input = input("Grubby> ").strip()
        if not user_input: continue
        
        parts = user_input.split(" ", 1)
        cmd = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""

        if cmd == ".help": help_menu()
        elif cmd == ".exit": break
        elif cmd == ".clear": clear()
        elif cmd == ".hello": print("Hello! I am Grubby.")
        elif cmd == ".date": os.system("date")
        elif cmd == ".time": print(time.ctime())
        elif cmd == ".calc": print(f"Result: {eval(args)}" if args else "Usage: .calc 2+2")
        elif cmd == ".cowsay": os.system(f"cowsay '{args}'" if args else "cowsay 'Hello'")
        elif cmd == ".joke": print("Why do coders like dark mode? Because light attracts bugs.")
        elif cmd == ".ip": os.system("ifconfig")
        elif cmd == ".sys": os.system("uname -a")
        elif cmd == ".whoami": os.system("whoami")
        elif cmd == ".ls": os.system("ls")
        elif cmd == ".pwd": os.system("pwd")
        elif cmd == ".slap": print("*slaps the screen*")
        elif cmd == ".hack": print("Accessing mainframe... 0%... 50%... 100% Done!")
        elif cmd == ".random": print(random.randint(1, 100))
        else: print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
