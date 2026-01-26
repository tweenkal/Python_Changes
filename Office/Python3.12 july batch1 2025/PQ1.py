class Person:
    def __init__(self, name, age, gender, mob_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.mob_number = mob_number


class Doctor(Person):
    def __init__(self, name, age, gender, mob_number, Specialization):
        super().__init__(name, age, gender, mob_number)
        self.Specialization = Specialization

    def display(self):
        print(
            f"Name:{self.name} age:{self.age} gender:{self.gender} mob_number:{self.mob_number} Specialization:{self.Specialization}")


class Patient(Person):
    def __init__(self, name, age, gender, mob_number, patient_id):
        super().__init__(name, age, gender, mob_number)
        self.patient_id = patient_id
        self.medical_history = []

    def display(self):
        print(
            f"Name:{self.name} age:{self.age} gender:{self.gender} mob_number:{self.mob_number} patient_id:{self.patient_id}")


class MedicalRecord:
    def __init__(self, diagnosis, treatment, date):
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.date = date

    def display(self):
        print(
            f"Diagnosis​:{self.diagnosis} Treatment​:{self.treatment} Date:{self.date}")


class HospitalManagementSystem:
    def __init__(self):
        self.doctors = []
        self.patients = []

    def validate_mobile_number(self, mobile):
        """Validate that the mobile number is exactly 10 digits."""
        if mobile.isdigit() and len(mobile) == 10:
            return True
        return False

    def add_doctor(self):
        name = input("Enter doctor name=")
        age = int(input("Enter age="))
        gender = input("Enter gender=")
        while True:
            mob_number = input("Enter mobile number=")
            if self.validate_mobile_number(mob_number):
                break
            print("Invalid mobile number! Must be 10 digits.")
        specialization = input("Enter specialization=")
        self.doctors.append(
            Doctor(name, age, gender, mob_number, specialization))
        print("\n Added doctor successfully")

    def view_doctor(self):
        print("\n---Doctor Details---")
        if not self.doctors:
            print("Doctor not found")
        for doctor in self.doctors:
            doctor.display()
        print()

    def update_doctor(self):
        mobile = input("Enter doctor mobile number to update=")
        for doctor in self.doctors:
            if doctor.mob_number == mobile:
                doctor.name = input("Enter new doctor name=")
                doctor.age = int(input("Enter new age="))
                doctor.gender = input("Enter new gender=")
                while True:
                    doctor.Specialization = input("Enter new specialization=")
                    if doctor.Specialization:
                        break
                print("\nDoctor updated successfully")
                return
        print("\n Doctor not found")

    def delete_doctor(self):
        mobile = input("Enter doctor mobile number to delete=")
        for doctor in self.doctors:
            if doctor.mob_number == mobile:
                self.doctors.remove(doctor)
                print("\n Doctor delete successfully")
                return
        print("\n Doctor not found")

    def add_patient(self):
        name = input("Enter patient name: ")
        age = int(input("Enter age: "))
        gender = input("Enter gender: ")
        while True:
            mobile = input("Enter mobile number: ")
            if self.validate_mobile_number(mobile):
                break
            print("Invalid mobile number! Must be 10 digits.")

        patient_id = input("Enter patient ID: ")
        self.patients.append(Patient(name, age, gender, mobile, patient_id))
        print("Patient added successfully!\n")

    def view_patient(self):
        print("\n----Patient Details-----")
        if not self.patients:
            print("patient not found")
        for patient in self.patients:
            patient.display()
        print()

    def update_patient(self):
        mobile = input("Enter patient mobile number to update=")
        for patient in self.patients:
            if patient.mob_number == mobile:
                patient.name = input("Enter new patient name=")
                patient.age = int(input("Enter new age="))  # Fixed conversion
                patient.gender = input("Enter new gender=")
                patient.patient_id = input("Enter new patient id=")
                print("Patient updated successfully")  # Fixed message
                return
        print("\n Patient not found")

    def delete_patient(self):
        mobile = input("Enter patient mobile number to delete=")
        for patient in self.patients:
            if patient.mob_number == mobile:
                self.patients.remove(patient)
                print("\n patient delete successfully")
                return
        print("\n Patient not found")

    def add_medical_records(self):
        mobile = input("Enter patient mobile number=")
        for patient in self.patients:
            if patient.mob_number == mobile:
                diagnosis = input("Enter diagnosis=")
                treatment = input("Enter treatment=")
                date = input("Enter date (YYYY-MM-DD)=")
                patient.medical_history.append(
                    MedicalRecord(diagnosis, treatment, date))
                print("Medical record added successfully")
                return
        print("\n Patient not found")

    def view_medical_history(self):
        mobile = input("Enter patient mobile number=")
        for patient in self.patients:
            if patient.mob_number == mobile:
                print(f"\n--- Medical History for {patient.name} ---")
                if not patient.medical_history:
                    print("No medical records found.")
                for record in patient.medical_history:
                    record.display()
                print()
                return
        print("Patient not found!\n")


# ---------------Main Menu---------------------
hospital = HospitalManagementSystem()

while True:
    print("\n ----------Hospital Management System------------------")
    print("1.Add Doctor")
    print("2.View Doctor")
    print("3.Update Doctor")
    print("4.Delete Doctor")
    print("5.Add Patient")
    print("6.View Patient")
    print("7.Update Patient")
    print("8.Delete Patient")
    print("9.Add Medical Record")
    print("10.View Medical History")

    choice = input("\n Enter choice=")

    if choice == "1":
        hospital.add_doctor()
    elif choice == "2":
        hospital.view_doctor()
    elif choice == "3":
        hospital.update_doctor()
    elif choice == "4":
        hospital.delete_doctor()
    elif choice == "5":
        hospital.add_patient()
    elif choice == "6":
        hospital.view_patient()
    elif choice == "7":
        hospital.update_patient()
    elif choice == "8":
        hospital.delete_patient()
    elif choice == "9":
        hospital.add_medical_records()
    elif choice == "10":
        hospital.view_medical_history()
    elif choice == "0":
        print("Exiting system...")
        break
    else:
        print("Invalid choice. Try again!\n")