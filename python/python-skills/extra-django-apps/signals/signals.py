
						# in signalspy
						
						
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

from django.contrib.auth.models import User

    ##apps.py file mai changes krni hungii iskay baad


@receiver(post_save,sender=User)                        #library import krwani paraygii(connect krnay ka dosraa tareeka)
def Create_profile(sender,instance,created,**kwargs):
    if created:
        <modelname>.objects.create(user=instance,name=instance.username)
        print('profile created')

#post_save.connect(Create_profile,sender=User)       # connecting sender with reciever.  (connect krnay ka pehla tareeka)


@receiver(post_save,sender=User)
def update_profile(sender,instance,created,**kwargs):
    if created==False:
            <modelname>.profiles.save()
            print("profile updatd")


#post_save.connect(update_profile,sender=User)





						# in apps.py
						
						
from django.apps import AppConfig


class MyappConfig(AppConfig):
    name = 'myapp'
    def ready(self):
        import myapp.signals
						
						
						
						
						
