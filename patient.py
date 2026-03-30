"""Structure patient"""

import numpy as np
from datetime import datetime, timedelta
from calendrier import Calendrier

# Preset pour les patients [["description"], [temps avant le prochain événement]] x n événements
preset_patient = {
    "parcours type 1" : np.array([[["Rendez-vous préliminaire"], [0]], 
                                 [["Suivi 1"], [timedelta(days=7)]],
                                 [["Suivi 2"], [timedelta(days=7)]]])}

memoire_patient = {} # Dictionnaire pour stocker les parcours des patients, avec le nom du patient comme clé et la structure parallèle comme valeur

def ajout_parcours_patient(calendrier, patient, parcours, memoire_patient):
    """Ajouter un parcours type à un patient dans le calendrier
    Args:
        calendrier (Calendrier): Le calendrier dans lequel ajouter les événements
        patient (str): Le nom du patient
        equipe (str): Le nom de l'équipe responsable du patient
        parcours (str): Le parcours à ajouter, soit un élément de preset_patient transformé avec des dates (selon le modèle de simulation), ou un parcours autre
            Format du parcours : [[date_debut], [date_fin], [proprietaire], [description]] x n événements
    """
    memoire_patient[str(patient)] = np.array([[], [], [], [], []]) # Initialiser un tableau vide pour le patient
    for i in range(parcours.shape[1]-1):
        ID = calendrier.ajouter_evenement(parcours[i, 0][0], parcours[i, 1][0], parcours[i, 2][0], parcours[i, 3][0]) # Ajouter l'événement au calendrier et récupérer l'ID
        memoire_patient[str(patient)] = np.concatenate((memoire_patient[str(patient)], 
                                                        np.array([[parcours[i, 0][0]], [parcours[i, 1][0]], [parcours[i, 2][0]], [parcours[i, 3][0]], [ID]])), axis=1)