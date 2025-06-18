from django.shortcuts import render, redirect
from .models import OSINTQuery
from .tasks import run_email_check, run_domain_check


def dashboard(request):
    history = OSINTQuery.objects.order_by('-created_at')[:20]
    return render(request, 'index.html', {'history': history})


def scan_email(request):
    email = request.GET.get('email')
    if email:
        run_email_check.delay(email)
    return redirect('/')


def scan_domain(request):
    domain = request.GET.get('domain')
    if domain:
        run_domain_check.delay(domain)
    return redirect('/')

def clear_history(request):
    OSINTQuery.objects.all().delete()
    return redirect('/')