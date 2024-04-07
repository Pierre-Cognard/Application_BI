import requests
import base64

# Remplacez "votre_client_id" et "votre_client_secret" par vos informations d'identification client INSEE
client_id = "votre_client_id"
client_secret = "votre_client_secret"

# URL de l'endpoint pour obtenir le jeton d'accès
token_url = "https://api.insee.fr/token"

# Données à envoyer avec la demande POST
data = {
    "grant_type": "client_credentials"
}

# En-tête d'autorisation contenant les informations d'identification client codées en base64
# Format: base64(client_id:client_secret)
auth_header = {
    "Authorization": "Basic " + base64.b64encode((client_id + ":" + client_secret).encode()).decode()
}

# Envoi de la demande POST pour obtenir le jeton d'accès
response = requests.post(token_url, data=data, headers=auth_header)

# Vérification de la réponse
if response.status_code == 200:
    # Affichage du jeton d'accès
    print("Token d'accès:", response.json()["access_token"])
else:
    # Affichage du message d'erreur en cas d'échec de la demande
    print("Échec de la demande:", response.text)
