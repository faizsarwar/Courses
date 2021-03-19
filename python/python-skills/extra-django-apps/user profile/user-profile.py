
				#	in models.py 

from django.contrib.auth.models import User
	# making one to one relation with parent model(jis model ko user banana hai wo user banayga nh bs relation set huga )
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    
    



				#	 in views.py

# fetching user,and its tasks from post request  (where profile is parent model and task is child model[forign key profile ])
task=request.user.profile.tasks_set.create(title=request.POST)



    if request.method=='POST':
        form=createuserform(request.POST)  #usercreation form ko costumize kia hai forms.py mai
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='profile')
            user.groups.add(group)                          # create krte hi group mai add krdega
            profile.objects.create(user=user,name=user.username)  # (jessay hi profile model create huga uska user khud create hujaiga)




# fetching a posted field from a posted form
            username =form.cleaned_data.get('username')                 #form say data catch krnay keliye
            
            
            
            
            
            
            
            
            # us todo itm ko queryset mai say is tarha fetch kia tha (extra hai ye)
            
            
    w=list(tasks)
    todotasks=[]
    for i in w:
        print(i.id)
        #print(str(i).split(',')[1].split(':')[1])
        todoItem=str(i).split(',')[1].split(':')[1]
        todoItemWord=todoItem[3:-2]
            
            
            
            
            
            
