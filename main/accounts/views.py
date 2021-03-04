from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from django.views.generic import UpdateView, CreateView

from accounts.forms import UserUpdateForm

# LoginRequiredMixin добавляет проверку того, что пользователь авторизован в системе


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/user_update.html'
    # отвечает за импорт модели пользователя
    model = get_user_model()
    form_class = UserUpdateForm
    success_url = '/'

    def get_object(self, queryset=None):
        return self.request.user
