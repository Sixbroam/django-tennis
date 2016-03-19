from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from .settings.base import ADMIN_SITE_HEADER
from rest_framework import routers
from .apps.events.api import views as events_views
from .apps.users.api import views as users_views

router = routers.DefaultRouter()
router.register(r'tournaments', events_views.TournamentViewSet)
router.register(r'matches', events_views.MatchViewset)
router.register(r'users', users_views.UserViewSet)
router.register(r'players', users_views.PlayerViewSet)
router.register(r'clubs', users_views.ClubViewset)

urlpatterns = [
    # Examples:
    # url(r'^$', 'tt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = ADMIN_SITE_HEADER
