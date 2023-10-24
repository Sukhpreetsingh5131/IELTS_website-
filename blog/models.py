from django.db import models
#from django.core.validators import MinValueValidator,MaxValueValidator


class teacher(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    def __str__(self):
       return f'{self.first_name} ({self.last_name})'
    #salory=models.IntegerField()


class email(models.Model):



    name=models.ForeignKey(teacher,on_delete=models.CASCADE)
    no=models.IntegerField()
class Review(models.Model):
    user_mail=models.CharField(max_length=100)
    password=models.IntegerField()
    def __str__(self):
       return f'{self.user_mail} ({self.password})'
        
class accounts(models.Model):
    user_name=models.CharField(max_length=70)
    user_email=models.CharField(max_length=100)
    user_city=models.TextField()
    user_education=models.CharField(max_length=50)
    user_password=models.IntegerField()
    def __str__(self):
       return f'{self.user_name} ({self.user_email}) ({self.user_city}) ({self.user_education}) ({self.user_password})'
class transcript(models.Model):
    long_text=models.TextField()
    def __str__(self):
        return f'{self.long_text}'



    




# Create your models here.







