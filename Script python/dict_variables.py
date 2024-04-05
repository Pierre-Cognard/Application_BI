dict_type_variables = {
    "name [Agents]": {"Type": "Textuelle", "File": "Agents.csv","Log":False, "Seuil": 100}, # OK
    "name [Names]": {"Type": "Textuelle", "File": "Names.csv","Log":False, "Seuil": 100}, # OK
    "name [Criteria]": {"Type": "Textuelle", "File": "Criteria.csv","Log":False, "Seuil": 10000}, # OK
    "siret": {"Type": "Numérique", "File": "Agents.csv","Log":True, "Seuil": 1}, # A CORRIGER
    "address": {"Type": "Textuelle", "File": "Agents.csv","Log":False, "Seuil": 70}, # OK
    "city": {"Type": "Textuelle", "File": "Agents.csv","Log":False,"Seuil": 1000}, # OK
    "zipcode": {"Type": "Numérique", "File": "Agents.csv","Log":False, "Seuil": 800}, # OK Textuelle --> Numérique
    "country": {"Type": "Textuelle", "File": "Agents.csv","Log":False, "Seuil": 1}, # OK
    "department": {"Type": "Textuelle", "File": "Agents.csv","Log":False, "Seuil": 2000}, # OK
    "longitude": {"Type": "Numérique", "File": "Agents.csv","Log":True},
    "latitude": {"Type": "Numérique", "File": "Agents.csv","Log":True},
    "weight": {"Type": "Numérique", "File": "Criteria.csv","Log":True},
    "type": {"Type": "Categorielle", "File": "Criteria.csv","Log":False, "Seuil": 1}, # OK
    "correctionsNb": {"Type": "Numérique", "File": "Lots.csv","Log":True},
    "cancelled": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1}, # OK
    "awardDate": {"Type": "Textuelle", "File": "Lots.csv","Log":False, "Seuil": 1000}, # OK mais interprétation ?
    "awardEstimatedPrice": {"Type": "Numérique", "File": "Lots.csv","Log":True},
    "awardPrice": {"Type": "Numérique", "File": "Lots.csv","Log":True},
    "cpv": {"Type": "Numérique", "File": "Lots.csv","Log":True, "Seuil": 20000}, # A CORRIGER
    "lotsNumber": {"Type": "Textuelle", "File": "Lots.csv","Log":True, "Seuil": 1001},
    "onBehalf": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1}, # OK
    "jointProcurement": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1}, # OK
    "fraAgreement": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1}, # OK
    "fraEstimated": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1}, # OK
    "numberTenders": {"Type": "Numérique", "File": "Lots.csv","Log":True},
    "accelerated": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1}, # OK le reste à N ?
    "outOfDirectives": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1}, # OK
    "contractorSme": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 11000}, # OK fixed
    "numberTendersSme": {"Type": "Numérique", "File": "Lots.csv","Log":True},
    "subContracted": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1}, # OK
    "gpa": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1},
    "multipleCae": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1}, # OK
    "typeOfContract": {"Type": "Textuelle", "File": "Lots.csv","Log":False, "Seuil": 1},
    "topType": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1}, # OK
    "renewal": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1}, # OK
    "contractDuration": {"Type": "Numérique", "File": "Lots.csv","Log":True},
    "publicityDuration": {"Type": "Numérique", "File": "Lots.csv","Log":True},
}


dict_fichier_variables = {
    "name": "Agents.csv",
    "siret": "Agents.csv",
    "address": "Agents.csv",
    "city": "Agents.csv",
    "zipcode": "Agents.csv",
    "country": "Agents.csv",
    "department": "Agents.csv",
    "longitude": "Agents.csv",
    "latitude": "Agents.csv",
    "weight": "Criteria.csv",
    "type": "Criteria.csv",
    "correctionsNb": "Lots.csv",
    "cancelled": "Lots.csv",
    "awardDate": "Lots.csv",
    "awardEstimatedPrice": "Lots.csv",
    "awardPrice": "Lots.csv",
    "cpv": "Lots.csv",
    "tenderNumber": "Lots.csv",
    "onBehalf": "Lots.csv",
    "jointProcurement": "Lots.csv",
    "fraAgreement": "Lots.csv",
    "fraEstimated": "Lots.csv",
    "numberTenders": "Lots.csv",
    "accelerated": "Lots.csv",
    "outOfDirectives": "Lots.csv",
    "contractorSme": "Lots.csv",
    "numberTendersSme": "Lots.csv",
    "subContracted": "Lots.csv",
    "gpa": "Lots.csv",
    "multipleCae": "Lots.csv",
    "typeOfContract": "Lots.csv",
    "topType": "Lots.csv",
    "renewal": "Lots.csv",
    "contractDuration": "Lots.csv",
    "publicityDuration": "Lots.csv",
}
