from django.contrib import admin
from django.urls import path
import blog.views
import portfolio.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home,name='home'),
    path('blog/<int:blog_id>/',blog.views.detail,name='detail'),
    path('blog/new/',blog.views.new,name='new'),
    path('blog/create/',blog.views.create,name='create'),
    path('blog/contact/',blog.views.contact,name='contact'),
    path('portfolio/',portfolio.views.portfolio,name='portfolio'),
    path('accounts/signup/',accounts.views.signup,name='signup'),
    path('accounts/login/',accounts.views.login,name='login'),
    path('accounts/logout/',accounts.views.logout,name='logout'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
