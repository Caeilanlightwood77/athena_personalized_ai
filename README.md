# Athena - Personalized AI Assistant

**Athena** is a Python-based personal assistant that interacts with users through voice and text. It can perform various tasks, such as managing a timetable, setting timers, generating random numbers, and sending emails. The assistant features a secure login system to ensure authorized access, providing a conversational experience with speech synthesis via `pyttsx3`.

## Features

- **Timetable Access**: Opens a pre-configured timetable (requires an external `timetable` module).
- **Timer**: Sets and runs a timer (requires an external `timer` module).
- **Random Number Generator**: Generates a random number within a specified range using a custom module (`number_generator`).
- **Email Sending**: Sends emails through an integrated email module (`send_email`), with support for 2FA and app passwords.
- **Secure Login**: Prompts for a username and password to ensure only authorized users can access Athena.
- **Speech and Text Interaction**: Uses `pyttsx3` for text-to-speech responses, allowing for a more interactive and immersive experience.

## Prerequisites

- **Python 3.x**
- **Dependencies**: Install the necessary libraries with the following command:
  ```bash
  pip install pyttsx3 stdiomask
  ```
- **Modules**: Athena requires additional modules (`timetable`, `timer`, `number_generator`, `send_email`). Ensure these are available in your project directory.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Caeilanlightwood77/athena_personalized_ai.git
   cd athena_personalized_ai
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place any required external modules (`timetable`, `timer`, `number_generator`, `send_email`) in the project directory.

## Usage

1. Run Athena:
   ```bash
   python Athena.py
   ```

2. **Login Prompt**: Athena will ask for a username and password. The default login credentials are:
   - **Username**: `HelloWorld`
   - **Password**: `H3ll0W0rld`

3. **Commands**:
   - **Timetable**: Enter keywords like "timetable" or "open timetable."
   - **Timer**: Use "timer" or "execute timer."
   - **Random Number Generator**: Say "random number" or "generate a random number."
   - **Send Email**: Enter "send email" to initiate the email-sending process.

4. **Two-Factor Authentication**:
   - To enhance security, enable 2FA on your email account (e.g., Gmail, Outlook). Follow the service's instructions to set it up.

5. **Using App Passwords**:
   - After enabling 2FA, you will need to generate an app password to send emails through Athena.
   - In Gmail:
     - Go to your Google Account.
     - Under the "Security" tab, find "Signing in to Google."
     - Select "App passwords," then generate a new app password for the application.
     - Use this app password instead of your regular password in the `send_email` module.

6. Athena will interact with you via voice and text, asking if you want to continue or end the program.

## Notes

- Ensure the `timetable`, `timer`, `number_generator`, and `send_email` modules are correctly implemented and accessible.
- Customize the login credentials in the `login()` function for better security.
- Keep your app password secure and do not share it with others.
