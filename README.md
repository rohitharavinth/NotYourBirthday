# NotYourBirthday
this is a password checker use it you will know what i mean NotYourBirthday is a application helps users analyze the strength of their passwords, check if they contain any personal information (like their name or birth year), and generate a safe, encrypted password. It provides feedback to improve password security and encryption for safer use.

use VSCODE ITS EASIER
Features:

Password Strength Analysis: Checks if a password is strong or weak based on certain criteria. Personal Information Detection: Analyzes if your password contains personal identifiable information (PII), like your name or birth year. Safe Password Generation: Generates a random 16-character password and encrypts it using Base64. Encrypted Password Display: Shows the encrypted password and how to decrypt it. Prerequisites Before running the project, make sure you have the following installed:

Python 3.x: This project requires Python 3.x. You can download it from python.org.

Python Libraries: You need to install the following Python libraries:

re (Regular Expressions) - Built-in Python library. base64 - Built-in Python library. random - Built-in Python library. string - Built-in Python library. math - Built-in Python library. tkinter - For creating the GUI (Graphical User Interface). It comes pre-installed with Python for most systems.

For most systems, the required libraries should already be available. If not, you can install them using the commands above.

Usage Run the Python script: Follow the on-screen prompts:

Enter your name and date of birth. Input a password for analysis. Receive feedback on password strength and suggestions to improve it. If your password is weak or contains personal information, you will receive an alert and suggestions for improvement.

If your password is strong and secure, a randomly generated encrypted password will be shown for your reference.

How to Decrypt the Safe Password After generating a safe password, you can decrypt it using the following Python code:

python Copy Edit import base64 encrypted_password = "your_encrypted_password" decrypted_password = base64.b64decode(encrypted_password).decode() print(decrypted_password)
