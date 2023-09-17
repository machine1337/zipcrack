import os
import platform
import time
print("[*] Checking Requirements Module....")
def header():
    ascii_banner = pyfiglet.figlet_format("{ZIP CRACKER}").upper()
    print(colored(ascii_banner.rstrip("\n"), 'cyan', attrs=['bold']))
    print(colored("                                <Coded By: Clay>     \n", 'yellow', attrs=['bold']))
    print(colored("                                <Version: 2.0>     \n", 'magenta', attrs=['bold']))
    return
if platform.system().startswith("Windows"):
    try:
        from tqdm import tqdm
    except ImportError:
        os.system("python -m pip install tqdm -q -q -q")
        from tqdm import tqdm
    try:
        import termcolor
    except ImportError:
        os.system("python -m pip install termcolor -q -q -q")
        import termcolor
    from termcolor import colored
    try:
        import pyfiglet
    except ImportError:
        os.system("python -m pip install pyfiglet -q -q -q")
        import pyfiglet
elif platform.system().startswith("Linux"):
    try:
        from tqdm import tqdm
    except ImportError:
        os.system("python3 -m pip install tqdm -q -q -q")
        from tqdm import tqdm
    try:
        import termcolor
    except ImportError:
        os.system("python3 -m pip install termcolor -q -q -q")
        import termcolor
    from termcolor import colored
    try:
        import pyfiglet
    except ImportError:
        os.system("python3 -m pip install pyfiglet -q -q -q")
        import pyfiglet
def linuxpdf():
    os.system("clear")
    header()
    zip_filename = input(termcolor.colored("[*] Enter Path Of Your zip file:- ", 'cyan'))
    if not os.path.exists(zip_filename):
        print(termcolor.colored("\n[ X ] File " + zip_filename + " was not found, Provide Valid FileName And Path!",
                                'red'))
        exit()
    print(termcolor.colored("\n[*] Analyzing Zip File:- ", 'blue'), zip_filename)
    time.sleep(1)
    if zip_filename[-3:] == "zip":
        print(termcolor.colored("\n[ ✔ ] Valid ZIP File Found...", 'green'))
    else:
        print(termcolor.colored("\n[ X ] This is not a valid .zip file...\n", 'red'))
        exit()
    pwd_filename = input(termcolor.colored("\nEnter Path Of Your Wordlist:- ", 'yellow'))
    if not os.path.exists(pwd_filename):
        print(termcolor.colored("\n[ X ] File " + pwd_filename + " was not found, Provide Valid FileName And Path!",
                                'red'))
        exit()
    with open(pwd_filename, "rb") as passwords:
        passwords_list = passwords.readlines()
        total_passwords = len(passwords_list)
        my_zip_file = zipfile.ZipFile(zip_filename)
        for index, password in enumerate(passwords_list):
            try:
                my_zip_file.extractall(path="Extracted Folder", pwd=password.strip())
                print(colored("\n{***********************SUCCESS***********************}", 'green'))
                print(colored("[ ✔ ] ZIP FILE Password Found:- ", 'cyan'), password.decode().strip())
                break
            except:
                helo = round((index / total_passwords) * 100, 2)
                if helo == '100%':
                    print(colored("[ X ] ALL ATTEMPTS FAILED", 'red'))
                else:
                    print(colored(f"[*] Trying password:- {password.decode().strip()} ", 'green'))
                continue
def winpdf():
    os.system("cls")
    header()
    zip_filename = input(termcolor.colored("Enter Path Of Your zip file:- ", 'cyan'))
    if not os.path.exists(zip_filename):
        print(termcolor.colored("\n[ X ] File " + zip_filename + " was not found, Provide Valid FileName And Path!",
                                'red'))
        exit()
    print(termcolor.colored("\n[*] Analyzing Zip File:- ", 'blue'), zip_filename)
    time.sleep(2)
    if zip_filename[-3:] == "zip":
        print(termcolor.colored("\n[ ✔ ] Valid ZIP File Found...", 'green'))
    else:
        print(termcolor.colored("\n[ X ] This is not a valid .zip file...\n", 'red'))
        exit()
    pwd_filename = input(termcolor.colored("\nEnter Path Of Your Wordlist:- ", 'yellow'))

    if not os.path.exists(pwd_filename):
        print(termcolor.colored("\n[ X ] File " + pwd_filename + " was not found, Provide Valid FileName And Path!",
                                'red'))
        exit()
    with open(pwd_filename, "rb") as passwords:
        passwords_list = passwords.readlines()
        total_passwords = len(passwords_list)
        my_zip_file = zipfile.ZipFile(zip_filename)
        for index, password in enumerate(passwords_list):
            try:
                my_zip_file.extractall(path="Extracted Folder", pwd=password.strip())
                print(colored("\n{***********************SUCCESS***********************}", 'green'))
                print(colored("[ ✔ ] ZIP FILE Password Found:- ", 'cyan'), password.decode().strip())
                break
            except:
                helo = round((index / total_passwords) * 100, 2)
                if helo == '100%':
                    print(colored("[ X ] ALL ATTEMPTS FAILED", 'red'))
                else:
                    print(colored(f"[*] Trying password:- {password.decode().strip()} ", 'green'))
                continue
def catc():
    try:
        if platform.system().startswith("Linux"):
            linuxpdf()
        elif platform.system().startswith("Windows"):
            winpdf()
    except KeyboardInterrupt:
        print(termcolor.colored("\nYou Pressed The Exit Button!", 'red'))
        quit()


catc()
