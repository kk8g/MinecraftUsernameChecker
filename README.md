# Minecraft Username Checker

This program is a Minecraft username availability checker. It can generate random usernames based on user-defined criteria, check their availability using the Minecraft API, and send the available usernames to a Discord webhook.

---

## Features

- Generate random usernames with letters, digits, and underscores.
- Check availability of usernames using the Minecraft Services API.
- Send available usernames to a Discord webhook.
- Support for custom user input of usernames.
- Colorful terminal output with ASCII art.

---

## Requirements

- Python 3.10 or higher
- Packages: `requests`, `fade`, `colorama`

You can install the required packages using:

```bash
pip install requests fade colorama
```

---

## How to Use

1. **Run the Program**

```bash
python minecraft_username_checker.py
```

2. **Choose Input Method**

You can either input your own usernames or generate random ones.

- **Custom Input**: Enter a JSON array of usernames, e.g., `["username1", "username2"]`.
- **Random Generation**: Specify the number of usernames, length, and whether to include letters, digits, and underscores.

3. **Username Processing**

The program will check up to 100 usernames in batches of 10 using the Minecraft API.

4. **Results**

Available usernames are displayed in the terminal.

5. **Discord Integration**

Available usernames are sent to a specified Discord webhook. Replace `WEBHOOK_URL_HERE` in the script with your webhook URL.

---

## Functions Overview

- `generate_random_usernames`: Generates random usernames based on the selected options.
- `bulk_lookup`: Sends a batch of usernames to the Minecraft API to check availability.
- `filter_usernames`: Filters out unavailable usernames.
- `send_to_discord`: Sends available usernames to a Discord webhook in chunks.
- `get_usernames_from_input`: Safely gets custom usernames from the user.
- `center_text`: Centers ASCII art in the terminal.
- `current_time_str`: Returns current timestamp for logs and webhooks.

---

## Notes

- Maximum 100 usernames are processed per run.
- Batch size is 10 to avoid API rate limiting.
- Generated usernames are automatically converted to lowercase.
- The program includes colorful ASCII art and uses the `fade` library for effects.
- Sending to Discord is delayed by 2 seconds between chunks to avoid webhook spam.

---

**Author:** K K 8 G

