from django.db import models
from django.contrib.auth.models import User
from PIL import Image

User._meta.get_field('email')._unique = True


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    is_counsellor = models.BooleanField(default=False)
    bio = models.TextField(null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            ouput_size = (300,300)
            img.thumbnail(ouput_size)
            img.save(self.image.path)

    def get_phones(self):
        return self.user.phone_set.all()


class CounsellorDetails(models.Model):
    fee = models.IntegerField(default=0)
    turn_around_time = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name}\'s Counsellor Details'

    class Meta:
        verbose_name = 'Counsellor Details'
        verbose_name_plural = 'Counsellors Details'


class Phone(models.Model):
    phone = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} {self.phone}'

