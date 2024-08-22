import os
import shutil
import webbrowser
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from PIL.ExifTags import TAGS

# Define the correct unlock code
UNLOCK_CODE = "PT164"

# Function to extract the date from photo metadata


def extract_date(photo_path):
    try:
        image = Image.open(photo_path)
        exif_data = image._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                if TAGS.get(tag) == 'DateTimeOriginal':
                    return value.split(' ')[0].replace(':', '-')
    except Exception as e:
        print(f"Error extracting date from {photo_path}: {e}")
    return None

# Function to organize photos


def organize_photos(source_folder, destination_folder):
    if not os.path.exists(source_folder):
        messagebox.showerror("Error", "Source folder does not exist.")
        return

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                photo_path = os.path.join(root, file)
                date = extract_date(photo_path)
                if date:
                    date_folder = os.path.join(destination_folder, date)
                    if not os.path.exists(date_folder):
                        os.makedirs(date_folder)
                    shutil.copy2(photo_path, date_folder)

    messagebox.showinfo("Success", "Photos organized successfully.")

# Function to select source folder


def select_source_folder():
    source_folder.set(filedialog.askdirectory())

# Function to select destination folder


def select_destination_folder():
    destination_folder.set(filedialog.askdirectory())

# Function to start organizing


def start_organizing():
    organize_photos(source_folder.get(), destination_folder.get())

# Function to open payment link


def open_payment_link():
    payment_url = "https://www.aurawave.eu//_paylink/AZFtMv8L"
    webbrowser.open(payment_url)

# Function to verify and handle the code


def verify_code():
    entered_code = code_entry.get()
    if entered_code == UNLOCK_CODE:
        messagebox.showinfo("Success", "Code accepted. Unlocking program...")
        payment_window.withdraw()
        main_window.deiconify()
    else:
        messagebox.showerror("Error", "Invalid code. Please try again.")

# Function to confirm exit


def confirm_exit():
    result = messagebox.askokcancel(
        "Exit", "Don't forget to visit our shop aurawave.eu :)")
    if result:
        main_window.destroy()

# Function to handle closing of the payment window


def on_payment_window_close():
    result = messagebox.askokcancel(
        "Reminder", "Don't forget to visit our shop aurawave.eu :)")
    if result:
        payment_window.destroy()


# Initialize payment window
payment_window = Tk()
payment_window.title("Payment Required")
payment_window.geometry("600x500")
payment_window.configure(bg="#c0c0c0")
payment_window.resizable(False, False)

# Load the QR code image
qr_image_path = "qrphototidy.png"  # Ensure this path is correct
try:
    qr_image = Image.open(qr_image_path)
    qr_image = qr_image.resize((150, 150), Image.Resampling.LANCZOS)
    qr_photo = ImageTk.PhotoImage(qr_image)
except Exception as e:
    print(f"Error loading QR image: {e}")
    qr_photo = None

# Bind the window close event to the on_payment_window_close function
payment_window.protocol("WM_DELETE_WINDOW", on_payment_window_close)

# Define button styles
button_style = {
    "bg": "#b0b0b0",
    "fg": "white",
    "relief": FLAT,
    "padx": 10,
    "pady": 4,
    "bd": 0,
    "highlightbackground": "#a8a8a8",
    "highlightthickness": 1
}

# Payment GUI Elements
frame_payment = Frame(payment_window, bg="#dcdcdc", padx=20, pady=20)
frame_payment.pack(expand=True, fill=BOTH)

Label(frame_payment, text="To unlock PhotoTidy 1.6.4, please make a payment of €1.19.",
      bg="#dcdcdc", fg="#333333", wraplength=460, justify=LEFT).grid(row=0, column=0, columnspan=2, pady=5, sticky="ew")
Label(frame_payment, text="This payment is processed through our shop for beachwear, AuraWave, located in Málaga, Spain. Thank you for your order!",
      bg="#dcdcdc", fg="#333333", wraplength=460, justify=LEFT).grid(row=1, column=0, columnspan=2, pady=5, sticky="ew")

# Display the QR code image if it was loaded successfully
if qr_photo:
    Label(frame_payment, image=qr_photo, bg="#dcdcdc").grid(
        row=2, column=0, pady=10, sticky="ew")

Button(frame_payment, text="Pay Now", command=open_payment_link, **
       button_style).grid(row=2, column=1, pady=(0, 5), sticky="ew")

Label(frame_payment, text="Enter the code sent to your email:", bg="#dcdcdc",
      fg="#333333").grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")
code_entry = Entry(frame_payment, width=40, borderwidth=1, relief=SUNKEN)
code_entry.grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")
Button(frame_payment, text="Submit Code", command=verify_code, height=2,
       **button_style).grid(row=6, column=0, columnspan=2, pady=10, sticky="ew")

# Ensure all columns expand equally
frame_payment.grid_columnconfigure(0, weight=1)
frame_payment.grid_columnconfigure(1, weight=1)

# Initialize main application window (hidden initially)
main_window = Toplevel()
main_window.title("PhotoTidy 1.6.4")
main_window.geometry("780x320")
main_window.configure(bg="#c0c0c0")
main_window.resizable(False, False)
main_window.withdraw()

# Variables to store folder paths
source_folder = StringVar()
destination_folder = StringVar()

# GUI Elements for main window
frame_main = Frame(main_window, bg="#dcdcdc", padx=20, pady=20)
frame_main.pack(expand=True, fill=BOTH)

Label(frame_main, text="Source Folder:", bg="#dcdcdc", fg="#333333").grid(
    row=0, column=0, sticky=W, padx=10, pady=5)
Entry(frame_main, textvariable=source_folder, width=35, borderwidth=1,
      relief=SUNKEN).grid(row=0, column=1, padx=10, pady=5)
Button(frame_main, text="Browse", command=select_source_folder,
       **button_style).grid(row=0, column=2, padx=10, pady=5)

Label(frame_main, text="Destination Folder:", bg="#dcdcdc",
      fg="#333333").grid(row=1, column=0, sticky=W, padx=10, pady=5)
Entry(frame_main, textvariable=destination_folder, width=35,
      borderwidth=1, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=5)
Button(frame_main, text="Browse", command=select_destination_folder,
       **button_style).grid(row=1, column=2, padx=10, pady=5)

Button(frame_main, text="Start", width=10, command=start_organizing,
       **button_style).grid(row=2, column=1, pady=20)
Button(frame_main, text="Exit", width=10, command=confirm_exit,
       **button_style).grid(row=2, column=2, pady=20)

description_text = (
    "PhotoTidy 1.6.4 - Efficiently organizes your photos by date, creating a structured folder system "
    "for easy access. Simply select your source and destination folders, and let PhotoTidy handle the "
    "rest. This tool helps you keep your photo collection neat and sorted. Developed by Mirko Secchi."
)
Label(frame_main, text=description_text, bg="#dcdcdc", fg="#333333", wraplength=680,
      justify=LEFT).grid(row=3, column=0, columnspan=3, padx=10, pady=20)

# Start the payment window loop
payment_window.mainloop()
