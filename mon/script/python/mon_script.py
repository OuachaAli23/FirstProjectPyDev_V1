'''
Created on 15 oct. 2023

@author: Dell
'''

class Auteur:
    def __init__ (self, nom):
        self.nom = nom

class Livre:
    def __init__ (self, titre, auteur):
        self.titre = titre
        self.auteur = auteur


    
class Bibliotheque:
    def __init__ (self):
        self.collection = []

    def emprunter_livre(self, livre):
        if livre in self.collection:
            self.collection.remove(livre)
            return f"{Livre.titre} aewemprunte"
        else:
            return "Le livre n'est pas disonnible"


auteurl = Auteur("J.K. Rowling")
livrel = Livre("Harry Potter and the Sorcerer's Stone", auteurl)
bibliotheque = Bibliotheque()

resultat = bibliotheque.emprunter_livre(livrel)

print(resultat)


