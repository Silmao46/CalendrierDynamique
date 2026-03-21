# CalendrierDynamique

Architecture :

classe Calendrier:

Méthode ajout d'événement
    Entrée : Date de début (datetime), Date de fin (datetime), Propriétaire (str), Description (str)
    Ajoute un événement dans l'Array du calendrier
    Retourne l'ID de l'événement ajouté pour aider l'automatisation

Méthode suppression d'événement
    Entrée : ID
    Supprime un événement dans l'Array du calendrier
    Soulève une erreur si l'ID est inexistant

Méthode de déplacement d'événement
    Entrée : ID, Date de déplacement(datetime)
    Déplace l'événement ID à date de déplacement
    Soulève une erreur si l'ID est inexistant

Méthode de sortie des tous les événements d'un propriétaire
    Entrée : Propriétaire (str)
    Retourne une classe Calendrier contenant seulement les événements du Propriétaire
    Soulève une erreur si le propriétaire n'a aucun événement

Méthode de modification de la date de fin
    Entrée : ID, Nouvelle date de fin (datetime)
    Remplace la date de fin de l'événement ID
    Soulève une erreur si l'ID est inexistant
    Soulève une erreur si la Nouvelle date de fin est avant la date de début

Méthode de modification de la description
    Entrée : ID, Nouvelle description
    Remplace la description de l'événement ID
    Soulève une erreur si l'ID est inexistant

Méthode de modification du propriétaire
    Entrée : ID, Nouveau propriétaire
    Remplace le propriétaire de l'événement ID
    Soulève une erreur si l'ID est inexistant

Format de stockage :
    Array : [Date de début, Date de fin, Propriétaire, Description, ID] x n éléments
    ID : Déterminé selon l'ID max dans la liste d'événements. Utiliser un ID absolu ?
