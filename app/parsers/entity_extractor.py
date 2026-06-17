"""Entity extraction from resume text"""
import re

class EntityExtractor:

    EMAIL = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    PHONE = r'\+?\d[\d\s\-]{8,}'

    def extract_contact(self, text):

        email = re.search(self.EMAIL, text)
        phone = re.search(self.PHONE, text)

        return {
            "email": email.group() if email else None,
            "phone": phone.group() if phone else None
        }