from django.db import models

# Create your models here.


class login(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.user_name


class register_user(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.user_name

# class question(models.Model):
#     question_id = models.AutoField(primary_key=True)
#     question_title = models.CharField(max_length=220)
#     question_text = models.CharField(max_length=500)
#     question_already_done = models.CharField(max_length=300)
#     question_tags = models.CharField(max_length=100)
#     question_pub_date = models.DateTimeField('date published')

#     def __str__(self) -> str:
#         return self.question_text
