

# image upload settings


#						#in models.py
  profile_pic=models.ImageField(null=True,blank=True,default='download.png')     #first run cammand pip install pillow, also add media root 												in settings file
  
  					
  						#in settings.py
  MEDIA_ROOT=os.path.join(BASE_DIR,'static/images')    #ju bhi pic upload hugi yhn save hugi


						#in views.py
						
@login_required(login_url='login')
@allowed_users(allowed_roles=['profile','staff','admin'])
def accountSettings(request):       #added-customer form 
    profile=request.user.profile
    form=profileform(instance=profile)
    if request.method=="POST":
        form=profileform(request.POST,request.FILES,instance=profile)
    if form.is_valid():
        form.save()
    context={'form':form}
    return render(request,"tasks/account-settings.html",context)      


