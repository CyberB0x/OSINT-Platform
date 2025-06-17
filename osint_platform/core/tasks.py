from celery import shared_task
from .models import OSINTQuery
from .services import email_check, whois_check

@shared_task
def run_email_check(email):
    result = email_check.check_email(email)
    OSINTQuery.objects.create(query_type="email", input_data=email, result=result)


@shared_task
def run_domain_check(domain):
    result = whois_check.check_domain(domain)
    OSINTQuery.objects.create(query_type="domain", input_data=domain, result=result)