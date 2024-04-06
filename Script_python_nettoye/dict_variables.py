dict_type_variables = {
    "name [Agents]": {"Type": "Textuelle", "File": "Agents.csv","Log":False, "Seuil": 50, "Grouper":True}, # OK
    "name [Names]": {"Type": "Textuelle", "File": "Names.csv","Log":False, "Seuil": 100, "Grouper":True}, # OK
    "name [Criteria]": {"Type": "Textuelle", "File": "Criteria.csv","Log":False, "Seuil": 10000, "Grouper":False}, # OK
    "siret": {"Type": "Numérique", "File": "Agents.csv","Log":True, "Seuil": 1, "Grouper":False}, # A CORRIGER
    "address": {"Type": "Textuelle", "File": "Agents.csv","Log":False, "Seuil": 70, "Grouper":True}, # OK
    "city": {"Type": "Textuelle", "File": "Agents.csv","Log":False,"Seuil": 1000, "Grouper":False}, # OK
    "zipcode": {"Type": "Numérique", "File": "Agents.csv","Log":False, "Seuil": 800, "Grouper":False}, # OK Textuelle --> Numérique
    "country": {"Type": "Textuelle", "File": "Agents.csv","Log":False, "Seuil": 5000, "Grouper":False}, # OK
    "department": {"Type": "Textuelle", "File": "Agents.csv","Log":False, "Seuil": 2000, "Grouper":False}, # OK
    "longitude": {"Type": "Numérique", "File": "Agents.csv","Log":True, "Grouper":False},
    "latitude": {"Type": "Numérique", "File": "Agents.csv","Log":True, "Grouper":False},
    "weight": {"Type": "Numérique", "File": "Criteria.csv","Log":True, "Grouper":False},
    "type": {"Type": "Categorielle", "File": "Criteria.csv","Log":False, "Seuil": 1, "Grouper":False}, # OK
    "correctionsNb": {"Type": "Numérique", "File": "Lots.csv","Log":True, "Grouper":False},
    "cancelled": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1, "Grouper":False}, # OK
    "awardDate": {"Type": "Textuelle", "File": "Lots.csv","Log":False, "Seuil": 1000, "Grouper":False}, # OK mais interprétation ?
    "awardEstimatedPrice": {"Type": "Numérique", "File": "Lots.csv","Log":True, "Grouper":False},
    "awardPrice": {"Type": "Numérique", "File": "Lots.csv","Log":True, "Grouper":False},
    "cpv": {"Type": "Textuelle", "File": "Lots.csv","Log":False, "Seuil": 1000, "Grouper":False}, # A CORRIGER
    "tenderNumber": {"Type": "Numérique", "File": "Lots.csv","Log":True, "Grouper":False},
    "onBehalf": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1, "Grouper":False}, # OK
    "jointProcurement": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1, "Grouper":False}, # OK
    "fraAgreement": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1, "Grouper":False}, # OK
    "fraEstimated": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1, "Grouper":False}, # OK
    "numberTenders": {"Type": "Numérique", "File": "Lots.csv","Log":True, "Grouper":False},
    "accelerated": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1, "Grouper":False}, # OK le reste à N ?
    "outOfDirectives": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1, "Grouper":False}, # OK
    "contractorSme": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 11000, "Grouper":False}, # OK fixed
    "numberTendersSme": {"Type": "Numérique", "File": "Lots.csv","Log":True, "Grouper":False},
    "subContracted": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1, "Grouper":False}, # OK
    "gpa": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1, "Grouper":False},
    "multipleCae": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1, "Grouper":False}, # OK
    "typeOfContract": {"Type": "Textuelle", "File": "Lots.csv","Log":False, "Seuil": 1, "Grouper":False},
    "topType": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1, "Grouper":False}, # OK
    "renewal": {"Type": "Categorielle", "File": "Lots.csv","Log":False, "Seuil": 1, "Grouper":False}, # OK
    "contractDuration": {"Type": "Numérique", "File": "Lots.csv","Log":True, "Grouper":False},
    "publicityDuration": {"Type": "Numérique", "File": "Lots.csv","Log":True, "Grouper":False},
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
