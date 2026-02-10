from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from user.forms import CustomUserForm


class UserRegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = CustomUserForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_staff = True
        user.save()

        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = 'login.html'
    next_page = '/'