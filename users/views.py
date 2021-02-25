from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from django.core.paginator import Paginator

class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    context_object_name = 'users_list'
    template_name = 'users_list.html'
    paginate_by = 10

    def listing(request):
        user_list = CustomUser.objects.all()
        paginator = Paginator(user_list, 10)
        page_number = request.Get.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'user_index.html', {'page_obj': page_obj})