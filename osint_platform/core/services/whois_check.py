import whois

def serialize_date(date):
    if isinstance(date, list):
        return [d.strftime("%Y-%m-%d") for d in date]
    elif hasattr(date, "strftime"):
        return date.strftime("%Y-%m-%d")
    return str(date)

def check_domain(domain):
    try:
        data = whois.whois(domain)
        return {
            "Registrar": data.registrar,
            "CreationDate": serialize_date(data.creation_date),
            "ExpirationDate": serialize_date(data.expiration_date),
            "NameServers": data.name_servers if isinstance(data.name_servers, list) else [data.name_servers],
        }
    except Exception as e:
        return {"error": str(e)}
