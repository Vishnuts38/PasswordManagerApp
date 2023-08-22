from django.db import models

from django.contrib.auth.models import User

class PasswordItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

class PasswordShare(models.Model):
    shared_with = models.ForeignKey(User, on_delete=models.CASCADE)
    password_item = models.ForeignKey(PasswordItem, on_delete=models.CASCADE)
    access_type = models.CharField(max_length=10, choices=[('view', 'View'), ('edit', 'Edit')])

class Organisation(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password_org = models.CharField(max_length=100)




