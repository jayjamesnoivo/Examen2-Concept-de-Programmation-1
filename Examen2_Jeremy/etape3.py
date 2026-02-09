class Vehicule:
    def __init__(self, marque, modele, annee, immatriculation):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.immatriculation = immatriculation
        self.__en_marche = False  # privé

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
        # On respecte la logique de Vehicule avec l'attribut privé
        if not self._Vehicule__en_marche:
            self._Vehicule__en_marche = True
            print(f"Le camion {self.immatriculation} démarre avec un grondement.")
        else:
            print(f"Le véhicule {self.immatriculation} est déjà en marche.")


# À tester :
if __name__ == "__main__":
    c = Camion("Volvo", "FH16", 2019, "XX-999-YY", 19)
    c.demarrer()  # camion démarre
    c.demarrer()  # déjà en marche (message Vehicule)
    c.arreter()
    c.demarrer()  # camion démarre à nouveau
