

from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):              #logn hua wa user login page nhi dekh skta logout hunay say pehlay #agr pehlay hi registered hai tu direct login huga
		if request.user.is_authenticated:
			return redirect('/')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse("you are not allowed to view this page")
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request,*args,**kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group == 'staff':
            return HttpResponse('Only admins can view this page')
        if group == "admin":
            return view_func(request,*args,**kwargs)
    return wrapper_func        
