class Vehicule:
    _vehicules_crees = []

    def __init__(self, marque, modele, annee, immatriculation):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.immatriculation = immatriculation
        self.__en_marche = False
        Vehicule._vehicules_crees.append(self)

    def se_decrire(self):
        return f"{self.marque} {self.modele} ({self.annee}), immat. {self.immatriculation}"

    def demarrer(self):
        if not self.__en_marche:
            self.__en_marche = True
            print(f"Le véhicule {self.immatriculation} démarre.")
        else:
            print(f"Le véhicule {self.immatriculation} est déjà en marche.")

    def arreter(self):
        if self.__en_marche:
            self.__en_marche = False
            print(f"Le véhicule {self.immatriculation} s'arrête.")
        else:
            print(f"Le véhicule {self.immatriculation} est déjà à l'arrêt.")

    @classmethod
    def afficher_flotte(cls):
        for v in cls._vehicules_crees:
            etat = "en marche" if v._Vehicule__en_marche else "à l'arrêt"
            print(f"{v.immatriculation} : {etat}")

    @staticmethod
    def verifier_immatriculation(immat):
        return "-" in immat


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
        if not self._Vehicule__en_marche:
            self._Vehicule__en_marche = True
            print(f"Le camion {self.immatriculation} démarre avec un grondement.")
        else:
            print(f"Le véhicule {self.immatriculation} est déjà en marche.")


# À tester :
if __name__ == "__main__":
    v1 = Voiture("Peugeot", "308", 2021, "EF-456-GH", 5)
    v2 = Camion("Renault", "T", 2020, "ZZ-TOP-01", 15)
    v1.demarrer()
    Vehicule.afficher_flotte()
    print(Vehicule.verifier_immatriculation("123456"))  # False
