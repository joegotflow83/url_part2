from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.models import User

from .models import URL, Click


class Home(View):

    def get(self, request):
        """Redirect users to login"""
        return redirect(reverse('login'))


class Converter(CreateView):

    model = URL
    fields = ['url', 'short', 'description', 'private']

    def form_valid(self, form):
        """Validate the form"""
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super().form_valid(form)

    def get_success_url(self):
        """Clean the form for the user to enter another url"""
        return reverse('converter')


class UpdateURL(UpdateView):

    template_name = 'main/url_update_form.html'
    model = URL
    fields = ['url', 'short', 'description']

    def form_valid(self, form):
        object = form.save(commit=False)
        user = User.objects.get(pk=self.request.user.id)
        if user != object.user:
            return redirect(reverse('error'))
        object.save()
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect user to url list"""
        return reverse('url_list')


class URLList(ListView):

    model = URL


class URLDetail(DetailView)

    model URL


class URLRedirect(View):

    def get(self, request, url):
        """Redirect a user to their desired link from their new url"""
        new_url = get_object_or_404(URL, short=url)
        Click.objects.create(bookmark=new_url)
        return redirect(new_url.url)


class Error(View):

    def get(self, request):
        """Dispaly error page"""
        return render(request, 'errors/error.html')
