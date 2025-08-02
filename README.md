# Password-manager

A simple command-line password manager written in Python. This program allows you to securely generate, store, and retrieve passwords for different sites using basic encryption methods and an SQLite database.

## Features

- **Password Generation:** Randomly generates strong 5-character passwords.
- **Encryption:** Encrypts passwords using one of three custom encryption methods before storing them.
- **Database Storage:** Stores encrypted passwords, usernames, and site information in an SQLite database (`database.db`).
- **Password Retrieval:** Allows you to retrieve and decrypt stored passwords for any registered site.

## How It Works

- When registering a new site, the program generates a password, encrypts it, and saves it along with the username and site name.
- When retrieving a password, the program fetches the encrypted password from the database, decrypts it, and displays the username and password.

## Usage

1. **Run the Program**

   Open a terminal in the project directory and run:

   ```sh
   python start.py
   ```

2. **Choose an Option**

   - Enter `1` to register a new site.
   - Enter `2` to find an existing site.

3. **Register a New Site**

   - Enter the site name and username when prompted.
   - The program will generate and store a new password for the site.

4. **Find an Existing Site**

   - Enter the site name when prompted.
   - The program will display the username and decrypted password for the site.

## Database

The program uses an SQLite database file named `database.db` to store all credentials. The table `secrets` is created automatically if it does not exist.

## Notes

- All encryption and decryption logic is implemented in [`main.py`](main.py).
- The main entry point for the program is [`start.py`](start.py).
- This program was written multiple years ago and is no longer in use by me. 
- I do not recommend using this program to encrypt/decrypt and store passwords used. 
- This should only be used as an example of how sqlite can be implemented in a project. 

---