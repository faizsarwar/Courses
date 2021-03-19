#settings file mai ye paste kru



#SMTP CONFIGUARTION

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587        # google krlu jiska chaiye
EMAIL_USE_TLS=True    
EMAIL_HOST_USER='faizsarwar856@gmail.com'   	#jis email say eail sent hugi
EMAIL_HOST_PASSWORD='perfectcup'		#uska password



# is url pe jaoo upar wala email login kr k button option on krdu on krduu

#https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4Pk-Keq9mB_K-41Z_uN0gja5e-37vPAOWFvniv07yynpHLNQOiZOb5irOCup90zn2s8UcomO-2YHP6ynLXCrTHx29qntQ



# app kay urls file (not project)  mai ye paste kru  without changig any thing





from django.contrib.auth import views as aurth_view       #alias isliye kia hai takay match na hujaii orignal view
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="tasks/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="tasks/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="tasks/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="tasks/password_reset_done.html"), 
        name="password_reset_complete"),


