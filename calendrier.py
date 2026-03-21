"""Calendrier dynamique"""
from datetime import datetime
import numpy as np


class Calendrier:
    """Calendrier dynamique"""
    
    def __init__(self, evenements=None):
        if evenements is None:
            self.evenements = np.array([[], [], [], []]) # Format : [date, propriétaire, description, ID]
        else:
            self.evenements = np.array(evenements)

    def ajouter_evenement(self, date: datetime, proprietaire: str, description: str):
        """Ajouter un événement au calendrier"""
        ID = np.max(self.evenements[3]) + 1 if self.evenements[3].size > 0 else 0  # ID basé sur l'ID max actuel
        nouvel_evenement = np.array([[date], [proprietaire], [description], [ID]])
        self.evenements = np.concatenate((self.evenements, nouvel_evenement), axis=1)
        return ID # Peut être utile pour l'automatisation d'ajouts/modifications/suppressions

    def suppression_evenement(self, ID: int):
        """Supprimer un événement du calendrier par son ID"""
        try:
            index = np.where(self.evenements[3] == ID)[0][0]  # Trouver l'index de l'événement avec l'ID donné
            self.evenements = np.delete(self.evenements, index, axis=1)
        except IndexError:
            print("Index hors limites. Aucun événement supprimé.")
    
    def deplacer_evenement(self, ID: int, nouvelle_date: datetime):
        """Déplacer un événement à une nouvelle date"""
        try:
            index = np.where(self.evenements[3] == ID)[0][0]  # Trouver l'index de l'événement avec l'ID donné
            self.evenements[0, index] = nouvelle_date
        except IndexError:
            print("Index hors limites. Aucun événement déplacé.")

    def calendrier_proprietaire(self, proprietaire: str):
        """Retourne les événements d'un propriétaire"""
        return Calendrier([self.evenements[0, self.evenements[1] == proprietaire],
                           self.evenements[1, self.evenements[1] == proprietaire],
                           self.evenements[2, self.evenements[1] == proprietaire],
                           self.evenements[3, self.evenements[1] == proprietaire]])

    def __str__(self):
        """Méthode pour print les événements du calendrier"""
        result = "Calendrier:\n"
        for i in range(self.evenements.shape[1]):
            date = self.evenements[0, i]
            proprietaire = self.evenements[1, i]
            description = self.evenements[2, i]
            ID = self.evenements[3, i]
            result += f"{ID}: {date} - {proprietaire} - {description}\n"
        return result