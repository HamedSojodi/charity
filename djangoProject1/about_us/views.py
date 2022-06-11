from django.shortcuts import render, get_object_or_404
from django.views import View, generic
from django.views.generic import ListView

from accounts.models import User


# class about_us(View):
#     def get(self, request):
#         users = User.objects.all()
#         return render(request, 'about_us.html', {'users':users})
class about_us(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'about_us.html'
