from fastapi import FastAPI, HTTPException
from app.signature_engine import SignatureEngineWrapper
from app.models import (
    SignatureVerificationRequest,
    SignatureVerificationResponse,
    EnrollmentRequest,
    EnrollmentResponse,
    TemplateStatusResponse
)

app = FastAPI(
    title="Wacom Signature Verification API",
    description="API to verify and enroll signatures using Wacom Ink SDK for Verification",
    version="1.0.0"
)

engine = SignatureEngineWrapper()

@app.get("/status")
def read_status():
    return {"status": "running", "message": "Signature Verification API is live"}

# Verification endpoint
@app.post("/verify", response_model=SignatureVerificationResponse)
def verify_signature(request: SignatureVerificationRequest):
    try:
        result = engine.verify_signature(request.template, request.signature)
        return SignatureVerificationResponse(
            score=result["score"],
            isAccepted=result["isAccepted"],
            updatedTemplate=result["updatedTemplate"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Create a new empty template
@app.post("/enroll/start")
def create_template():
    try:
        template = engine.create_template()
        return {"template": template}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Add a new signature to an existing template (enrollment phase)
@app.post("/enroll/add", response_model=EnrollmentResponse)
def enroll_signature(request: EnrollmentRequest):
    try:
        result = engine.enroll_signature(request.template, request.signature)
        return EnrollmentResponse(
            updatedTemplate=result["updatedTemplate"],
            isEnrollmentComplete=result["isEnrollmentComplete"],
            requiredSamples=result["requiredSamples"],
            currentSamples=result["currentSamples"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Check enrollment progress
@app.post("/enroll/status", response_model=TemplateStatusResponse)
def check_status(request: EnrollmentRequest):
    try:
        status = engine.get_template_status(request.template)
        return TemplateStatusResponse(
            isEnrollmentComplete=status["isComplete"],
            requiredSamples=status["requiredSamples"],
            currentSamples=status["currentSamples"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
