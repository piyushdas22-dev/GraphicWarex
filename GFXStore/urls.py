from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    # path('blog/', include("blog.urls")),
    path('accounts/', include("accounts.urls")),
    path('gfx/', include("gfx.urls")),
    path('contact/', views.contact, name="contact"),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL,
#                       document_root=settings.STATICFILES_DIRS[0])
