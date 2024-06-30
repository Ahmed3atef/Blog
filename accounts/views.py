from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView,ListView
from .models import CustomUser
from blog.models import Post
from .forms import CustomUserCreationForm



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    model = CustomUser
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    enctype = "multipart/form-data"

class ProfileView(ListView):
    model = Post
    template_name = 'accounts/profile.html'
    
    def get_queryset(self):
        username = self.kwargs.get('username')
        user = get_object_or_404(CustomUser, username=username)
        return Post.objects.filter(author=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs.get('username')
        context['user_profile'] = get_object_or_404(CustomUser, username=username)
        return context