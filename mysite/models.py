from django.db import models



# Create your models here.



class CountryImages(models.Model):
     Country = models.CharField(max_length=200, unique=True)
     Country_photo = models.ImageField(upload_to='images')

     def __str__(self):
         return self.Country

class Tourism (models.Model):
    Country = models.CharField(max_length=200, unique=True)
    Description = models.CharField(max_length=5000)

    def __str__(self):
        return self.Country


class scholars_list(models.Model):
    Country = models.TextField()
    Name = models.TextField(unique=True, primary_key=True )
    Description = models.TextField()
    level = models.TextField()
    last_date = models.DateField()
    scholarship = models.TextField()
    link = models.TextField()
    status = models.IntegerField()

    def __str__(self):
        return self.Name



# class Basicinfo(models.Model):
#     Country = models.CharField(max_length=200, unique=True)
#     Passport_Validity = models.CharField(max_length=300)
#     Blank_Passport_pages = models.CharField(max_length=300)
#     Tourist_visa_required = models.CharField(max_length=300)
#     Vacction = models.CharField(max_length=300)
#     Currency_restriction_For_Entry = models.CharField(max_length=300)
#     Currency_restriction_For_Exit = models.CharField(max_length=300)
#
#
#     def __str__(self):
#         return self.Country

class Basicinfo(models.Model):
    id = models.IntegerField(blank=True)
    name = models.TextField(blank=True, primary_key=True, unique=True)
    validity = models.TextField(blank=True, null=True)
    blank_pages = models.TextField(blank=True, null=True)
    vaccination = models.TextField(blank=True, null=True)
    amount_entry = models.TextField(blank=True, null=True)
    amount_exit = models.TextField(blank=True, null=True)
    link = models.TextField()
    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'basicinfo'

class VisaInformation(models.Model):
    id = models.IntegerField(blank=True)
    name = models.TextField(blank=True, primary_key=True, unique=True)
    study_visa = models.TextField(blank=True, null=True)
    visit_visa = models.TextField(blank=True, null=True)
    business_visa = models.TextField(blank=True, null=True)
    employment_visa = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'visa_information'

class Contacts(models.Model):
    firstname = models.TextField()
    lastname = models.TextField()
    email = models.TextField(blank=True)
    subjects = models.TextField(primary_key=True)
    message = models.TextField()

    def __str__(self):
        return self.email




class newScholarship(models.Model):
    username = models.TextField()
    email = models.TextField()
    name = models.TextField(primary_key=True)

    def __str__(self):
        return self.name


class reviews(models.Model):
    username = models.TextField()
    comment = models.TextField()

    def _str_(self):
        return self.username



