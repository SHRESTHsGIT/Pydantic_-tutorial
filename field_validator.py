from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    #if we want data validation on 2 fiels we cant use field_validator decorator we have to use model validator 
    @field_validator('email')# a new method to validate email with decorator field_validator in brackets we can pass the field name to validate
    @classmethod#to show this is a class method
    def email_validator(cls, value):# our custom validation method

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1] # split the email by '@' and take the last part as domain name it divide in 2 parts last part is after '@'
        # ['abc', 'gmail.com']
        # ['gmail.com']
        # ['icici.com']

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    #field_validator different modes before and after
    # before: runs before the field is validated, useful for transforming data
    # after: runs after the field is validated, useful for additional validation-> get value after type cursion and other validations
    # e.g. if we want to validate age after it has been converted to int
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '30', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1)