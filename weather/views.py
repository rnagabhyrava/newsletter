from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
try:
    from django.urls import reverse_lazy
except ImportError:
    from django.core.urlresolvers import reverse_lazy
from django.forms import inlineformset_factory
from django.views.generic.edit import CreateView
  
from dal import autocomplete
from weather.models import Email, Location
from .forms import SignupForm


def done(request):
    return render(request, 'weather/done.html', {})

    
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email_address', '')
            location = request.POST.get('location', '')
            loc_obj = get_object_or_404(Location, pk=location)
            
            new_email = Email(email_address=email, location=loc_obj)
            new_email.save()

            return HttpResponseRedirect(reverse('weather:done'))
    else:
        form = SignupForm()
    
    return render(request, 'weather/signup.html', {'form': form})

class LocationAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Location.objects.all().order_by('pk')
        
        if self.q:
            qs = qs.filter(city__istartswith=self.q)

        return qs
