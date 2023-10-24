from django.db import models
class personal_rooms(models.Model):
   live_room_phone_number=models.IntegerField()
   live_room_country_code=models.IntegerField()
   live_room_profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)


   live_room_user_name=models.CharField(max_length=70)
   live_room_gender=models.CharField(max_length=10)
   live_room_gmail=models.CharField(max_length=80)
   live_room_password=models.CharField(max_length=70)

   def __str__(self):
     
        return f'{self.live_room_phone_number} ({self.live_room_gmail}) ({self.live_room_country_code}) ({self.live_room_gender}) ({self.live_room_gmail}) ({self.live_room_password})'
   class Meta:
        app_label = 'liveroom'