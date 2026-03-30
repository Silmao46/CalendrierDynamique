"""Exemple rudimentaire pour calendrier dynamique"""


from datetime import datetime
import numpy as np
from calendrier import Calendrier
from patient import ajout_parcours_patient

# Initialisation du calendrier

print("Initialisation du calendrier :")
test_calendrier = Calendrier()

# Ajout d'événements
test_calendrier.ajouter_evenement(datetime(2026, 6, 2), datetime(2026, 6, 2, 10, 0), "Equipe 2", "Diagnostic initial")
test_calendrier.ajouter_evenement(datetime(2026, 6, 3), datetime(2026, 6, 3, 10, 0), "Equipe 2", "Rendez-vous de suivi")
test_calendrier.ajouter_evenement(datetime(2026, 6, 2), datetime(2026, 6, 2, 10, 0), "Equipe 1", "Diagnostic initial")

print("Événements ajoutés :")
print(test_calendrier)

# Déplacement d'un événement

test_calendrier.deplacer_evenement(0, datetime(2026, 6, 4))

print("Événement déplacé :")
print(test_calendrier)

# Suppression d'un événement

test_calendrier.suppression_evenement(1)

print("Événement supprimé :")
print(test_calendrier)

# Test de suppression avec un index hors limites

print("Test de suppression avec un index hors limites :")

test_calendrier.suppression_evenement(5)

# Test de rajout d'un événement après suppression

test_calendrier.ajouter_evenement(datetime(2026, 6, 5), datetime(2026, 6, 5, 10, 0), "Equipe 2", "Rendez-vous de suivi 2")

print("Événement ajouté après suppression :")
print(test_calendrier)

# Affichage du calendrier d'un propriétaire spécifique

calendrier_equipe2 = test_calendrier.calendrier_proprietaire("Equipe 2")

print("Calendrier de l'Equipe 2 :")
print(calendrier_equipe2)

# Test de déplacement d'un événement avec un index hors limites

print("Test de déplacement d'un événement avec un index hors limites :")
test_calendrier.deplacer_evenement(5, datetime(2026, 6, 6))

# Test de suppression d'un événement avec un index hors limites

print("Test de suppression d'un événement avec un index hors limites :")
test_calendrier.suppression_evenement(5)

# Test de modification de la date de fin d'un événement avec un index hors limites
print("Test de modification de la date de fin d'un événement avec un index hors limites :")
test_calendrier.modifier_fin_evenement(5, datetime(2026, 6, 7))

# Test de modification de la description d'un événement avec un index hors limites
print("Test de modification de la description d'un événement avec un index hors limites :")
test_calendrier.modifier_description_evenement(5, "Nouvelle description")

# Test de modification du propriétaire d'un événement avec un index hors limites
print("Test de modification du propriétaire d'un événement avec un index hors limites :")
test_calendrier.modifier_proprietaire_evenement(5, "Nouvelle équipe")

# Test de modification de la date de fin d'un événement avec une date de fin antérieure à la date de début
print("Test de modification de la date de fin d'un événement avec une date de fin antérieure à la date de début :")
test_calendrier.modifier_fin_evenement(0, datetime(2026, 6, 1))

# Test de modification de la date de fin d'un événement avec une date de fin valide
print("Test de modification de la date de fin d'un événement avec une date de fin valide :")
test_calendrier.modifier_fin_evenement(0, datetime(2026, 6, 8))

print(test_calendrier)

# Test de modification de la description d'un événement avec une description valide
print("Test de modification de la description d'un événement avec une description valide :")
test_calendrier.modifier_description_evenement(0, "Diagnostic final")
print(test_calendrier)

# Test de modification du propriétaire d'un événement avec un propriétaire valide
print("Test de modification du propriétaire d'un événement avec un propriétaire valide :")
test_calendrier.modifier_proprietaire_evenement(0, "Equipe 3")
print(test_calendrier)

# Test de retour du calendrier d'un propriétaire avec un propriétaire inexistant
print("Test de retour du calendrier d'un propriétaire avec un propriétaire inexistant :")
calendrier_inexistant = test_calendrier.calendrier_proprietaire("Equipe Inexistante")
print(calendrier_inexistant)

# Test d'ajout d'un parcours type à un patient dans le calendrier
memoire_patient = {}

parcours = np.array([[[datetime(2026, 6, 1)], [datetime(2026, 6, 1, 10, 0)], ["Equipe 1"], ["Diagnostic initial"]],
                     [[datetime(2026, 6, 8)], [datetime(2026, 6, 8, 10, 0)], ["Equipe 1"], ["Rendez-vous de suivi"]],
                     [[datetime(2026, 6, 15)], [datetime(2026, 6, 15, 10, 0)], ["Equipe 1"], ["Rendez-vous de suivi 2"]]])

print(parcours[1, 1])

print("Test d'ajout d'un parcours type à un patient dans le calendrier :")
ajout_parcours_patient(test_calendrier, "Patient 1", parcours, memoire_patient)
print(test_calendrier)
print("Mémoire patients :")
print(memoire_patient)