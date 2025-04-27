# COMPILED 27/4/25

import random
import string
import requests
import json
import time
import fade
from datetime import datetime
from colorama import Fore, Style, init
import shutil

# Init colorama
init(autoreset=True)

ascii_art = """
 ██▒   █▓ ██▓▓█████  █     █░ ███▄ ▄███▓ ▄▄▄     ▄▄▄█████▓ ██▀███   ██▓▒██   ██▒
▓██░   █▒▓██▒▓█   ▀ ▓█░ █ ░█░▓██▒▀█▀ ██▒▒████▄   ▓  ██▒ ▓▒▓██ ▒ ██▒▓██▒▒▒ █ █ ▒░
 ▓██  █▒░▒██▒▒███   ▒█░ █ ░█ ▓██    ▓██░▒██  ▀█▄ ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██▒░░  █   ░
  ▒██ █░░░██░▒▓█  ▄ ░█░ █ ░█ ▒██    ▒██ ░██▄▄▄▄██░ ▓██▓ ░ ▒██▀▀█▄  ░██░ ░ █ █ ▒ 
   ▒▀█░  ░██░░▒████▒░░██▒██▓ ▒██▒   ░██▒ ▓█   ▓██▒ ▒██▒ ░ ░██▓ ▒██▒░██░▒██▒ ▒██▒
   ░ ▐░  ░▓  ░░ ▒░ ░░ ▓░▒ ▒  ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒▓ ░▒▓░░▓  ▒▒ ░ ░▓ ░
   ░ ░░   ▒ ░ ░ ░  ░  ▒ ░ ░  ░  ░      ░  ▒   ▒▒ ░   ░      ░▒ ░ ▒░ ▒ ░░░   ░▒ ░
     ░░   ▒ ░   ░     ░   ░  ░      ░     ░   ▒    ░        ░░   ░  ▒ ░ ░    ░  
      ░   ░     ░  ░    ░           ░         ░  ░           ░      ░   ░    ░  
     ░                                                        @ K K 8 G

    >_ If you want the program run faster, Pay me for proxies :D  
                                                                
"""

fade_ascii_art = fade.blackwhite(ascii_art)

# API endpoint
url = "https://api.minecraftservices.com/minecraft/profile/lookup/bulk/byname"
WEBHOOK_URL = "WEBHOOK_URL_HERE"

# get current timestamp for logs and webhook
def current_time_str():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z")

# generate random usernames based on user inputs
def generate_random_usernames(count, length, use_letters, use_digits, use_underscore):
    usernames = []
    for _ in range(count):
        username = ""
        
        if use_letters:
            username += ''.join(random.choice(string.ascii_lowercase) for _ in range(length))  # Force lowercase letters
        
        if use_digits:
            username += ''.join(random.choice(string.digits) for _ in range(length))
        
        if use_underscore:
            username = ''.join(random.choice(string.ascii_lowercase + string.digits + "_") for _ in range(length))  # Force lowercase letters
        
        username = username[:length]
        
        username = username.lower()

        usernames.append(username)

    return usernames

# send request to minecraft services API
def bulk_lookup(usernames):
    payload = json.dumps(usernames)
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post(url, data=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"{Fore.RED}Error: {response.status_code}")
        print(response.text)
        return None

# send already processed usernames to Discord
def send_to_discord(usernames):
    for i in range(0, len(usernames), 5):
        chunk = usernames[i:i + 5]
        embed = {
            "title": "Available Minecraft Usernames",
            "description": f"Here are {len(chunk)} available usernames:",
            "color": 3066993,
            "fields": [{"name": name, "value": " ", "inline": False} for name in chunk],
            "timestamp": current_time_str(),
        }

        payload = {"embeds": [embed]}

        response = requests.post(WEBHOOK_URL, json=payload)

        if response.status_code == 204:
            print(f"{current_time_str()} Successfully sent {len(chunk)} usernames to Discord.")
        else:
            print(f"Failed to send to Discord. Status Code: {response.status_code}")
            print(f"Error Response: {response.text}")
        
        time.sleep(2)

# filter available usernames
def filter_usernames(usernames):
    available = []
    batch_size = 10
    max_to_process = 100

    print(f"{Fore.YELLOW}Processing up to {max_to_process} usernames...")

    for i in range(0, min(max_to_process, len(usernames)), batch_size):
        batch = usernames[i:i + batch_size]
        print(f"{Fore.YELLOW}Checking batch: {batch}")
        result = bulk_lookup(batch)

        if result is not None:
            for username in batch:
                if not any(profile['name'].lower() == username.lower() for profile in result):
                    available.append(username)
        else:
            print(f"{Fore.RED}Skipping batch due to API error.")

        time.sleep(2)

    return available

# center the art in the terminal
def center_text(text):
    terminal_width = shutil.get_terminal_size().columns
    lines = text.splitlines()
    centered_lines = [line.center(terminal_width) for line in lines]
    return "\n".join(centered_lines)

# get user input safely
def get_usernames_from_input():
    while True:
        try:
            custom_input = input(f"{Fore.MAGENTA}Please enter your usernames in the format [\"username1\", \"username2\"]: ")
            # Attempt to parse the input as JSON
            usernames = json.loads(custom_input)

            # Validate if all items are strings
            if not all(isinstance(username, str) for username in usernames):
                raise ValueError("All items must be strings.")

            return usernames
        except json.JSONDecodeError:
            print(f"{Fore.RED}Invalid format. Please make sure your input is a valid JSON array of strings.")
        except ValueError as e:
            print(f"{Fore.RED}{str(e)}. Please make sure all usernames are valid strings.")

# main func
def main():
    print(center_text(fade_ascii_art))

    use_custom = input(f"{Fore.MAGENTA}Do you want to input your own list of usernames? (y/n): ").lower() == 'y'
    
    if use_custom:
        usernames = get_usernames_from_input()
        print(f"{Fore.GREEN}Using custom usernames: {usernames}")
    else:
        try:
            total = int(input(f"{Fore.MAGENTA}How many usernames to generate? (max 100): "))
            if total > 100: total = 100
        except ValueError:
            total = 50

        try:
            length = int(input(f"{Fore.MAGENTA}Username length (3–16 recommended): "))
            if length < 3: length = 3
        except ValueError:
            length = 4

        use_letters = input(f"{Fore.MAGENTA}Include letters? (y/n): ").lower() == "y"
        use_digits = input(f"{Fore.MAGENTA}Include digits? (y/n): ").lower() == "y"
        use_underscore = input(f"{Fore.MAGENTA}Include underscores? (y/n): ").lower() == "y"

        usernames = generate_random_usernames(
            count=total,
            length=length,
            use_letters=use_letters,
            use_digits=use_digits,
            use_underscore=use_underscore
        )

    print(f"{Fore.GREEN}Generated {len(usernames)} usernames.")
    
    available_usernames = filter_usernames(usernames)

    print(f"{Fore.GREEN}Final Available Usernames:")
    if available_usernames:
        for name in available_usernames:
            print(f"{Fore.GREEN}{name}")
    else:
        print(f"{Fore.RED}None found.")

    # send usernames to discord
    send_to_discord(available_usernames)

if __name__ == "__main__":
    main()
