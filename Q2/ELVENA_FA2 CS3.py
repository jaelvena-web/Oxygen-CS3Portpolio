class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85


def main():
    regular_patient = Patient("Juan Dela Cruz", 15000.0)
    senior_patient = SeniorPatient("Maria Santos", 15000.0)
    philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000.0)

    print("Hospital Billing System")
    print("------------------------")

    print(f"Patient Name:   {regular_patient.get_name()}")
    print(f"Original Bill: PHP {regular_patient.get_bill_amount():,.2f}")
    print(f"Final Bill: PHP {regular_patient.calculate_bill():,.2f}\n")

    print(f"Patient Name:   {senior_patient.get_name()}")
    print(f"Original Bill: PHP {senior_patient.get_bill_amount():,.2f}")
    print(f"Final Bill: PHP {senior_patient.calculate_bill():,.2f}\n")

    print(f"Patient Name:   {philhealth_patient.get_name()}")
    print(f"Original Bill: PHP {philhealth_patient.get_bill_amount():,.2f}")
    print(f"Final Bill: PHP {philhealth_patient.calculate_bill():,.2f}")


if __name__ == "__main__":
    main()