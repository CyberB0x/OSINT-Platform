import whois

def check_domain(domain):
    try:
        data = whois.whois(domain)
        return {
            "Registrar": data.registrar,
            "CreationDate": str(data.creation_date),
            "ExpirationDate": str(data.expiration_date),
            "NameServers": data.name_servers if isinstance(data.name_servers, list) else [data.name_servers],
        }
    except Exception as e:
        return {"error": str(e)}
