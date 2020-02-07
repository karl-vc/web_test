from django.db import models

# Create your models here.

class roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=100)


    def __str__(self):
        return self.role_name


#company profile only shows in admin panel
class company_profile(models.Model):
    role_id =models.ForeignKey(roles, on_delete=models.CASCADE)
    company_useremail=models.EmailField(primary_key=True,max_length=225)
    company_userpassword=models.CharField(max_length=1000)
    company_name=models.CharField(max_length=255)
    contact_person=models.CharField(max_length=255)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=255)
    postal_code = models.IntegerField(null=True)
    state_province = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, default="")
    mobile_number = models.CharField(max_length=15, default="")
    fax = models.CharField(max_length=50)
    website_url = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    profile_updated = models.BooleanField(default=False)
    password_updated = models.BooleanField(default=False)
    created_date = models.DateTimeField()




# HR/User Model
class user_profile(models.Model):
    role_id = models.ForeignKey(roles, on_delete=models.CASCADE)
    user_firstname = models.CharField(max_length=255)
    user_lastname = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=255)
    user_password = models.CharField(max_length=1000)
    username = models.CharField(max_length=255, default="")
    user_company_email = models.CharField(max_length=255, default="")
    user_company = models.CharField(max_length=255, default="")
    user_phone = models.CharField(max_length=15, default="")
    user_employee_id = models.CharField(
        max_length=1000, unique=True, primary_key=True, default="")
    employee_read = models.BooleanField(default=False, null=True)
    employee_create = models.BooleanField(default=False, null=True)
    employee_edit = models.BooleanField(default=False, null=True)
    employee_delete = models.BooleanField(default=False, null=True)
    leaves_read = models.BooleanField(default=False, null=True)
    leaves_create = models.BooleanField(default=False, null=True)
    leaves_edit = models.BooleanField(default=False, null=True)
    leaves_delete = models.BooleanField(default=False, null=True)
    holidays_read = models.BooleanField(default=False, null=True)
    holidays_create = models.BooleanField(default=False, null=True)
    holidays_edit = models.BooleanField(default=False, null=True)
    holidays_delete = models.BooleanField(default=False, null=True)
    event_read = models.BooleanField(default=False, null=True)
    event_create = models.BooleanField(default=False, null=True)
    event_edit = models.BooleanField(default=False, null=True)
    event_delete = models.BooleanField(default=False, null=True)
    is_active = models.BooleanField(default=False)
    created_date = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.user_email


# Departments
class department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255)
    added_by = models.CharField(max_length=255, default="")
    edited_by = models.CharField(max_length=255, default="")
    deleted_by = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.department_name


#designations based on departments
class designation(models.Model):
    designation_id = models.AutoField(primary_key=True)
    designation_name = models.CharField(max_length=255)
    department_id = models.ForeignKey(department, on_delete=models.CASCADE)
    added_by = models.CharField(max_length=255, default="")
    edited_by = models.CharField(max_length=255, default="")
    deleted_by = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.designation_name


# employee profile details
class employee_profile(models.Model):
    role_id = models.ForeignKey(roles, on_delete=models.CASCADE)
    department_id = models.ForeignKey(department, on_delete=models.CASCADE)
    designation_id = models.ForeignKey(designation, on_delete=models.CASCADE)
    employee_firstname = models.CharField(max_length=255)
    employee_lastname = models.CharField(max_length=255)
    employee_username = models.CharField(max_length=255, default="")
    employee_official_email = models.EmailField(max_length=255, default="")
    employee_personal_email = models.EmailField(max_length=255, default="")
    employee_password = models.CharField(max_length=1000)
    employee_company = models.CharField(max_length=255)
    employee_hr_name = models.CharField(max_length=255, default="")
    employee_company_email = models.CharField(max_length=255, default="")
    employee_hr_email = models.CharField(max_length=255, default="")
    employee_phone = models.CharField(max_length=15, default="")
    employee_employee_id = models.CharField(
        max_length=1000, primary_key=True, unique=True, default="")
    profile_edit = models.BooleanField(default=False)
    added_by = models.CharField(max_length=255)
    edited_by = models.CharField(max_length=255)
    deleted_by = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_terminated = models.BooleanField(default=False)
    terminated_by = models.CharField(default="", max_length=255)
    promoted_by = models.CharField(default="", max_length=255)
    created_date = models.CharField(max_length=255, default="")
    terminated_date = models.CharField(max_length=255, default="")
    gender = models.CharField(max_length=50, default="", null=True)
    birthday = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=500, default="")
    martial_status = models.CharField(max_length=255, default="")

    masters_college_name = models.CharField(max_length=500, default="")
    masters_college_course_name = models.CharField(max_length=500, default="")
    masters_college_details = models.CharField(max_length=500, default="")
    masters_start_year = models.CharField(max_length=4, default="")
    masters_complete_year = models.CharField(max_length=4, default="")

    graduation_college_name = models.CharField(max_length=500, default="")
    graduation_college_course_name = models.CharField(
        max_length=500, default="")
    graduation_college_details = models.CharField(max_length=500, default="")
    graduation_start_year = models.CharField(max_length=4, default="")
    graduation_complete_year = models.CharField(max_length=4, default="")

    sec_schl_name = models.CharField(max_length=500, default="")
    sec_schl_board = models.CharField(max_length=255, default="")
    sec_schl_details = models.CharField(max_length=500, default="")

    sec_schl_complete_year = models.CharField(max_length=4, default="")

    matric_schl_name = models.CharField(max_length=500, default="")
    matric_schl_board = models.CharField(max_length=255, default="")
    matric_schl_details = models.CharField(max_length=500, default="")

    matric_schl_complete_year = models.CharField(max_length=4, default="")
    permission_to_edit = models.BooleanField(default=False)
    updated_once = models.BooleanField(default=False)
    # 0=none 1= request for edit 2=approved  3=declined 4=request for delete
    request_status = models.IntegerField(default=0)
    edit_request_hr_email = models.CharField(max_length=255, default="")
    edit_request_emp_email = models.CharField(max_length=255, default="")
    edit_request_by_emp = models.BooleanField(default=False)
    edit_request_by_hr = models.BooleanField(default=False)

    def __str__(self):
        return self.employee_official_email
