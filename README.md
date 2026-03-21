# CalendrierDynamique

Architecture :

classe Calendrier:

Méthode ajout d'événement
    Entrée : Date(datetime), Propriétaire (str), Description (str)
    Ajoute un événement dans l'Array du calendrier
    Retourne l'ID de l'événement ajouté pour aider l'automatisation
Méthode suppression d'événement
    Entrée : ID
    Supprime un événement dans l'Array du calendrier
Méthode de déplacement d'événement
    Entrée : ID, Date de déplacement(datetime)
    Déplace l'événement ID à date de déplacement
Méthode de sortie des tous les événements d'un propriétaire
    Entrée : Propriétaire (str)
    Retourne une classe Calendrier contenant seulement les événements du Propriétaire

Format de stockage :
    Array : [Date, Propriétaire, Description, ID] x n éléments
    ID : Déterminé selon l'ID max dans la liste d'événements. Utiliser un ID absolu ?
