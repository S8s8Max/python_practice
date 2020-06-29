class Human:
    def __init__(self, name):
        self.name = name
        
class Patient(Human):
    def __init__(self, name, patient_id, symptom):
        super().__init__(name)
    
        self.symptom = symptom
        self.patient_id = patient_id
    
class Clinic:
    def __init__(self):
        self.patient_list = []
        
    
    def show_waiting_counts(self):
        print(f"現在、{len(self.patient_list)}人待ちです。")
        
    
    def reserve(self, patient):
        if self._check_reserved(patient):
            print(f'{patient.name}さんはすでに予約済みです。')
        else:
            self.patient_list.append(patient)
            print(f'{patient.name}さんの予約が完了しました。')
            
    
    def diagnosis(self, patient_id=None):
        patient = None
        if patient_id == None:
            if len(self.patient_list) > 0:
                patient = self.patient_list[0]
                self.patient_list.remove(self.patient_list[0])
        else:
            for p in self.patient_list:
                if p.patient_id == patient_id:
                    patient = p
        
        if patient == None:
            print("診察する患者がいません。")
        else:
            print(f"{patient.name}さんは{patient.symptom}です。")
            
            print(f"診察が終わりました。")
            
        
    def _check_reserved(self, patient):
        for p in self.patient_list:
            if patient.patient_id == p.patient_id:
                return True
        return False

if __name__ == "__main__":
    myclinic = Clinic()

    patients = [["佐藤", "111", "咳"],
                ["田中", "222", "腹痛"],
                ["鈴木", "333", "鼻水"],
                ["山田", "444", "倦怠感"],
                ["中田", "555", "インフル"],]

    for p in patients:
        patient = Patient(p[0], p[1], p[2])
    
        myclinic.reserve(patient)

        myclinic.show_waiting_counts()

    me = Patient("中田", "555", "インフル")
    myclinic.reserve(me)
    myclinic.show_waiting_counts()