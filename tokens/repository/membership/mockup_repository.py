


class mockup_repository:

    def __init__(self):
        self.members=list()

    def find_all(self):
        member=dict()

        member["first_name"]="Benoît"
        member["last_name"]="Chenal"
        member["phone"]="0614236680"
        member["mail"]="benoit.chenal.57@gmail.com"
        member["adresse"]="1, rue de la carrière,Saint-Avold"
        member["zip"]="57500"
        member["authorized_rs"]="Oui"
        member["authorized_web"]="Oui"
        member["authorized_press"]="Oui"
        member["cotisation"]=30
        self.members.append(member)

        member=dict()
        member["first_name"]="Bastien"
        member["last_name"]="Chenal"
        member["phone"]="0614236680"
        member["mail"]="bastienchenal@gmail.com"
        member["adresse"]="1, rue de la carrière,Saint-Avold"
        member["zip"]="57470"
        member["authorized_rs"]="Oui"
        member["authorized_web"]="Oui"
        member["authorized_press"]="Oui"
        member["cotisation"]=30
        self.members.append(member)

        return self.members