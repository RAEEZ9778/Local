print("Hospital Appointment Booking System!")\

def reg_patient():
    print("Registering a new patient...")
    print("Please enter patient details:")
    print("Name: ")
    name = input()
    print("Age: ")
    age = int(input())
    print("Contact Number: ")
    contact = input()
    print("Patient registered successfully!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print("Login Successfull")