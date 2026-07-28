# CloudExify Security Final – Aliza Javed

یہ ریپو ایک سیکیورٹی/نیٹ ورک سیکیورٹی فائنل پروجیکٹ کی گائیڈ ہے۔ اس میں دو اہم پروجیکٹس شامل ہیں جو سیکیورٹی کے بنیادی تصورات کو ظاہر کرتے ہیں۔

## Project Overview

یہ repository دو مختلف کاموں پر مبنی ہے:

1. Project 1 – Network Security Analysis
2. Project 2 – Secure Authentication and Cryptography

## Repository Structure

- Final/Project 1 only required docs/
  - pdf Report & other Files/
    - Project (1) Report.pdf: main report for Project 1
    - nmap-output.txt: output from an Nmap scan
    - Wireshark capturing.pcap: network packet capture file

- Final/Project(2)/
  - Project Report & other files/
    - secure_auth.py: simple secure login/registration system using bcrypt
    - password-hash.py: example of hashing a password with bcrypt
    - password-verify.py: password verification example using bcrypt
    - sha256-example.py: demonstration of SHA-256 hashing
    - encryption_example.py: encryption and decryption demo using Fernet
    - users.json: sample user database for the secure authentication script
    - Project (2) Report.pdf: report for Project 2
  - ScreenShots/: screenshots related to the project

## What This Repository Is About

### Project 1: Network Security Analysis
Is project ka focus network security aur reconnaissance par hai. Is mein:
- Nmap scan results ka use kiya gaya hai
- Wireshark capture file di gayi hai
- Report mein network traffic aur security findings ko explain kiya gaya hai

### Project 2: Secure Authentication and Cryptography
Is project ka focus password security aur encryption par hai. Is mein:
- Password hashing ke liye bcrypt aur SHA-256 ka use kiya gaya hai
- Secure authentication system banaya gaya hai
- Fernet encryption ka demo diya gaya hai

## How to Run the Python Files

Python scripts ko run karne ke liye aapko required packages install karni hoti hain:

```bash
pip install bcrypt cryptography
```

Then run files like:

```bash
python secure_auth.py
python password-hash.py
python password-verify.py
python sha256-example.py
python encryption_example.py
```

## Why This Project Matters

Ye repository students ya beginners ko sikha sakti hai:
- basic cybersecurity concepts
- password hashing
- secure authentication design
- encryption/decryption basics
- network analysis using Nmap and Wireshark

## Notes

- Yeh files educational purpose ke liye hain
- In scripts ko production environment mein directly use karne se pehle aur details check karni chahiye
- Agar aap chahen to is repository ko aur behtar format mein bhi present kiya ja sakta hai
