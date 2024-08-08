from django.db import models

class basic_mcq(models.Model):
    ques_description = models.TextField(max_length=700)
    Option1 = models.TextField(max_length=200)
    Option2 = models.TextField(max_length=200)
    Option3 = models.TextField(max_length=200)
    Option4 = models.TextField(max_length=200)
    answers = models.TextField(max_length=200)

class basic_tf(models.Model):
    ques_description = models.TextField(max_length=700)
    answers = models.TextField(max_length=200)
     

class basic_fbl(models.Model):
    ques_description = models.TextField(max_length=700)
    answers = models.TextField(max_length=200)     