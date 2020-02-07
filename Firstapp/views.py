from django.contrib.auth.hashers import check_password
from django.shortcuts import render,HttpResponse,redirect



# Create your views here.
#from Firstapp.forms import LoginForm, company_profile, user_profile
from Firstapp.forms import *





def login(request):
    form = LoginForm()

    if request.method =='POST':
        form = LoginForm(request.POST)
        try:
            role=int(request.POST.get('role_id'))
            #store the roleid in integer form

            if int(role)==1:
                if form.is_valid():
                    email=request.POST['email']
                    password = request.POST['password']
                 #storing the values of email and password that are entered by user
                    try:
                        company_data = company_profile.objects.get(company_useremail=email)
                        #storing the company data like email by using .get method
                        if email ==  company_data.company_useremail:#it compares the user entered email to the company email

                            try:
                                #checking weather the password is encrypted(updated) or not
                                if not company_data.password_updated:
                                    if company_data.company_userpassword == password:
                                        request.session['user_email'] = email
                                        request.session['user_role_id'] = company_data.role_id_id
                                        request.session['user_is_authenticated'] =True
                                        return redirect("/change-password")
                                    elif company_data.company_userpassword != password:
                                        return render(request,'login.html',{'invalid_credentials': True,'form': form})

                                if company_data.pasword_updated:

                                    if check_password(password,company_data.company_userpasssword):
                                        request.session['user_email'] = email
                                        request.session['user_role_id'] = company_data.role_id_id
                                        request.session['user is authenticated'] =True
                                        if not company_data.profile_updated:
                                            return redirect("/home")
                                    else:
                                        return render(request,'login.html', {'invalid_credentials': True, 'form': form})
                            except:

                                return render(request,'login.html', {'invalid_credentials': True, 'form': form})

                    except:

                        return render(request, 'login.html',{'invalid_credentials': True, 'form': form})


            elif int(role) == 2:

                if form.is_valid():

                    email = request.POST['email']

                    password = request.POST['password']

                    hr_data = user_profile.objects.get(user_email=email)

                    if check_password(password, hr_data.user_password):

                        request.session['user_email'] = email

                        request.session['user_role_id'] = hr_data.role_id_id

                        request.session['user_is_authenticated'] = True

                        return redirect("/home")

                    else:

                        form = LoginForm(request.POST)

                        return render(request, 'login.html', {'invalid_credentials': True, 'form': form})


            elif int(role)==3:
                if form.is_valid():
                    email = request.POST['email']
                    password = request.POST['password']
                    employee_data=employee_profile.object.get(employee_official_email=email)
                    if check_password(password,employee_data.employee_password):
                        if not employee_data.is_terminated:
                            request.session['user_email']=email
                            request.session['user_role_id']=employee_data.role_id_id
                            request.session['user is authenticated']= True
                            return redirect("/home")
                        if employee_data.is_terminated:
                            form = LoginForm(request.POST)
                            return render(request, 'login.html', {'invalid_credentials': True, 'form': form})
                    else:
                        form = LoginForm(request.POST)
                        return render(request, 'login.html', {'invalid_credentials': True, 'form': form})

                elif not form.is_valid():
                    form = LoginForm(request.POST)
                    return render(request, 'login.html', {'invalid_credentials': True, 'form': form})

            else:
                form = LoginForm(request.POST)
                return render(request, 'login.html', {'invalid_credentials': True, 'form': form})

        except:
            form = LoginForm(request.POST)
            return render(request, 'login.html', {'invalid_credentials': True, 'form': form})



    return render(request,'login.html',{'form':form})

def test(request):
    return HttpResponse('hello this is working ')