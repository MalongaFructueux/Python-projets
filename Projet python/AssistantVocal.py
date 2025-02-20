import speech_recognition as sr
import pyttsx3
import os
import webbrowser

# Initialiser le moteur de synthèse vocale
engine = pyttsx3.init()

def parler(texte):
    """Fait parler l'assistant."""
    engine.say(texte)
    engine.runAndWait()

def ecouter():
    """Écoute une commande vocale et la retourne sous forme de texte."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Je vous écoute...")
        audio = recognizer.listen(source)

        try:
            commande = recognizer.recognize_google(audio, language='fr-FR')
            print(f"Vous avez dit : {commande}")
            return commande.lower()
        except sr.UnknownValueError:
            print("Je n'ai pas compris votre commande.")
            return ""
        except sr.RequestError:
            print("Le service de reconnaissance vocale est indisponible.")
            return ""

def executer_commande(commande):
    """Exécute une commande en fonction de l'entrée utilisateur."""
    if "ouvre" in commande:
        application = commande.replace("ouvre ", "")
        parler(f"Ouverture de {application}")
        os.system(f"open -a {application}")  # Pour macOS
        # os.system(f"start {application}")  # Pour Windows
        # os.system(f"{application} &")      # Pour Linux
    elif "cherche" in commande:
        recherche = commande.replace("cherche ", "")
        parler(f"Recherche de {recherche} sur le web")
        webbrowser.open(f"https://www.google.com/search?q={recherche}")
    elif "arrête-toi" in commande or "au revoir" in commande:
        parler("Au revoir !")
        exit()
    else:
        parler("Commande non reconnue. Veuillez réessayer.")

if __name__ == "__main__":
    parler("Bonjour, comment puis-je vous aider ?")
    while True:
        commande = ecouter()
        if commande:
            executer_commande(commande)
