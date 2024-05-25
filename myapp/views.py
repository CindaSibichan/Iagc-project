from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import View
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from .forms import *
import json

# Create your views here.
class LoginPageView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'authorization/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse({'success': True, 'username': user.username})
            else:
                return JsonResponse({'success': False}, status=401)
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        
        
@csrf_exempt
def dashboard(request):
    persons = Person.objects.all().order_by('id')
    form = PersonForm()
    pagenator = Paginator(persons,20)
    page_num = request.GET.get("page")
    try:
        persons = pagenator.page(page_num)

    except PageNotAnInteger:
        persons = pagenator.page(1)  
    except EmptyPage:
        persons = pagenator.page(pagenator.num_pages) 

    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = PersonForm()
    return render(request, "card.html", {'form': form ,'persons':persons})




@require_GET
def generate_id(request):
    last_person = Person.objects.order_by('id').last()
    if last_person:
        try:
            unique_id_parts = last_person.unique_id.split('-')
            if len(unique_id_parts) == 2 and '/' in unique_id_parts[1]:
                last_id = int(unique_id_parts[1].split('/')[0])
                new_id = f"KL-{last_id + 1:04d}/TVM"
            else:
                new_id = "KL-0001/TVM"
        except (IndexError, ValueError):
            new_id = "KL-0001/TVM"
    else:
        new_id = "KL-0001/TVM"
    
    return JsonResponse({'unique_id': new_id})


@csrf_exempt
def edit_Person(request, pk):
    if request.method == 'POST':
        try:
            person = get_object_or_404(Person, id=pk)
            form = PersonForm(request.POST, instance=person)
            if form.is_valid():
                form.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'errors': form.errors})
        except Exception as e:
            # Log the exception for debugging
            print("Exception occurred:", e)
            return JsonResponse({'success': False, 'error': 'An error occurred while processing the request'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
    

def delete_person(request, pk):
    if request.method == 'POST':
        person = get_object_or_404(Person, id=pk)
        person.delete()
        return JsonResponse({'status': 'success'}, status=200)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)    

def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        print(query)
        if query:
            persons = Person.objects.filter(name__icontains = query)   

            return render(request,"dashboard.html",{'persons': persons}) 
        else:
            return render(request,'dashboard.html')

# def filter_expired_persons(request):
#     if request.method == 'POST':
#         expiration_status = request.POST.get('expiration_status')
#         today = date.today()

#         if expiration_status == 'expired':
#             persons = Person.objects.filter(validity_date__lte=today)
#         elif expiration_status == 'valid':
#             persons = Person.objects.filter(validity_date__gt=today)
#         else:
#             persons = Person.objects.all()

#         return render(request, 'card.html', {'persons': persons})

    
#     return render(request, 'card.html')



@login_required(login_url='login_page')
def logout(request):
    auth.logout(request)
    return redirect("login_page")







