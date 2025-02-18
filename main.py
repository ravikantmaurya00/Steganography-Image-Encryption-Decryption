import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel, scrolledtext
from PIL import Image, ImageTk
import ttkbootstrap as ttk  # Advanced UI styling

def encrypt_image():
    global img_path, img
    msg = msg_entry.get("1.0", tk.END).strip()
    password = password_entry.get()

    if not msg or not password or not img_path:
        messagebox.showerror("Error", "Please select an image, enter a message, and a password.")
        return

    d = {chr(i): i for i in range(256)}

    n, m, z = 0, 0, 0

    try:
        for i in range(len(msg)):
            img[n, m, z] = d[msg[i]]
            n = (n + 1) % img.shape[0]
            m = (m + 1) % img.shape[1]
            z = (z + 1) % 3
    except IndexError:
        messagebox.showerror("Error", "Message too long to fit in the image.")
        return

    encrypted_img_path = "encryptedImage.png"
    cv2.imwrite(encrypted_img_path, img)

    result_label.config(text=f"Image encrypted and saved as {encrypted_img_path}", foreground='green')
    show_encrypted_image(encrypted_img_path)

def decrypt_image():
    global img_path, img
    pas = decrypt_password_entry.get()
    password = password_entry.get()

    if not pas or not img_path or not password:
        messagebox.showerror("Error", "Please select an image and enter the password.")
        return

    if password == pas:
        message = ""
        n, m, z = 0, 0, 0
        try:
            for i in range(len(msg_entry.get("1.0", tk.END).strip())):
                message += chr(img[n, m, z])
                n = (n + 1) % img.shape[0]
                m = (m + 1) % img.shape[1]
                z = (z + 1) % 3
        except IndexError:
            messagebox.showerror("Error", "Corrupted image or incorrect password.")
            return
        
        show_decrypted_message(message)
    else:
        messagebox.showerror("Error", "Incorrect password.")

def show_decrypted_message(message):
    dialog = Toplevel(root)
    dialog.title("Decrypted Message")
    dialog.geometry("400x300")
    
    label = ttk.Label(dialog, text="Decrypted Message:", font=("Arial", 12, "bold"))
    label.pack(pady=10)
    
    text_area = scrolledtext.ScrolledText(dialog, wrap=tk.WORD, width=50, height=10)
    text_area.pack(padx=10, pady=10)
    text_area.insert(tk.END, message)
    text_area.config(state=tk.DISABLED)
    
    close_button = ttk.Button(dialog, text="Close", command=dialog.destroy, bootstyle="danger")
    close_button.pack(pady=10)

def show_encrypted_image(image_path):
    dialog = Toplevel(root)
    dialog.title("Encrypted Image")
    dialog.geometry("350x350")
    
    img = Image.open(image_path)
    img = img.resize((300, 300), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    
    label = ttk.Label(dialog, image=photo)
    label.image = photo  # Keep a reference
    label.pack(pady=10)
    
    close_button = ttk.Button(dialog, text="Close", command=dialog.destroy, bootstyle="danger")
    close_button.pack(pady=10)

def open_image():
    global img_path, img
    img_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")])
    if img_path:
        try:
            img = cv2.imread(img_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(img)
            image = image.resize((300, 300), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            image_label.config(image=photo)
            image_label.image = photo
            result_label.config(text="")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open image: {e}")
            img_path = None
            img = None

# UI Setup
root = ttk.Window(themename="darkly")
root.title("Secure Data Hiding in Image using Steganography")
root.geometry("500x650")

# Heading
heading_label = ttk.Label(root, text="Image Steganography Project", font=("Arial", 16, "bold"))
heading_label.pack(pady=10)

# Image Display
image_label = ttk.Label(root)
image_label.pack(pady=10)
open_button = ttk.Button(root, text="Open Image", command=open_image, bootstyle="primary")
open_button.pack(pady=5)

# Encryption
msg_label = ttk.Label(root, text="Enter secret message:")
msg_label.pack()
msg_entry = tk.Text(root, width=50, height=5)
msg_entry.pack()

password_label = ttk.Label(root, text="Enter passcode:")
password_label.pack()
password_entry = ttk.Entry(root, width=40, show="*")
password_entry.pack()

encrypt_button = ttk.Button(root, text="Encrypt", command=encrypt_image, bootstyle="success")
encrypt_button.pack(pady=10)

# Decryption
decrypt_password_label = ttk.Label(root, text="Enter passcode for Decryption:")
decrypt_password_label.pack()
decrypt_password_entry = ttk.Entry(root, width=40, show="*")
decrypt_password_entry.pack()

decrypt_button = ttk.Button(root, text="Decrypt", command=decrypt_image, bootstyle="danger")
decrypt_button.pack(pady=10)

result_label = ttk.Label(root, text="", font=("Arial", 12))
result_label.pack()

img_path, img = None, None
root.mainloop()
