from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from user.forms import CustomUserForm
from django.core.mail import send_mail
from django.contrib import messages


class UserRegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = CustomUserForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        user_token = default_token_generator.make_token(user)
        activation_url = self.request.build_absolute_uri(reverse_lazy('user:activate', kwargs={'user_pk': user.pk, 'token': user_token}))

        send_mail('Activate your account',
                  f'Hello, {user.username}! Please activate your account by clicking on the link: \n {activation_url}',
                  '',
                  [user.email]
                  )

        messages.success(self.request, 'Please confirm your email to complete registration!')
        return redirect('user:login')

def activate_user(request, user_pk, token):
    user = User.objects.get(pk=user_pk)

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your account has been activated successfully!')
        return redirect('user:login')

    messages.warning(request, 'Invalid activation link or expired token!')
    return redirect('/')

class UserLoginView(LoginView):
    template_name = 'login.html'
    next_page = '/'
















