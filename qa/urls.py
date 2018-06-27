from django.conf.urls import url,include
from .views import QuestionDetail,AnswerDetail,QACenterView
from . import views

app_name='qa'
urlpatterns=[
    url('^$',QACenterView.as_view(),name='qa_center'),
    url('^ask/$',views.ask,name='ask'),
    url('^answer/$',views.answer,name='answer'),
    url('^Q_detail/(?P<pk>\d{1,5})/$',QuestionDetail.as_view(),name='question_detail'),
    url('^A_detail/(?P<pk>\d{1,5})/$',AnswerDetail.as_view(),name='answer_detail')
]
