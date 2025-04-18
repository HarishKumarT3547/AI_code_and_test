import json
from datetime import datetime

class User:
    def __init__(self, first_name, last_name, email, password, phone, address, city, state, zip_code, country, dob, gender, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone
        self.address = {
            "street": address,
            "city": city,
            "state": state,
            "zip": zip_code,
            "country": country
        }
        self.dob = dob
        self.gender = gender
        self.occupation = occupation
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def validate(self):
        """Validate user data."""
        if len(self.password) < 8:
            return {"error": "Password too short"}
        if len(self.phone) != 10:
            return {"error": "Invalid phone number"}
        return None

    def to_dict(self):
        """Convert user data to a dictionary."""
        return {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
            "password": self.password,
            "phone": self.phone,
            "address": self.address,
            "dob": self.dob,
            "gender": self.gender,
            "occupation": self.occupation,
            "createdAt": self.created_at
        }

def create_user(first_name, last_name, email, password, phone, address, city, state, zip_code, country, dob, gender, occupation):
    user = User(first_name, last_name, email, password, phone, address, city, state, zip_code, country, dob, gender, occupation)
    validation_error = user.validate()
    if validation_error:
        return validation_error
    return user.to_dict()