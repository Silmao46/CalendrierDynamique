"""Calendrier dynamique"""
from datetime import datetime
import numpy as np


class Calendrier:
    """Calendrier dynamique"""
    
    def __init__(self, evenements=None):
        if evenements is None:
            self.evenements = np.array([[], [], [], [], []]) # Format : [date de début, date de fin, propriétaire, description, ID]
        else:
            self.evenements = np.array(evenements)

    def ajouter_evenement(self, date_debut: datetime, date_fin:datetime, proprietaire: str, description: str):
        """Ajouter un événement au calendrier"""
        ID = np.max(self.evenements[4]) + 1 if self.evenements[4].size > 0 else 0  # ID basé sur l'ID max actuel
        nouvel_evenement = np.array([[date_debut], [date_fin], [proprietaire], [description], [ID]])
        self.evenements = np.concatenate((self.evenements, nouvel_evenement), axis=1)
        return ID # Peut être utile pour l'automatisation d'ajouts/modifications/suppressions

    def suppression_evenement(self, ID: int):
        """Supprimer un événement du calendrier par son ID"""
        try:
            index = np.where(self.evenements[4] == ID)[0][0]  # Trouver l'index de l'événement avec l'ID donné
            self.evenements = np.delete(self.evenements, index, axis=1)
        except IndexError:
            print("ID inexistant. Aucun événement supprimé.")
    
    def deplacer_evenement(self, ID: int, nouvelle_date: datetime):
        """Déplacer un événement à une nouvelle date"""
        try:
            index = np.where(self.evenements[4] == ID)[0][0]  # Trouver l'index de l'événement avec l'ID donné
            duree = self.evenements[1, index] - self.evenements[0, index]  # Calculer la durée de l'événement
            self.evenements[0, index] = nouvelle_date
            self.evenements[1, index] = nouvelle_date + duree  # Mettre à jour la date de fin également
        except IndexError:
            print("ID inexistant. Aucun événement déplacé.")

    def calendrier_proprietaire(self, proprietaire: str):
        """Retourne les événements d'un propriétaire"""
        try:
            if not np.any(self.evenements[2] == proprietaire):
                raise IndexError("Propriétaire inexistant. Aucun événement trouvé.")
            calendrier_propriétaire = Calendrier([self.evenements[0, self.evenements[2] == proprietaire],
                           self.evenements[1, self.evenements[2] == proprietaire],
                           self.evenements[2, self.evenements[2] == proprietaire],
                           self.evenements[3, self.evenements[2] == proprietaire],
                           self.evenements[4, self.evenements[2] == proprietaire]])
            return calendrier_propriétaire
        except IndexError as e:
            print(f"Erreur : {e}")
    
    def modifier_fin_evenement(self, ID: int, nouvelle_date_fin: datetime):
        """Modifier la date de fin d'un événement"""
        try:
            if nouvelle_date_fin < self.evenements[0, np.where(self.evenements[4] == ID)[0][0]]:
                raise ValueError("La nouvelle date de fin ne peut pas être antérieure à la date de début.")
            index = np.where(self.evenements[4] == ID)[0][0]  # Trouver l'index de l'événement avec l'ID donné
            self.evenements[1, index] = nouvelle_date_fin
        except IndexError as e:
            print(f"Erreur : {e}")
        except ValueError as e:
            print(f"Erreur : {e}")
    
    def modifier_description_evenement(self, ID: int, nouvelle_description: str):
        """Modifier la description d'un événement"""
        try:
            index = np.where(self.evenements[4] == ID)[0][0]  # Trouver l'index de l'événement avec l'ID donné
            self.evenements[3, index] = nouvelle_description
        except IndexError as e:
            print(f"Erreur : {e}")
    
    def modifier_proprietaire_evenement(self, ID: int, nouveau_proprietaire: str):
        """Modifier le propriétaire d'un événement"""
        try:
            index = np.where(self.evenements[4] == ID)[0][0]  # Trouver l'index de l'événement avec l'ID donné
            self.evenements[2, index] = nouveau_proprietaire
        except IndexError:
            print("ID inexistant. Aucun événement modifié.")

    def __str__(self):
        """Méthode pour print les événements du calendrier"""
        result = "Calendrier:\n"
        for i in range(self.evenements.shape[1]):
            date_debut = self.evenements[0, i]
            date_fin = self.evenements[1, i]
            proprietaire = self.evenements[2, i]
            description = self.evenements[3, i]
            ID = self.evenements[4, i]
            result += f"{ID}: {date_debut} à {date_fin} - {proprietaire} - {description}\n"
        return result