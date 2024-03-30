from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, logout
from apps.user.forms import RegisterUserForm, LoginUserForm
# Create your views here.
class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'user/auth.html'
    success_url = reverse_lazy('book:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['description']='Пожалуйста, заполните эту форму, чтобы создать учетную запись.'
        context['title'] = 'Регистрация'
        return context
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('book:index')
        
        
           
class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'user/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['description']='Пожалуйста, заполните эту форму, чтобы войти в учетную запись.'
        context['title'] = 'Войти'
        
        return context
    
    def get_success_url(self):
        return reverse_lazy('book:index')

def logout_user(request):
    logout(request)
    return redirect('book:index')