from django import forms
#from Firstapp.models we import all the models by importing *
from Firstapp.models import *

# from Firstapp.models import company_profile



# class LoginForm(forms.Form):
#     email = forms.CharField(required=True,label='Email',max_length=255,widget=forms.TextInput(
#        attrs={
#            'class':'form-control',
#            'placeholder':'Email',
#        }
#     ))
#     password = forms.CharField(label='password',max_length=255,widget=forms.PasswordInput(
#         attrs={
#             'class':'form-control',
#             'placeholder':'Email',
#
#         }
#     ))

class LoginForm(forms.ModelForm):
    class Meta:
        model = company_profile
        exclude = ["role_id",
                   "company_useremail",
                   "company_userpassword",
                   "company_name",
                   "contact_person",
                   "address",
                   "country",
                   "city",
                   "postal",
                   "state_province",
                   "phone_number",
                   "mobile_number",
                   "fax",
                   "website_url",
                   "is_active",
                   "profile_updated",
                   "password_updated",
                   "created_data",


                   ]

class user_profileForm(forms.ModelForm):
    class Meta:
        model = user_profile
        exclude = ["role_id",
                   "user_firstname",
                   "user_lastname",
                   "user_email",
                   "user_password",
                   "username",
                   "user_company_email",
                   "user_company",
                   "user_phone",
                   "user_employee_id",
                   "employee_read",
                   "employee_create",
                   "employee_edit",
                   "employee_delete",
                   "leaves_read",
                   "leaves_create",
                   "leaves_edit",
                   "leaves_delete",
                   "holidays_read",
                   "holidays_create",
                   "holidyas_edit",
                   "holidays_delete",
                   "event_read",
                   "event_create",
                   "event_edit",
                   "event_delete",
                   "is_active",
                   "created_data",




        ]

class employee_profileForm(forms.ModelForm):
    class Meta:
        model= employee_profile
        exclude=[
            "role_id",
            "department_id",
            "designation_id",
            "employee_firstname",
            "employee_lastname",
            "employee_username",
            "employee_officaial_email",
            "employee_personal_email",
            "employee_password",
            "employee_company",
            "employee_hr_name",
            "employee_company_email",
            "employee_hr_email",
            "employee_phone",
            "employee_employee_id",
            "profile_edit",
            "added_by",
            "edited_by",
            "deleted_by",
            "is_active",
            "is_terminated",
            "terminated_by",
            "promoted_by",
            "created_date",
            "terminated_date",
            "promoted_by",
            "created_date",
            "terminated_date",
            "gender",
            "birthdat",
            "address",
            "martial_status",
            "masters_college_name",
            "masters_college_cource_name",
            "masters_college_details",
            "masters_start_year",
            "masters_complete_year",
            "graduation_college_name",
            "graduation_college_cource_name",
            "graduation_start_year",
            "graduation_complete_year",
            "sec_schl_name",
            "sec_schl_board",
            "sec_schl_details",
            "sec_schl_complete_year",
            "matric_schl_name",
            "matric_schl_board",
            "matric_schl_details",
            "matric_schl_complete_year",
            "permission_to_edit",
            "updated_once",
            "request_status",
            "edit_request_hr_email",
            "edit_request_emp_email",
            "edit_request_by_emp"
            "edit_request_by_hr",




        ]

class departmentForm(forms.ModelForm):
    class meta:
        model=department
        exclude=[
            "department_id",
            "department_name",
            "added_by",
            "edited_by",
            "deleted_by",

        ]

class designation(forms.ModelForm):
    class Meta:
        model=designation
        exclude=[
            "designation_id",
            "designation_name",
            "department_id",
            "added_by",
            "edited_by",
            "deleted_by",
        ]