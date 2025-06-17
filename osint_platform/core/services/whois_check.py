import whois

def check_domain(domain):
    try:
        w = whois.whois(domain)
        return w.__dict__
    except Exception as e:
        return {"error": str(e)}