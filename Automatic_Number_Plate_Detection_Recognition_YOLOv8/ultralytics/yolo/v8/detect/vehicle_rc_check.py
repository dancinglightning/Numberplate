import requests

def is_valid(numberplate):
    url = "https://rto-vehicle-information-verification-india.p.rapidapi.com/api/v1/rc/vehicleinfo"

    payload = {
        "reg_no": numberplate,
        "consent": "Y",
        "consent_text": "I hear by declare my consent agreement for fetching my information via AITAN Labs API"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "c089d67699msh85665753b86bb42p1bce4bjsn44cea35cb78c",
        "X-RapidAPI-Host": "rto-vehicle-information-verification-india.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()['status']