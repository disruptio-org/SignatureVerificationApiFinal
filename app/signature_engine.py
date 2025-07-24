import win32com.client


class SignatureEngineWrapper:
    def __init__(self):
        try:
            self.engine = win32com.client.Dispatch("WacomGSS.SignatureEngine")
        except Exception as e:
            raise RuntimeError(f"Failed to load Wacom SignatureEngine COM object: {e}")

    def create_template(self, config_options=None):
        """
        Creates a new signature template for enrollment.
        """
        try:
            template = self.engine.CreateTemplate(config_options)
            return template
        except Exception as e:
            raise RuntimeError(f"Error creating template: {e}")

    def get_template_status(self, template_blob):
        """
        Returns enrollment status of the current template.
        """
        try:
            status = self.engine.GetTemplateStatus(template_blob)
            return {
                "isComplete": status.IsEnrollmentComplete,
                "requiredSamples": status.RequiredSamples,
                "currentSamples": status.CurrentSamples
            }
        except Exception as e:
            raise RuntimeError(f"Error getting template status: {e}")

    def enroll_signature(self, template_blob, signature_blob):
        """
        Adds a signature sample to the template (during enrollment).
        Returns the updated template and status.
        """
        try:
            result = self.engine.EnrollSignature(template_blob, signature_blob)
            return {
                "updatedTemplate": result.UpdatedTemplate,
                "isEnrollmentComplete": result.IsEnrollmentComplete,
                "requiredSamples": result.RequiredSamples,
                "currentSamples": result.CurrentSamples
            }
        except Exception as e:
            raise RuntimeError(f"Error enrolling signature: {e}")

    def verify_signature(self, template_blob, signature_blob):
        """
        Verifies a signature against a template and returns result dict.
        """
        try:
            result = self.engine.VerifySignature(template_blob, signature_blob)
            return {
                "score": result.Score,
                "isAccepted": result.IsAccepted,
                "updatedTemplate": result.UpdatedTemplate
            }
        except Exception as e:
            raise RuntimeError(f"Error verifying signature: {e}")
