from django.db import models

# Create your models here.

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100, null=False)
    user_email = models.CharField(max_length=150, null=False)


    class Meta:
        db_table = "User"

    def __str__(self):
        return self.user_name
