from django.urls import path
from . import views


app_name="polls" #agr kisi or app mai same name ki htl hugi tu is say differentiate huga
urlpatterns=[
    path('',views.index,name='index'), # " " iska matlab homepage pe show krna hai polls app k, views.index ka mtlb views.py file mai index ka function call krna hai.
                                      # name=index  hamain html likhtay wqt kaam ayga is url ka reference dena hua agr tu
    # ex: /polls/5/
    path('specific/<int:question_id>/',views.detail,name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/',views.results,name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/votes/",views.vote,name="vote"),

]