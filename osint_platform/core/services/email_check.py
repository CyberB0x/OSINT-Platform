import requests

def check_email(email):
    # Заглушка
    if email == "test@mail.com":
        return {
            "status": "found",
            "breaches": [
                {"name": "Adobe", "date": "2013-10-04"},
                {"name": "LinkedIn", "date": "2012-06-05"}
            ]
        }
    else:
        return {"status": "not_found"}