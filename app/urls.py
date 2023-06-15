from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.home_view import *
from .views.category_view import *
from .views.product_view import *
from .views.review_view import *
from .views.search_view import *
from .views.account_view import *

app_name = 'app'

urlpatterns = [
    path('search/', search, name='search'),
    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('logout/', logout_view, name='logout_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

