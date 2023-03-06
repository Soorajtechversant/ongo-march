from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from django.contrib.staticfiles.urls import static
from ongoappfolder import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('ongoappfolder.urls' )),
    path('subscription',include('subscription.urls')),
    path('cart',include('cart.urls' )),
    path('payments/',include('payments.urls' )),
    path('chat/', include('chat.urls')),
    path('search/', include('haystack.urls')),
    
    # path('social-auth/', include('social_django.urls', namespace="social")),
    path('registration/', include('social_django.urls', namespace="social")),
    path('accounts/', include('allauth.urls')),
  
    # path('oauth/', include('social_django.urls', namespace='social')), 
    # path('settings/', core_views.SettingsView.as_view(), name='settings'),
    # path('settings/password/', core_views.password, name='password'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#For serving uploaded files