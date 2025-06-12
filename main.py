import re
import base64
import random
import string
from math import log2
import tkinter as tk
from tkinter import messagebox, simpledialog

def get_user_info():
    messagebox.showinfo("🤖 Hello, human!", "I promise I won't steal your data... or will I? Just kidding. 😆")
    
    while True:
        name = simpledialog.askstring("👤 Name Input", "Enter your full name (First & Last):").strip()
        if len(name.split()) < 2:
            messagebox.showwarning("⚠️ Nice try!", "But I need both your first and last name. Leave space between them.")
            continue
        break
    
    while True:
        dob = simpledialog.askstring("📅 DOB Input", "Enter your date of birth (YYYY-MM-DD):").strip()
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', dob):
            messagebox.showerror("🚨 Oops!", "That’s not a valid format. Try again: YYYY-MM-DD")
            continue
        break
    
    messagebox.showinfo("✅ Password Check", "Now let's see if your password is as strong as my biceps. I have been hitting the gym lately. 💪")
    return name.lower(), dob

def extract_pii(name, dob):
    first_name, last_name = name.split()[0], name.split()[-1]
    birth_year = dob.split('-')[0]
    return first_name, last_name, birth_year

def check_pii_in_password(password, first_name, last_name, birth_year):
    pii_detected = [
        f"First name ({first_name})" if first_name in password.lower() else None,
        f"Last name ({last_name})" if last_name in password.lower() else None,
        f"Birth year ({birth_year})" if birth_year in password else None
    ]
    return [item for item in pii_detected if item]

def calculate_entropy(password):
    char_pool = len(set(password))
    entropy = len(password) * log2(char_pool) if char_pool > 0 else 0
    return entropy

def check_password_strength(password, first_name, last_name, birth_year):
    criteria = {
        "🔠 Uppercase letter": bool(re.search(r'[A-Z]', password)),
        "🔡 Lowercase letter": bool(re.search(r'[a-z]', password)),
        "🔢 Digit": bool(re.search(r'\d', password)),
        "🔣 Special character": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
        "📏 Length (8+ chars)": len(password) >= 8
    }
    common_passwords = {"password", "123456", "admin", "qwerty", "letmein"}
    is_common = password.lower() in common_passwords
    
    # Check if password contains PII (personal information)
    pii_detected = check_pii_in_password(password, first_name, last_name, birth_year)
    if pii_detected:
        return "💀 Weak (Contains your personal information!)", 0, pii_detected  # Force weak if PII detected

    score = sum(criteria.values()) - int(is_common)
    entropy = calculate_entropy(password)
    
    if score <= 2 or entropy < 28:
        strength = "💀 Weak (Hackers love this one!)"
    elif score <= 4 or entropy < 36:
        strength = "😬 Medium (Still risky... like eating upma)"
    else:
        strength = "💪 Strong (Even your pet hamster couldn't guess this!)"
    
    feedback = [msg for msg, passed in criteria.items() if not passed]
    if is_common:
        feedback.append("❌ Avoid common passwords like 'password123'. Even your sperm could guess that!")
    
    return strength, entropy, feedback

def generate_safe_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    safe_password = ''.join(random.choice(characters) for _ in range(16))
    encrypted_password = base64.b64encode(safe_password.encode()).decode()
    return safe_password, encrypted_password

def main():
    root = tk.Tk()
    root.withdraw()
    name, dob = get_user_info()
    first_name, last_name, birth_year = extract_pii(name, dob)
    
    password = simpledialog.askstring("🔑 Password Input", "Enter your password for analysis:", show='*').strip()
    
    pii_detected = check_pii_in_password(password, first_name, last_name, birth_year)
    strength, entropy, feedback = check_password_strength(password, first_name, last_name, birth_year)
    
    analysis_msg = f"\n📊 === Password Analysis === \n\n"
    analysis_msg += f"🔹 Strength: {strength}\n"
    analysis_msg += f"🔹 Entropy Score: {entropy:.2f} bits (Higher is better)\n"
    
    if pii_detected:
        analysis_msg += "\n⚠️ Do you have amnesia or what? Your password contains your personal information:\n"
        for pii in pii_detected:
            analysis_msg += f"❌ {pii}\n"
        analysis_msg += "➡️ Even your 90-year-old neighbor could guess this. Change it! Now.\n"
    
    if feedback:
        analysis_msg += "\n💡 Suggestions for a stronger password:\n"
        for tip in feedback:
            analysis_msg += f"✔️ {tip}\n"
    
    messagebox.showinfo("Password Analysis", analysis_msg)
    
    safe_password, encrypted_password = generate_safe_password()
    messagebox.showinfo("🔐 Safe Password", f"Your **ENCRYPTED** safe password: {encrypted_password}\n\nTo decrypt it, use:\nbase64.b64decode('your_encrypted_password').decode()")
    
    security_tips = "\n✅ Some tips to save your unaware ass from a nerd who hacks:\n"
    security_tips += "- Use at least 12-16 characters or more.\n"
    security_tips += "- Mix uppercase, lowercase, numbers, and symbols.\n"
    security_tips += "- Consider using a **passphrase** instead of a password.\n"
    security_tips += "- **Enable 2FA** (Two-Factor Authentication) everywhere!\n"
    security_tips += "- Use a **password manager**. Please don't use Notepad or Notes app!\n"
    security_tips += "- If your password is '123456', I can't save you. Sorry.\n"
    
    messagebox.showinfo("🔐 Stay Safe!", security_tips)
    
    messagebox.showinfo("Final Warning", "Save your ass from data theft. Keep your passwords strong without using PII.\nI will hack your system, find your location, and laugh at you if your password is weak! 😂")
    
if __name__ == "__main__":
    main()
