from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^registration/$', views.RegistrationView.as_view(), name="registration"),
    url(r'^success/$', views.RegistrationSuccessView.as_view(), name="registration-success"),
    url(r'^annotate/$', views.AnnotationView.as_view(), name="annotation"),
    url(r'^annotate_complete/$', views.AnnotationCompleteView.as_view(), name="annotate-complete"),

]
