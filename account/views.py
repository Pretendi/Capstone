from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



#my simplified usercreation form
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('survey')
    else:
        form = UserRegisterForm()
    return render(request, 'register_paul.html', {'form': form})

def survey(request):
    return render(request, 'questionaires.html')
    #if request.method == ""

#def profile(request):
#    return render(request, )
    # Simon's default code
"""
class LoginView(FormView):

    form_class = LoginForm
    template_name = 'account/login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form, **kwargs):
        kwargs.update({'form': form})
        return self.render_to_response(self.get_context_data(**kwargs))

    def get_success_url(self):
       return self.request.POST.get('next', reverse('index'))
"""
