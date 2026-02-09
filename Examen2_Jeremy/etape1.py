class Vehicule:
    def __init__(self, marque, modele, annee, immatriculation):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.immatriculation = immatriculation

    def se_decrire(self):
        return f"{self.marque} {self.modele} ({self.annee}), immat. {self.immatriculation}"

    def demarrer(self):
        print(f"Le véhicule {self.immatriculation} démarre.")


# À tester :
if __name__ == "__main__":
    v = Vehicule("Renault", "Clio", 2020, "AB-123-CD")
    print(v.se_decrire())
    v.demarrer()
