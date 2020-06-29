from oop_practice import Clinic, Patient

if __name__ == "__main__":

    new_clinic = Clinic()

    new_patients = [["Sam", "0001", "asthma"],
                    ["Kate", "0002", "diabetes"],
                    ["Drake", "0003", "injury"],
                    ["Sara", "0004", "abortion"],]
    
    for p in new_patients:
        patient = Patient(p[0], p[1], p[2])

        new_clinic.reserve(patient)

    new_clinic.show_waiting_counts()

    count = len(new_clinic.patient_list)

    while count >= 0:
        new_clinic.diagnosis(patient_id=None)
        count -= 1

