import requests
import json
import pandas as pd
from datetime import datetime



# Liste des villes pour lesquelles nous voulons récupérer les données météorologiques
villes = ["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Strasbourg", "Montpellier", "Bordeaux", "Lille", "Rennes", "Reims", "Le Havre", "Saint-Etienne", "Toulon", "Grenoble", "Dijon", "Angers", "Nîmes", "Villeurbanne"]

# Clé API pour OpenWeatherMap
api_cle = "ccd28dc62bea9dff40f57b56e9073c9b"

# Création d'un DataFrame pour stocker les données
df = pd.DataFrame(columns=["Ville", "Température actuelle", "Température ressentie", "Température minimale", "Température maximale", "Pression atmosphérique", "Humidité", "Vitesse du vent", "Direction du vent", "Lever du soleil", "Coucher du soleil"])

# Boucle pour effectuer des requêtes pour chaque ville et stocker les données dans le DataFrame
for ville in villes:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ville},fr&appid={api_cle}"
    response = requests.get(url)
    data = response.json()
    
    temperature_actuelle = data["main"]["temp"] -273.15
    temperature_ressentie = data["main"]["feels_like"] -273.15
    temperature_minimale = data["main"]["temp_min"] -273.15
    temperature_maximale = data["main"]["temp_max"] -273.15
    pression = data["main"]["pressure"]
    humidite = data["main"]["humidity"]

    vent_vitesse = data["wind"]["speed"]
    vent_direction = data["wind"]["deg"]
     # Conversion des horaires de lever et coucher du soleil
    lever_soleil = datetime.fromtimestamp(data["sys"]["sunrise"])
    coucher_soleil = datetime.fromtimestamp(data["sys"]["sunset"])
    
   
    

  
  

    # Ajout des données dans le DataFrame
    df2 = pd.DataFrame({
        "Ville": ville,
        "Température actuelle": temperature_actuelle,
        "Température ressentie": temperature_ressentie,
        "Température minimale": temperature_minimale,
        "Température maximale": temperature_maximale,
        "Pression atmosphérique": pression,
        "Humidité": humidite,
        "Vitesse du vent": vent_vitesse,
        "Direction du vent": vent_direction,
        "Lever du soleil": lever_soleil.strftime("%H:%M:%S"),
        "Coucher du soleil": coucher_soleil.strftime("%H:%M:%S"),
        
    },index=[0])
# concaténation du dataframe princial avec le dataframe contenant les données requetées sur l'api
    df = pd.concat([df, df2], ignore_index=True)

print(df)

#export du dataframe au format csv
df.to_csv('meteo_villes_francaises.csv', index=False)

