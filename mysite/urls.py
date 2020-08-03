from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='home'),
    path('index.html', views.index, name='home'),
    path('login.html', views.login, name='login'),
    path('signup.html', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('about.html', views.about, name='about'),
    path('scholars_List.html', views.scholars_List.as_view(), name='scholars_List'),
    path('tourism.html', views.tourism, name='tourism'),
    path('Bussines.html', views.bussines, name='bussines'),
    path('Employment.html', views.employment, name='employment'),
    path('Study.html', views.study, name='study'),
    path('contact.html', views.Contact, name='contact'),
    path('Detail.html', views.Detail, name='Detail'),
    path('resetPassword.html', views.resetpassword, name='resetPassword'),
    path('passwordConfirm.html', views.passwordConfirm, name='passwordConfirm'),
    path('PostScholarship.html', views.PostScholarship, name='PostScholarship'),
    path('activate/<uidb64>/<token>/',views.activate, name='activate')

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

