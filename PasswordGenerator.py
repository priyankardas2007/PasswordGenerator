import customtkinter as ctk
import string
import secrets
import math

# ---------------- PASSWORD GENERATOR LOGIC ----------------
class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special_characters = string.punctuation

    def generate_password(self, length, lc, uc, dg, sp):
        pool = ""
        if lc: pool += self.lowercase
        if uc: pool += self.uppercase
        if dg: pool += self.digits
        if sp: pool += self.special_characters

        similar = "il1Lo0O"
        pool = ''.join(c for c in pool if c not in similar)

        if not pool:
            raise ValueError("Select at least one character type")

        return ''.join(secrets.choice(pool) for _ in range(length))

    def passphrase(self, words=4, sep="-"):
        word_list = [
            "apple","banana","carrot","dolphin","eagle","forest","guitar",
            "hammer","island","jungle","kitten","lantern","mountain",
            "notebook","octopus","penguin","quartz","river","sunset"
        ]
        selected = secrets.SystemRandom().sample(word_list, words)
        return sep.join(w.capitalize() for w in selected)

    def entropy(self, pwd):
        size = 0
        if any(c in self.lowercase for c in pwd): size += 26
        if any(c in self.uppercase for c in pwd): size += 26
        if any(c in self.digits for c in pwd): size += 10
        if any(c in self.special_characters for c in pwd): size += len(self.special_characters)
        if size == 0: size = 1
        return len(pwd) * math.log2(size)

    def strength(self, pwd):
        e = self.entropy(pwd)
        if e < 28: return "Very Weak", "red"
        if e < 36: return "Weak", "orange"
        if e < 60: return "Reasonable", "yellow"
        if e < 128: return "Strong", "green"
        return "Very Strong", "cyan"


# ---------------- GUI SETUP ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Advanced Password Generator")
app.geometry("520x520")

gen = PasswordGenerator()

title = ctk.CTkLabel(app, text="🔐 Password Generator", font=("Arial", 22, "bold"))
title.pack(pady=10)

# ---------------- TABS ----------------
tabs = ctk.CTkTabview(app)
tabs.pack(expand=True, fill="both", padx=10, pady=10)

tab_password = tabs.add("Password")
tab_passphrase = tabs.add("Passphrase")

# ================= PASSWORD TAB =================
length_entry = ctk.CTkEntry(tab_password)
length_entry.insert(0, "12")
length_entry.pack(pady=5)

lc = ctk.BooleanVar(value=True)
uc = ctk.BooleanVar(value=True)
dg = ctk.BooleanVar(value=True)
sp = ctk.BooleanVar(value=True)

ctk.CTkCheckBox(tab_password, text="Lowercase", variable=lc).pack()
ctk.CTkCheckBox(tab_password, text="Uppercase", variable=uc).pack()
ctk.CTkCheckBox(tab_password, text="Digits", variable=dg).pack()
ctk.CTkCheckBox(tab_password, text="Special", variable=sp).pack()

pwd_entry = ctk.CTkEntry(tab_password, width=360, show="*")
pwd_entry.pack(pady=10)
# 👁 Eye button
show_pwd = False
def toggle_eye():
    global show_pwd
    show_pwd = not show_pwd
    pwd_entry.configure(show="" if show_pwd else "*")

ctk.CTkButton(tab_password, text="👁 Show / Hide", command=toggle_eye).pack()

# Strength meter
strength_label = ctk.CTkLabel(tab_password, text="")
strength_label.pack(pady=5)

progress = ctk.CTkProgressBar(tab_password, width=350)
progress.pack(pady=5)
progress.set(0)

def generate_password():
    pwd = gen.generate_password(
        int(length_entry.get()),
        lc.get(), uc.get(), dg.get(), sp.get()
    )

    pwd_entry.delete(0, "end")
    pwd_entry.insert(0, pwd)

    entropy = gen.entropy(pwd)
    strength = gen.strength(pwd)
    color = strength_color(entropy)

    strength_label.configure(
        text=f"{strength} | Entropy: {entropy:.2f} bits",
        text_color=color
    )

    target = min(entropy / 128, 1)
    animate_strength_bar(target, color)

    if strength == "Very Strong":
        pulse_effect()

    if strength in ["Very Weak", "Weak"]:
        shake_widget(pwd_entry)


def strength_color(entropy):
    if entropy < 28:
        return "red"
    elif entropy < 36:
        return "orange"
    elif entropy < 60:
        return "yellow"
    elif entropy < 128:
        return "green"
    else:
        return "#00ffcc"  # neon cyan (Very Strong)

def shake_widget(widget):
    x = widget.winfo_x()
    y = widget.winfo_y()

    def shake(count=0):
        if count > 10:
            widget.place(x=x, y=y)
            return
        offset = -5 if count % 2 == 0 else 5
        widget.place(x=x + offset, y=y)
        app.after(40, lambda: shake(count + 1))

    shake()
def pulse_effect():
    colors = ["#00ffcc", "#00ffaa", "#00ffcc"]
    i = 0

    def pulse():
        nonlocal i
        progress.configure(progress_color=colors[i % len(colors)])
        i += 1
        if i < 12:
            app.after(120, pulse)

    pulse()

def animate_strength_bar(target, color):
    current = progress.get()
    step = 0.01 if target > current else -0.01

    progress.configure(progress_color=color)

    def animate():
        nonlocal current
        if (step > 0 and current < target) or (step < 0 and current > target):
            current += step
            progress.set(current)
            app.after(10, animate)
        else:
            progress.set(target)

    animate()


ctk.CTkButton(tab_password, text="Generate Password", command=generate_password).pack(pady=10)

# ================= PASSPHRASE TAB =================
words_entry = ctk.CTkEntry(tab_passphrase)
words_entry.insert(0, "4")
words_entry.pack(pady=5)

sep_entry = ctk.CTkEntry(tab_passphrase)
sep_entry.insert(0, "-")
sep_entry.pack(pady=5)

phrase_entry = ctk.CTkEntry(tab_passphrase, width=360)
phrase_entry.pack(pady=10)

phrase_strength = ctk.CTkLabel(tab_passphrase, text="")
phrase_strength.pack()

def generate_passphrase():
    phrase = gen.passphrase(int(words_entry.get()), sep_entry.get())
    phrase_entry.delete(0, "end")
    phrase_entry.insert(0, phrase)

    s, c = gen.strength(phrase)
    phrase_strength.configure(
        text=f"{s} | Entropy: {gen.entropy(phrase):.2f} bits",
        text_color=c
    )

ctk.CTkButton(tab_passphrase, text="Generate Passphrase", command=generate_passphrase).pack(pady=10)

app.mainloop()
