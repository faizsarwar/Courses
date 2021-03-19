# settings py mai ye paste kruu or static/app/file banaloo aur url template mai use krsktay hain
# image keliye /static/images/ is mai images rkh lu



MEDIA_URL='/images/'

STATICFILES_DIRS=[           #base_dir ka mtlb root directory
    os.path.join(BASE_DIR,'static')  
    
    
    
    #url is trha usde huga
    {% static 'myapp/style.css' %}
