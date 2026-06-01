import os
import sys
import random

def clear():
    os.system('clear')

def help_menu():
    print("--- Grubby Commands ---")
    commands = [
        ".help",
        ".exit",
        ".clear",
        ".hello",
        ".date",
        ".ping",
        ".info",
        ".sys",
        ".whoami",
        ".ls",
        ".pwd",
        ".banner",
        ".slap",
        ".joke",
        ".sleep",
        ".count",
        ".cowsay",
        ".sysinfo",
        ".ip",
        ".time",
        ".color",
        ".love",
        ".bye",
        ".calc",
        ".hack",
        ".dev",
        ".wait",
        ".echo",
        ".host",
        ".id",
        ".shell",
        ".os",
        ".up",
        ".random",
        ".start"
    ]
    for cmd in commands:
        print(cmd)

def main():
    clear()
    while True:
        try:
            user_input = input("Grubby> ").strip()
            if not user_input:
                continue
            
            if user_input == ".help":
                help_menu()
            elif user_input == ".exit":
                print("Exiting...")
                break
            elif user_input == ".clear":
                clear()
            elif user_input == ".hello":
                print("Hello there!")
            elif user_input == ".date":
                os.system("date")
            elif user_input == ".ping":
                print("Pong!")
            elif user_input == ".info":
                print("Grubby Terminal Tool - Version 1.0")
            elif user_input == ".sys":
                os.system("uname -a")
            elif user_input == ".whoami":
                os.system("whoami")
            elif user_input == ".ls":
                os.system("ls")
            elif user_input == ".pwd":
                os.system("pwd")
            elif user_input == ".banner":
                print("GRUBBY")
            elif user_input == ".slap":
                print("*slaps the screen*")
            elif user_input == ".joke":
                print("Why do programmers prefer dark mode? Because light attracts bugs.")
            elif user_input == ".sleep":
                print("Going to sleep... zzz...")
            elif user_input == ".count":
                for i in range(1, 6): print(i)
            elif user_input == ".cowsay":
                os.system("cowsay 'Grubby is awesome'")
            elif user_input == ".sysinfo":
                os.system("cat /proc/version")
            elif user_input == ".ip":
                os.system("ifconfig")
            elif user_input == ".time":
                os.system("date +%T")
            elif user_input == ".color":
                print("Color support active.")
            elif user_input == ".love":
                print("<3")
            elif user_input == ".bye":
                print("Goodbye!")
                break
            elif user_input == ".calc":
                print("Usage: Use .calc [number] + [number]")
            elif user_input == ".hack":
                print("Accessing mainframe... 100% complete.")
            elif user_input == ".dev":
                print("Developed by johnsonsetiawan17-svg")
            elif user_input == ".wait":
                time.sleep(2)
                print("Done waiting.")
            elif user_input == ".echo":
                print("Echo...")
            elif user_input == ".host":
                os.system("hostname")
            elif user_input == ".id":
                os.system("id")
            elif user_input == ".shell":
                print("Shell active.")
            elif user_input == ".os":
                print("Android / Termux")
            elif user_input == ".up":
                print("System is up.")
            elif user_input == ".random":
                print(random.randint(1, 1000))
            elif user_input == ".start":
                print("System starting...")
            else:
                print(f"Unknown command: {user_input}")
        except EOFError:
            break

if __name__ == "__main__":
    main()
