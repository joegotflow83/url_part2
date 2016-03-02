from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm


class Register(FormView):

    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    fields = ['username', 'email', 'password1', 'password2']

    def get_success_url(self):
        """Redirect user to url converter page"""
        return reverse('login')

    def form_valid(self, form):
        """Validate the form"""
        user = User.objects.create_user(form.cleaned_data['username'],
                                        form.cleaned_data['password1'])
        user.save()
        return super().form_valid(form)
