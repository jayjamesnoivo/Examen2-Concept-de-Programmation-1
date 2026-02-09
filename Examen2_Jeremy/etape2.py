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


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, immatriculation, nombre_portes):
        super().__init__(marque, modele, annee, immatriculation)
        self.nombre_portes = nombre_portes

    def se_decrire(self):
        return super().se_decrire() + f" | Portes: {self.nombre_portes}"


class Camion(Vehicule):
    def __init__(self, marque, modele, annee, immatriculation, charge_utile):
        super().__init__(marque, modele, annee, immatriculation)
        self.charge_utile = charge_utile

    def se_decrire(self):
        return super().se_decrire() + f" | Charge utile: {self.charge_utile}t"

    def demarrer(self):
        print(f"Le camion {self.immatriculation} démarre avec un grondement.")


# À tester :
if __name__ == "__main__":
    v = Voiture("Peugeot", "308", 2021, "EF-456-GH", 5)
    c = Camion("Volvo", "FH16", 2019, "XX-999-YY", 19)

    print(v.se_decrire())
    print(c.se_decrire())
    c.demarrer()
