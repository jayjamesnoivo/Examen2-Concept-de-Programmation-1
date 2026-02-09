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
    def afficher_flotte(cls, flotte=None):
        # Si flotte est fournie, on n'affiche que ses véhicules.
        if flotte is None:
            liste = cls._vehicules_crees
        else:
            liste = flotte._vehicules

        for v in liste:
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


class Flotte:
    def __init__(self, nom):
        self.nom = nom
        self._vehicules = []

    def ajouter_vehicule(self, vehicule):
        self._vehicules.append(vehicule)

    def generer_rapport(self):
        print(f"=== Rapport de la flotte: {self.nom} ===")
        print("\n-- Tous les véhicules créés --")
        Vehicule.afficher_flotte()
        print("\n-- Véhicules de cette flotte --")
        Vehicule.afficher_flotte(self)


# À tester :
if __name__ == "__main__":
    # Création des véhicules
    v1 = Voiture("Toyota", "Yaris", 2022, "AA-111-BB", 3)
    v2 = Camion("MAN", "TGX", 2021, "CC-222-DD", 20)
    v3 = Voiture("Fiat", "500", 2023, "EE-333-FF", 3)

    # Création et peuplement des flottes
    flotte_a = Flotte("Livraisons Urbaines")
    flotte_a.ajouter_vehicule(v1)
    flotte_a.ajouter_vehicule(v2)

    flotte_b = Flotte("Service Commercial")
    flotte_b.ajouter_vehicule(v3)

    # Rapports
    print("\n--- Tous les véhicules créés ---")
    Vehicule.afficher_flotte()

    print("\n--- Rapport flotte A ---")
    flotte_a.generer_rapport()

    print("\n--- Rapport flotte B ---")
    flotte_b.generer_rapport()
