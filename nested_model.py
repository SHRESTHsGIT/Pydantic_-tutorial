from pydantic import BaseModel
# when we use one model as field in another model we call it nested model
class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'gender': 'male', 'age': 35, 'address': address1}
print(patient_dict)# output- {'name': 'nitish', 'gender','
patient1 = Patient(**patient_dict)

temp = patient1.model_dump()
print(temp)
# output-{name: 'nitish..}
print(type(temp))
#output- <class 'dict'>
# model_dump() converts the model to a dictionary

#for json we can use model_dump_json()
temp2= patient1.model_dump_json()
print(temp2)
# output- {"name": "nit

temp3=patient1.model_dump_json(include={'name', 'address'})
#now only these 2 fields will be included in the output
print(temp3)
# output- {"name": "nitish", "address": {"city": "gurgaon", "state": "haryana", "pin": "122001"}}


temp4=patient1.model_dump(exclude={'address':['state']})
#now state will be excluded from the output

#other important parameter like - exclude_unset- used for ...



# benefits of using nested models:
# Better organization of related data (e.g., vitals, address, insurance)

# Reusability: Use Vitals in multiple models (e.g., Patient, MedicalRecord)

# Readability: Easier for developers and API consumers to understand

# Validation: Nested models are validated automatically—no extra work needed