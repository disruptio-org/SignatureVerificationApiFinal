# Wacom Signature Verification API

A FastAPI-based REST API that wraps the Wacom Ink SDK for Verification (COM-based) to allow biometric signature enrollment and verification via HTTP.

---

## 🚀 Features

- Create and manage signature templates
- Enroll new users by submitting dynamic signature samples (FSS)
- Verify signatures against stored templates
- Returns match score, accept/reject flags, and updated templates

---

## 📦 Requirements

- Windows 10/11
- Python 3.10+
- Wacom Ink SDK for Verification installed and licensed
- `SignatureEngine.dll` registered via `regsvr32`

---

## 📁 Project Structure

