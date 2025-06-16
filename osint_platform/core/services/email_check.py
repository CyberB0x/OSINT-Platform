import requests

def check_email(email):
    headers = {'User-Agent': 'OSINT-Platform'}
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return {"status": "found", "data": response.json()}
    return {"status": "not_found"}