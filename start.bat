@echo off
echo Starting Signature Verification API on port 10000...
uvicorn app.main:app --host 0.0.0.0 --port 10000
pause


