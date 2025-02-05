from django.db import models


class Register(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    registrationNo = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    course = models.CharField(max_length=60)
    jumuiya = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    password1 = models.CharField(max_length=60)
    password2 = models.CharField(max_length=60)


class Registration(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    password1 = models.CharField(max_length=60)
    password2 = models.CharField(max_length=60)

    def __str__(self):
        return self.first_name


class Activity(models.Model):
    ActivityName = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.ActivityName


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.title


