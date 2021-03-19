from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

    ##apps.py file mai changes krni hungii iskay baad


#@receiver(post_save,sender=User)                        #library import krwani paraygii(connect krnay ka dosraa tareeka)
def Create_profile(sender,instance,created,**kwargs):            
    if created:
        group=Group.objects.get(name='profile')
        instance.groups.add(group)                          # create krte hi group mai add krdega
        profile.objects.create(user=instance,name=instance.username)
        print('profile created')

post_save.connect(Create_profile,sender=User)       # connecting sender with reciever.  (connect krnay ka pehla tareeka)


#@receiver(post_save,sender=User)
def update_profile(sender,instance,created,**kwargs):
    if created==False:
            instance.profile.save()
            print("profile updatd")


post_save.connect(update_profile,sender=User)




