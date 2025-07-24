class EnrollmentRequest(BaseModel):
    template: str
    signature: str

class EnrollmentResponse(BaseModel):
    updatedTemplate: str
    isEnrollmentComplete: bool
    requiredSamples: int
    currentSamples: int

class TemplateStatusResponse(BaseModel):
    isEnrollmentComplete: bool
    requiredSamples: int
    currentSamples: int
