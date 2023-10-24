from django.db import models
class userprofile(models.Model):
    image=models.FileField(upload_to='images')

# Create your models here.
class writing(models.Model):
    user_name_community = models.CharField(max_length=50)
    user_email_community = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=13)
    comment = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.user_name_community} ({self.user_email_community}) ({self.age}) ({self.gender}) ({self.comment})'

class param(models.Model):





    comment=models.TextField()
    def __str__(self):

        return f'{self.comment}'    
class personal_detail(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    age=models.ImageField()
    gender=models.CharField(max_length=40)
    comments=models.TextField()
    def __str__(self):
     
        return f'{self.name} ({self.email}) ({self.age}) ({self.gender}) ({self.comments})'
    




from django.db import models



class User(models.Model):
    phone_number = models.CharField(max_length=20)
    country_code = models.CharField(max_length=10)
    user_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    gmail = models.EmailField()
    password = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return f"User: {self.user_name}, Phone: {self.phone_number}, Email: {self.gmail}, Gender:{self.gender},country_code:{self.country_code},password:{self.password},profile_picture:{self.profile_picture}"
class create_room(models.Model):
    user_name=models.CharField(max_length=20)
    tag=models.CharField(max_length=20)
    text=models.CharField(max_length=20)
    followers=models.IntegerField()
    room_ide=models.IntegerField()
    token=models.CharField(max_length=100,default=0)
    def __str__(self):
        return f"user:{self.user_name}, tag:{self.tag}, text:{self.text},followers:{self.followers},user_ide:{self.room_ide}"
class topics(models.Model):
    
    part1=models.CharField(max_length=500)
    part2=models.CharField(max_length=600)
    part3=models.CharField(max_length=500)
    def __str__(self):
        return f"part1:{self.part1}, part2:{self.part2},part3:{self.part3}"

class Question(models.Model):
    topic = models.ForeignKey(topics, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)

    def __str__(self):
        return self.question_text


