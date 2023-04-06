import random
import string
import time
import sys
import requests
from bs4 import BeautifulSoup

def opt():
    print("Choose an option:")
    print("[1] Generate Nitro Codes")
    print("[2] Check a Nitro Code list")
    print("[3] Exit")
    option = input("\n>> ")

    while option != "1" and option != "2" and option != "3":
        print("\n[-] Invalid option, please type an available one\n")
        print("[1] Generate Nitro Codes")
        print("[2] Check a Nitro Code list")
        print("[3] Exit")
        option = input("\n>> ")

    if option == "1":
        gen()
    elif option == "2":
        check()
    elif option == "3":
        print("\n[-] Going to sleep...")
        time.sleep(1)
        sys.exit()

def gen():
    codes = int(input("[+] ¿How many codes do you want to generate?\n>> "))
    dictionary = list(string.ascii_uppercase)+list(string.digits)+list(string.ascii_lowercase)
    code = ""
    with open("generated-codes.txt", "w") as file:
        file.write("")
    file.close()

    for i in range(codes):
        with open("generated-codes.txt", "a") as file:
            for i in range(16):
                caracter = random.choice(dictionary)
                code += caracter
            file.write(code+"\n")
            code = ""

    file.close()
    print("[*] Remember not to change the file's name to another one so you won't be able to check the codes after.")
    print("\n[+] Ready :D")

def check():
    print("[*] Remember that between each code validation there is a wait of 11 seconds due to api rules, so it will take a bit long...")
    with open("generated-codes.txt", "r") as file:
        for i in file.readlines():
            code = i.strip("\n")
            url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
            agent = {"User-Agent":"Firefox"}
            request = requests.get(url=url,headers=agent)
            soup = BeautifulSoup(request.text,"html.parser")
            if "Unknown Gift Code" in str(soup):
                #print("[-] Invalid Nitro Code ==> {}".format(code))
                pass
            else:
                print("[+] Found valid Nitro Code ==> {}".format(code))
            time.sleep(11)
    file.close()
    print("\n[+] Finished")

if __name__ == "__main__":
    try:
        opt()
    except KeyboardInterrupt:
        print("\n[-] Going to sleep...")
        time.sleep(1)
        sys.exit()