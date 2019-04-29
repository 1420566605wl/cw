from django.db import models

class Userinfo(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender_choices = ((0, '保密'), (1, '男'), (2, '女'))
    gender = models.SmallIntegerField(choices=gender_choices, default=0, verbose_name="性别")
    hobby = models.CharField(max_length=128)
