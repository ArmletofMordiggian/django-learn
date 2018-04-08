from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import Member,Beclass,Hobby
from .forms import SearchForm

def index(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            nameform = form.cleaned_data['nameform']
            #somebody = get_object_or_404(Member, user_name=nameform)
            member_list = Member.objects.all().filter(user_name=nameform)
            #print(anybody)
            return render(request, 'ourclass/submit.html', context = {'member_list': member_list})
        else:
            return HttpResponse('something error')
    else:
        member_list = Member.objects.all().order_by('-birth_time')
        return render(request, 'ourclass/index.html', context={'member_list': member_list})


def personalpage(request, user_name):
    somebody = get_object_or_404(Member, user_name=user_name)
    return render(request, 'ourclass/personalpage.html', context = {'somebody': somebody})