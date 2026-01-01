
# 🔐 Advanced Password Generator (CustomTkinter)

A modern desktop password generator built with **Python** and **CustomTkinter**, designed to create strong passwords and memorable passphrases with **visual feedback** and **smooth animations**.

---

## ✨ Features

### 🔑 Password Generator
- Custom length selection  
- Include/exclude options:  
  - Lowercase letters  
  - Uppercase letters  
  - Digits  
  - Special characters  
- Automatically removes similar-looking characters (`i l 1 L o 0 O`)  
- 👁 Show / Hide password button  
- 📊 Real-time strength meter  
- 🎨 Color-changing progress bar  
- 💥 Shake animation for weak passwords  
- 🌊 Pulse animation for very strong passwords  

### 🧩 Passphrase Generator
- Generates easy-to-remember word-based passphrases  
- Custom number of words  
- Custom separator (`-`, `_`, `.`, etc.)  
- Capitalized words for better readability  
- Entropy-based strength analysis  

### 🧠 Password Strength Logic
- Strength calculated using **entropy (bits)**  
- Visual indicators:  
  - 🔴 Very Weak  
  - 🟠 Weak  
  - 🟡 Reasonable  
  - 🟢 Strong  
  - 🔵 Very Strong  

### 🖥️ User Interface
- Built using **CustomTkinter**  
- 🌙 Dark mode UI  
- Tab-based layout:  
  - Password  
  - Passphrase  
- Smooth animations for better user experience  

---

## 📦 Requirements
- Python **3.9+**  
- Install required library:  
  ```bash
  pip install customtkinter
  ```

---

## ▶️ How to Run
```bash
python password_generator.py
```

---

## 📁 Project Structure
```
📂 Password-Generator
 ┣ 📄 password_generator.py
 ┣ 📄 README.md
```

---

## 🎯 Use Cases
- Creating strong passwords for online accounts  
- Generating secure yet memorable passphrases  
- Learning GUI development with Python  
- Understanding entropy-based password strength  

---

## 🧪 Security Notes
- Uses Python’s **secrets** module for cryptographically secure randomness  
- Avoids ambiguous characters  
- No passwords are stored or logged  

---

## 🚀 Future Improvements
- 📋 Copy-to-clipboard button  
- 🕑 Password history  
- 📤 Export passwords securely  
- 🔄 Animated tab transitions  

---

✅ This `README.md` is ready to drop into your project folder. It highlights your features, usage instructions, and future improvements in a professional, GitHub-friendly format.  

Would you like me to also design a **badge section** (e.g., Python version, license, stars) at the top to make it look even more like a polished open-source project?
