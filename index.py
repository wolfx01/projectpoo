class personne:
    def __init__(self ,  code  ,  nom ,  prenom):
        self.code = code
        self.nom = nom
        self.prenom = prenom
    def affich(self):
        print(f"{self.code} {self.nom} {self.prenom}   " ,  end="")