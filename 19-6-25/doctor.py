# Hospital Management System - Beginner Level
# Using Object-Oriented Programming with Getters

class Person:
    """Base class for both doctors and patients"""
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    # Getter methods
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_gender(self):
        return self.gender
    
    def get_personal_details(self):
        """Return formatted personal details"""
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Patient(Person):
    """Patient class that inherits from Person"""
    
    def __init__(self, name, age, gender, disease_info):
        super().__init__(name, age, gender)  # Call parent class constructor
        self.disease_info = disease_info
    
    # Getter method for disease information
    def get_disease_info(self):
        return self.disease_info
    
    def get_full_patient_details(self):
        """Return full patient details including disease information"""
        personal_details = self.get_personal_details()
        return f"{personal_details}, Disease: {self.disease_info}"


class Doctor(Person):
    """Doctor class that inherits from Person"""
    
    def __init__(self, name, age, gender, specialization):
        super().__init__(name, age, gender)  # Call parent class constructor
        self.specialization = specialization
        self.assigned_patients = []  # Private list to store assigned patients
    
    # Getter methods
    def get_specialization(self):
        return self.specialization
    
    def get_assigned_patients(self):
        """Return list of assigned patients"""
        return self.assigned_patients.copy()  # Return a copy to protect the original list
    
    def get_doctor_details(self):
        """Return full doctor details"""
        personal_details = self.get_personal_details()
        return f"{personal_details}, Specialization: {self.specialization}"
    
    # Methods to manage patients
    def assign_patient(self, patient):
        """Assign a patient to this doctor"""
        if isinstance(patient, Patient):  # Check if the input is a Patient object
            self.assigned_patients.append(patient)
            print(f"Patient {patient.get_name()} assigned to Dr. {self.get_name()}")
        else:
            print("Error: Only Patient objects can be assigned")
    
    def remove_patient(self, patient_name):
        """Remove a patient from assigned list"""
        for patient in self.assigned_patients:
            if patient.get_name() == patient_name:
                self.assigned_patients.remove(patient)
                print(f"Patient {patient_name} removed from Dr. {self.get_name()}'s list")
                return
        print(f"Patient {patient_name} not found in Dr. {self.get_name()}'s list")
    
    def list_assigned_patients(self):
        """Display all assigned patients"""
        if not self.assigned_patients:
            print(f"Dr. {self.get_name()} has no assigned patients")
        else:
            print(f"Dr. {self.get_name()}'s assigned patients:")
            for i, patient in enumerate(self.assigned_patients, 1):
                print(f"{i}. {patient.get_full_patient_details()}")


# Example usage and testing
if __name__ == "__main__":
    print("=== Hospital Management System Demo ===\n")
    
    # Create some patients
    patient1 = Patient("John Smith", 45, "Male", "Diabetes")
    patient2 = Patient("Sarah Johnson", 32, "Female", "Hypertension")
    patient3 = Patient("Mike Brown", 28, "Male", "Broken Arm")
    
    # Create some doctors
    doctor1 = Doctor("Dr. Emily Davis", 38, "Female", "Cardiology")
    doctor2 = Doctor("Dr. Robert Wilson", 42, "Male", "Orthopedics")
    
    # Display personal details using getter methods
    print("=== Patient Information ===")
    print(f"Patient 1: {patient1.get_full_patient_details()}")
    print(f"Patient 2: {patient2.get_full_patient_details()}")
    print(f"Patient 3: {patient3.get_full_patient_details()}")
    
    print("\n=== Doctor Information ===")
    print(f"Doctor 1: {doctor1.get_doctor_details()}")
    print(f"Doctor 2: {doctor2.get_doctor_details()}")
    
    print("\n=== Assigning Patients to Doctors ===")
    # Assign patients to doctors
    doctor1.assign_patient(patient1)  # Diabetes patient to Cardiologist
    doctor1.assign_patient(patient2)  # Hypertension patient to Cardiologist
    doctor2.assign_patient(patient3)  # Broken arm patient to Orthopedist
    
    print("\n=== Listing Assigned Patients ===")
    doctor1.list_assigned_patients()
    print()
    doctor2.list_assigned_patients()
    
    print("\n=== Using Getter Methods ===")
    print(f"Doctor 1 name: {doctor1.get_name()}")
    print(f"Doctor 1 specialization: {doctor1.get_specialization()}")
    print(f"Number of patients assigned to Dr. {doctor1.get_name()}: {len(doctor1.get_assigned_patients())}")
    
    print(f"\nPatient 1 name: {patient1.get_name()}")
    print(f"Patient 1 disease: {patient1.get_disease_info()}")
    
    print("\n=== Removing a Patient ===")
    doctor1.remove_patient("John Smith")
    doctor1.list_assigned_patients()