# ⚠️ WARNING: EDUCATIONAL PURPOSE ONLY
<!--
Copyright (c) 2024 [Soumit Santra]. All rights reserved.
-->

This keylogger is designed **STRICTLY FOR EDUCATIONAL PURPOSES**. Creating or using keyloggers for unauthorized monitoring is illegal and unethical. You could face serious legal consequences if used without explicit permission.

## Legal Disclaimer

- Using this software to monitor someone without their consent is **ILLEGAL**
- The author takes NO responsibility and/or liability for how you choose to use this tool
- By using this software, you agree to use it only for educational purposes on systems you own or have permission to test

## Description

This is an intermediate-level keylogger implementation in Python that demonstrates various system monitoring capabilities:

- Keyboard input logging
- Screenshot capture
- Audio recording
- Clipboard monitoring
- System information collection
- WiFi password extraction

## Requirements

- Python 3.x
- Windows OS
- Required packages will be automatically installed:
  - pynput
  - requests
  - pywin32
  - sounddevice
  - scipy
  - Pillow

## Usage

1. Run only on systems you own or have explicit permission to test
2. Execute the script:
   ```
   python keylogger.py
   ```
3. The script will create an "information" directory containing:
   - key_log.txt (keyboard inputs)
   - system_info.txt (system details)
   - wifi_pass.txt (saved WiFi credentials)
   - clipboard.txt (clipboard content)
   - screenshots/ (screen captures)
   - audio/ (sound recordings)

## Ethical Considerations

- Always obtain written permission before testing
- Never use for malicious purposes
- Keep logs secure and delete after testing
- Respect privacy and data protection laws

## Educational Value

This code demonstrates:
- Python file operations
- System interaction
- Multi-threading
- Event handling
- Audio/visual capture
- Network information gathering

## License

For educational use only. Not for commercial or malicious use.

**I am not responsible for any malicious use of this software.**

This project is open-sourced software licensed under the **MIT license**.
