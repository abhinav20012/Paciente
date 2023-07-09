from django.db import models

# Create your models here.
class signUpInfo1(models.Model):
    loginUser = models.CharField(max_length = 122)
    loginPassword = models.CharField(max_length = 122)
    rePassword = models.CharField(max_length = 122)

    def __str__(self):
        return self.loginUser

class signUpInfo2(models.Model):
    firstName = models.CharField(max_length = 122)
    lastName = models.CharField(max_length = 122)
    email = models.EmailField(max_length = 122)
    otp = models.CharField(max_length = 122)
    document = models.FileField(upload_to = None, null = True)

    def __str__(self):
        return self.email

# class login(models.Model):
#     username = models.CharField(max_length = 122)
#     email = models.CharField(max_length = 122)

#     def __str__(self):
#         return self.email