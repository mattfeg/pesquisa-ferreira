import requests

api_key = "--"

#for aresta in arestas:
    
params = {
    'key': api_key,
    'origins':'AQUIRAZ%20CE',
    'destinations':'HOSP%20GERAL%20MANUEL%20ASSUNCAO%20PIRES',
    'units':'metric'
    }

url = f"https://maps.googleapis.com/maps/api/json?"

response = requests.get(url, params=params)

try:
    data = response.json()
except ValueError as e:
    print(f"Error decoding JSON: {e}")
    print(f"Response content: {response.content}")

if data["status"] == "OK":
    # do something with the data
    distancia = data["rows"]["elements"]["distance"]["value"]
    tempo = data["rows"]["elements"]["duration"]["value"]
else:
    print(f"Falha ao buscar informações")

print(f"Distância: {distancia} metros")
print(f"Tempo: {tempo} segundos")

# {
#   "origins": [
#     {
#       "lat": 55.93,
#       "lng": -3.118
#     },
#     "Greenwich, England"
#   ],
#   "destinations": [
#     "Stockholm, Sweden",
#     {
#       "lat": 50.087,
#       "lng": 14.421
#     }
#   ],
#   "travelMode": "DRIVING",
#   "unitSystem": 0,
#   "avoidHighways": false,
#   "avoidTolls": false
# }

# Usar API do Google Maps para calcular distância entre dois pontos
# https://developers.google.com/maps/documentation/distance-matrix/overview
