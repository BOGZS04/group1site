from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Genders, Users
from django.contrib.auth.hashers import make_password


# Create your views here.

def gender_list(request):
   try:
      genders = Genders.objects.all()

      data = {
         'genders':genders
      }

      return render(request, 'gender/GendersList.html', data)
   except Exception as e:
     return HttpResponse(f'Error Occured During Loading Gender List: {e}')

def add_gender(request):
    try:
      if request.method == 'POST':
        gender = request.POST.get('gender')

        Genders.objects.create(gender=gender).save()
        messages.success(request, 'Gender Added Successfully!')
        return redirect('/gender/list')
      else:
        return render(request, 'gender/AddGender.html')
    except Exception as e: 
        return HttpResponse(f'Error Occurred During Add Gender: {e}')  

def edit_gender(request, genderId):
   try:
      if request.method == 'POST':
        genderObj = Genders.objects.get(pk=genderId)

        gender = request.POST.get('gender')    

        genderObj.gender = gender
        genderObj.save()

        messages.success(request, 'Gender Updated Successfully')

        data = {
         'gender': genderObj
      }

        return render(request, 'gender/EditGender.html', data)
      else:
        genderObj = Genders.objects.get(pk=genderId)

      data = {
         'gender': genderObj
      }

      return render(request, 'gender/EditGender.html', data)
   
   except Exception as e:
      return HttpResponse(f'Error Occurred During Edit Gender: {e}')
   
def delete_gender(request, genderId):
    try:
        if request.method == 'POST':
          genderObj = Genders.objects.get(pk=genderId)
          genderObj.delete()

          messages.success(request, 'Gender Deleted Successfully')
          return redirect('/gender/list')

        else:
          genderObj = Genders.objects.get(pk=genderId)

        data = {
            'gender': genderObj
        }

        return render(request, 'gender/DeleteGender.html', data)
    except Exception as e:
        return HttpResponse(f'Error Occurred During Delete Gender: {e}')

def user_list(request):
   try:
     userObj = Users.objects.select_related('gender') 

     data = {
        'users': userObj
     } 

     return render(request, 'user/UsersList.html', data)
   except Exception as e:
      return HttpResponse(f'Error Occurred During Loading User List: {e}')   

def add_user(request):
   try: 
      if request.method == 'POST':
        full_name = request.POST.get('full_name') 
        gender = request.POST.get('gender')
        birth_date = request.POST.get('birth_date')
        address = request.POST.get('address')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirm_password')

        if password != confirmPassword:
           messages.error(request, 'Password and Confirm Password do not match')
           return redirect('/user/add')

        Users.objects.create(
           full_name=full_name,
           gender=Genders.objects.get(pk=gender), 
           birth_date=birth_date,
           address=address,
           contact_number=contact_number,
           email=email,
           username=username,
           password=make_password(password) 
        ).save() 

        messages.success(request, 'User Added Successfully!')
        return redirect('/user/add')
        
      else:
        genderObj = Genders.objects.all()

      data = {
         'genders': genderObj
      }

      return render(request, 'user/AddUser.html', data)
   except Exception as e:
      return HttpResponse(f'Error Occurred During Add User: {e}')

