from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class HomePageView(TemplateView):
    template_name = 'payments/home.html'

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request):  # new
    if request.method == 'POST':

        paisa = request.POST.get('paisa')
        charge = stripe.Charge.create(
            amount=paisa,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
    return render(request, 'payments/charge.html')
