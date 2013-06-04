
#from django.http import HttpResponse

#def home(request):
#    return HttpResponse("You're looking at the home page.")

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from gracelee.forms import SignUpForm, EmailForm
from gracelee.models import gracelee
        

class NewCreateView(CreateView):
    form_class = SignUpForm

    def form_valid(self, form):
        email = self.request.POST['email']
        organization = self.request.POST['organization']
        send_mail('subject', "Email: {0} \n Organization: {1}".format(email, organization), 'test@gmail.com', ['testing@gmail.com'], fail_silently=True)
        return super(NewCreateView, self).form_valid(form)