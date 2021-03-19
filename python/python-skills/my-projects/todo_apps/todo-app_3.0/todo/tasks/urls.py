from django.urls import path

from . import views
from django.contrib.auth import views as auth_views       #alias isliye kia hai takay match na hujaii orignal view

urlpatterns=[
    path('',views.userpage,name='list'),
    path('index/',views.index,name='user-page'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('register/',views.register,name='register'),
    path('account-created/<key1>/',views.Account_created_email,name='account-created'),
    path('confirm-account/<key1>/',views.confirm_account_email,name='confirm-account'),
    path('update_tasks/<int:pk>/',views.update_task,name='update_tasks'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('account-settings/',views.accountSettings,name='account-settings'),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="tasks/password_reset.html"),
     name="reset_password"),     #submit email form    #settings file mai smtp configuration set kru

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="tasks/password_reset_sent.html"), 
        name="password_reset_done"),    # email set sucess message            #url sent in the email for conformation

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="tasks/password_reset_form.html"), 
     name="password_reset_confirm"),   # link to password reset form in email


    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="tasks/password_reset_done.html"), 
        name="password_reset_complete"),   # password sucessfully changed message   # name chnage ni hungay inkay

]


