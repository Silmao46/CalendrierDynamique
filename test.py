"""Exemple rudimentaire pour calendrier dynamique"""


from datetime import datetime
from calendrier import Calendrier


# Initialisation du calendrier
test_calendrier = Calendrier()

# Ajout d'événements
test_calendrier.ajouter_evenement(datetime(2026, 6, 2), "Equipe 2", "Diagnostic initial")
test_calendrier.ajouter_evenement(datetime(2026, 6, 3), "Equipe 2", "Rendez-vous de suivi")
test_calendrier.ajouter_evenement(datetime(2026, 6, 2), "Equipe 1", "Diagnostic initial")

print(test_calendrier)

# Déplacement d'un événement

test_calendrier.deplacer_evenement(0, datetime(2026, 6, 4))

print(test_calendrier)

# Affichage du calendrier d'un propriétaire spécifique

calendrier_equipe2 = test_calendrier.calendrier_proprietaire("Equipe 2")

print(calendrier_equipe2)

# Suppression d'un événement

test_calendrier.suppression_evenement(1)

print(test_calendrier)

# Test de suppression avec un index hors limites

test_calendrier.suppression_evenement(5)

# Test de rajout d'un événement après suppression

test_calendrier.ajouter_evenement(datetime(2026, 6, 5), "Equipe 2", "Rendez-vous de suivi 2")

# Affichage du calendrier d'un propriétaire spécifique

calendrier_equipe2 = test_calendrier.calendrier_proprietaire("Equipe 2")

print(calendrier_equipe2)