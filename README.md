# 🎓 Educational Keylogger

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-blue)
![License](https://img.shields.io/badge/License-Educational%20Only-orange)
![Security](https://img.shields.io/badge/Security-Authorized%20Testing%20Only-red)


**Created for Educational and Ethical Testing Purposes**  
© 2026 Educational Security Tools. All rights reserved.

---

## ⚠️ **CRITICAL WARNING: EDUCATIONAL PURPOSES ONLY**

> **🚨 This project is STRICTLY for educational and ethical testing purposes only.**
>
> **Unauthorized use is illegal and unethical.**

---

## 🚨 Legal Disclaimer

**⚖️ IMPORTANT LEGAL NOTICE:**
- **DO NOT use this software to monitor anyone without their explicit consent.**
- The author assumes **NO responsibility** for misuse or damages.
- By using this tool, you agree to use it **only for educational purposes** on systems you own or have written permission to test.
- **Unauthorized keylogging may be illegal** in your jurisdiction.
- **Check local laws and regulations** before use.

**🛡️ Ethical Guidelines:**
- Always obtain **written permission** before testing.
- Never use for malicious or unauthorized purposes.
- Keep logs secure and delete after testing.
- Respect privacy and comply with all data protection laws.
- Use in a controlled environment when possible.

---

## 📖 Project Description

This is an **intermediate-level Python keylogger** designed to demonstrate various system monitoring techniques for educational purposes. It serves as a learning tool for understanding cybersecurity concepts and system interaction programming.

---

## ✨ Features

**🔍 Monitoring Capabilities:**
- ⌨️ **Keyboard Input Logging** — Capture and log keystrokes
- 🖼️ **Screenshot Capture** — Automatic screen capture at intervals
- 🎤 **Audio Recording** — Record system audio for analysis
- 📋 **Clipboard Monitoring** — Track clipboard content changes
- 💻 **System Information Collection** — Gather system details
- 📶 **WiFi Password Extraction** — Retrieve saved WiFi credentials

**⚡ Technical Features:**
- Multi-threaded operation for efficiency
- Automatic dependency installation
- Clean file organization
- Error handling and logging
- Configurable capture intervals
- Secure data storage

---

## 🛠️ Requirements

**System Requirements:**
- **Python 3.6+**
- **Windows OS** (Windows 10/11 recommended)
- **Administrator privileges** (for some features)

**Dependencies:**
The following packages will be installed automatically if missing:
- `pynput` — Keyboard and mouse event handling
- `requests` — HTTP requests for data transmission
- `pywin32` — Windows API access
- `sounddevice` — Audio capture
- `scipy` — Scientific computing for audio processing
- `Pillow` — Image processing for screenshots

---

## 💻 Installation & Usage

### 🪟 Windows Installation

1. **Clone or download** the repository:
   ```bash
   git clone https://github.com/Soumit-Santra/Keylogger
   cd Keylogger
   ```

2. **Ensure Python 3.6+** is installed:
   ```bash
   python --version
   ```

3. **Run the script** (Administrator recommended):
   ```bash
   python keylogger.py
   ```

### 🚀 Usage Instructions

1. **⚠️ IMPORTANT: Run only on systems you own or have explicit written permission to test.**

2. **Execute the script:**
   ```bash
   python keylogger.py
   ```

3. **Monitor the output** — The script will create an `information` directory containing:
   ```
   information/
   ├── key_log.txt         # Keyboard inputs
   ├── system_info.txt     # System details
   ├── wifi_pass.txt       # Saved WiFi credentials
   ├── clipboard.txt       # Clipboard content
   ├── screenshots/        # Screen captures
   └── audio/             # Sound recordings
   ```

4. **Stop the program** safely using the configured key combination or by closing the terminal.

---

## 🎓 Educational Value

This project demonstrates several important programming and cybersecurity concepts:

**Programming Concepts:**
- **File Operations** — Reading, writing, and organizing files
- **System Interaction** — Interfacing with OS APIs
- **Multi-threading** — Concurrent execution of tasks
- **Event Handling** — Responding to system events
- **Audio/Visual Capture** — Working with multimedia data
- **Network Information** — Gathering system network details

**Cybersecurity Concepts:**
- **System Monitoring** — Understanding how monitoring tools work
- **Data Collection** — Learning about information gathering
- **Security Awareness** — Understanding potential vulnerabilities
- **Ethical Hacking** — Responsible security testing practices

---

## 🔧 Configuration

**Customizable Settings:**
- Screenshot interval timing
- Audio recording duration
- Log file locations
- Monitoring sensitivity
- Data retention policies

**Advanced Options:**
- Stealth mode configuration
- Custom hotkeys for control
- Selective monitoring features
- Export formats for data

---

## 📊 Output & Analysis

**Generated Files:**
- **Detailed logs** with timestamps
- **System information** reports
- **Visual evidence** through screenshots
- **Audio recordings** for analysis
- **Network configuration** details

**Analysis Features:**
- Structured data organization
- Timestamp correlation
- Pattern identification
- Security assessment reporting

---

## 🛡️ Security Considerations

**Best Practices:**
- **Secure Storage** — Encrypt sensitive data
- **Access Control** — Limit file permissions
- **Data Retention** — Delete logs after analysis
- **Network Security** — Secure data transmission
- **Audit Trail** — Maintain testing records

**Privacy Protection:**
- **Data Minimization** — Collect only necessary information
- **Consent Management** — Document all permissions
- **Secure Deletion** — Properly remove sensitive data
- **Compliance** — Follow data protection regulations

---

## ⚖️ Ethical Guidelines

**Responsible Use:**
- **Authorization First** — Always get written permission
- **Transparency** — Inform users about monitoring
- **Purpose Limitation** — Use only for stated educational goals
- **Data Protection** — Secure all collected information
- **Legal Compliance** — Follow all applicable laws

**Prohibited Uses:**
- ❌ Unauthorized surveillance
- ❌ Malicious data collection
- ❌ Privacy violations
- ❌ Commercial exploitation
- ❌ Harassment or stalking

---

## 📚 Learning Resources

**Related Topics:**
- Cybersecurity fundamentals
- Ethical hacking methodologies
- System administration
- Privacy and data protection
- Digital forensics

**Recommended Reading:**
- Python security programming
- Windows API documentation
- Cybersecurity best practices
- Legal aspects of security testing

---

## 🤝 Contributing

Contributions for educational improvements are welcome! Please ensure all contributions maintain the educational focus and ethical guidelines.

**Guidelines:**
- Focus on educational value
- Maintain security best practices
- Include comprehensive documentation
- Follow ethical coding standards

---

## 📝 Notes

- **Administrative privileges** may be required for some features
- **Antivirus software** may flag the program (expected behavior)
- **Performance impact** varies based on monitoring intensity
- **Data size** can grow quickly with continuous monitoring

---

## 📄 License

> **For educational use only. Not for commercial or malicious use.**
>
> This project is provided for educational purposes under the understanding that:
> - Users will act responsibly and ethically
> - All applicable laws and regulations will be followed
> - Proper consent and authorization will be obtained
> - The software will not be used for malicious purposes

---

## 📧 Contact
**Soumit Santra**  
For educational questions, suggestions, or collaboration opportunities.

---

## 🚨 Final Reminder

> **The author is not responsible for any misuse of this software.**
>
> **Remember: With great power comes great responsibility. Use this tool ethically and legally.**
>
> **This tool is meant to educate about cybersecurity concepts, not to enable malicious activities.**

---

*Stay ethical, stay legal, keep learning! 🛡️📚*
