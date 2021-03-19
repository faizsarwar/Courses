from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('Date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now  # mtlb pub-bate (self.pub_date) aur (now) k beech mai hai
        



class choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)#choice_set use krna parayga shell mai isko change bhi krsktay hain is bracket mai related_name=choice use kr kay
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

# see the documentations also