from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# Define a Patient model using Pydantic for validation
class Patient(BaseModel):

    # We can use Annotated to add metadata to the field.
    # This field must be a string of max length 50. It also includes title, description, and example metadata.
    name: Annotated[
        str, 
        Field(
            max_length=50, 
            title='Name of the patient', 
            description='Give the name of the patient in less than 50 chars', 
            examples=['Nitish', 'Amit']
        )
    ]

    # Validates that the input is a properly formatted email address
    email: EmailStr

    # Validates that the input is a valid URL (e.g., LinkedIn profile URL)
    linkedin_url: AnyUrl

    # Age must be an integer between 1 and 119 (exclusive bounds)
    age: int = Field(gt=0, lt=120)

    # Weight must be a float greater than 0.
    # 'strict=True' ensures only float values are accepted (not int or str).
    weight: Annotated[float, Field(gt=0, strict=True)]

    # Boolean field with default None. Describes if the patient is married or not.
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]

    # Optional list of strings. Max length = 5 items in the list.
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]

    # Dictionary of contact details.
    # If we write just dict, then it will accept any key and value types.
    # But if we want to restrict the types, we can use Dict[str, str] or Dict[int, str], etc.
    contact_details: Dict[str, str]

# Basic method to show how to use Pydantic models
# class patient(BaseModel):
#     name: str
#     age: int
#     allergies: Optional[List[str]] = None
#     married: bool = False

# patient_info = {'name':'nitish', 'age':'30'}
# patient1 = patient(**patient_info)  # Unpacking the dict using **patient_info
# This will create an object of Pydantic model class 'Patient' and store it in patient1

# Function to simulate updating or viewing patient data
def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

# Dictionary of patient information (simulating user input or API request body)
patient_info = {
    'name': 'nitish', 
    'email': 'abc@gmail.com', 
    'linkedin_url': 'http://linkedin.com/1322', 
    'age': '30',  # If '30' is a string, Pydantic will try to convert it to int. If it fails, it raises an error.
    'weight': 75.2,  # If 75.2 is a string, it will raise error because we have used strict=True in weight field
    'contact_details': {'phone': '2353462'}
}

# Create a validated Patient object by unpacking the dict
patient1 = Patient(**patient_info)

# Pass the patient object to the function
update_patient_data(patient1)
