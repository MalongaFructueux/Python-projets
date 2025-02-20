# Dictionnaire des correspondances
correspondances = {
    'A': {'bon': 'Règle', 'mauvais': 'Rigidité', 'but': 'Établir des limites saines'},
    'B': {'bon': 'Passage', 'mauvais': 'Instabilité', 'but': 'Construire des fondations'},
    'C': {'bon': 'Corps', 'mauvais': 'Superficialité', 'but': 'Unir le corps et l\'esprit'},
    'D': {'bon': 'Venir de', 'mauvais': 'Attachement', 'but': 'Trouver l\'origine'},
    'E': {'bon': 'Monde, création', 'mauvais': 'Illusion', 'but': 'Compréhension de l\'environnement'},
    'F': {'bon': 'Feu', 'mauvais': 'Colère', 'but': 'Éclairer la voie'},
    'G': {'bon': 'Chercher à l\'intérieur de', 'mauvais': 'Obsession', 'but': 'Auto-découverte'},
    'H': {'bon': 'Équilibre', 'mauvais': 'Indécision', 'but': 'Harmonie personnelle'},
    'I': {'bon': 'Unité (le tout, l\'onde unique)', 'mauvais': 'Isolation', 'but': 'Comprendre que chaque chose est en toi et que tu es en chaque chose'},
    'J': {'bon': 'Unité fixe', 'mauvais': 'Rigidité', 'but': 'Adaptation'},
    'K': {'bon': 'Casser', 'mauvais': 'Destruction', 'but': 'Transformation positive'},
    'L': {'bon': 'Mouvement dirigé', 'mauvais': 'Dérive', 'but': 'But précis'},
    'M': {'bon': 'Création', 'mauvais': 'Éparpillement', 'but': 'Manifestation'},
    'N': {'bon': 'Retournement, la haine', 'mauvais': 'Confusion', 'but': 'Nouveau regard'},
    'O': {'bon': 'Corps & Esprit', 'mauvais': 'Fragmentation', 'but': 'Alignement interne'},
    'P': {'bon': 'Transmission - Père', 'mauvais': 'Autoritarisme', 'but': 'Partage de sagesse'},
    'Q': {'bon': 'Séparer Corps & Esprit', 'mauvais': 'Dissociation', 'but': 'Compréhension duale'},
    'R': {'bon': 'Souffle (agitation, émotions)', 'mauvais': 'Laxisme', 'but': 'Maîtrise des émotions'},
    'S': {'bon': 'Mouvement dans tous les sens', 'mauvais': 'Instabilité', 'but': 'Flexibilité'},
    'T': {'bon': 'Terre, les racines', 'mauvais': 'Lourdeur', 'but': 'Ancrage'},
    'U': {'bon': 'Remplir de', 'mauvais': 'Vide', 'but': 'Satisfaction intérieure'},
    'V': {'bon': 'Ramener à un point', 'mauvais': 'Éparpillement', 'but': 'Clarté de but'},
    'W': {'bon': 'La concentration', 'mauvais': '-', 'but': '-'},
    'X': {'bon': 'Axe', 'mauvais': 'Confusion', 'but': 'Stabilité'},
    'Y': {'bon': 'Synthèse', 'mauvais': 'Éparpillement', 'but': 'Connexion à l\'essentiel'},
    'Z': {'bon': 'Retournement de la terre', 'mauvais': 'Éparpillement', 'but': 'Connexion à l\'essentiel'}
}

def get_random_phrase(array):
    """Retourne une phrase aléatoire d'un tableau."""
    import random
    return random.choice(array)

def generate_general_interpretation(bon_cote, mauvais_cote, buts):
    """Génère une interprétation générale basée sur les côtés bons, mauvais et les buts."""
    bon_phrase = f"Le bon côté c’est {', '.join(bon_cote)}."
    mauvais_phrase = f"Le mauvais côté c’est {', '.join(mauvais_cote)}."
    but_phrase = f"Le droit chemin c’est peut-être {', '.join(buts)}."
    return f"{bon_phrase} {mauvais_phrase} {but_phrase}"

def analyze_name(name):
    """Analyse un prénom et retourne une interprétation basée sur les correspondances."""
    name = name.upper()
    bon_cote = []
    mauvais_cote = []
    buts = []

    for letter in name:
        if letter in correspondances:
            bon_cote.append(correspondances[letter]['bon'])
            mauvais_cote.append(correspondances[letter]['mauvais'])
            buts.append(correspondances[letter]['but'])

    interpretation_generale = generate_general_interpretation(bon_cote, mauvais_cote, buts)

    result = {
        'Bon côté': ', '.join(bon_cote),
        'Mauvais côté': ', '.join(mauvais_cote),
        'But universel': ', '.join(buts),
        'Interprétation Générale': interpretation_generale
    }

    return result

# Exemple d'utilisation
if __name__ == "__main__":
    name_input = input("Entrez un prénom ou un nom : ")
    result = analyze_name(name_input)
    for key, value in result.items():
        print(f"{key} : {value}")
