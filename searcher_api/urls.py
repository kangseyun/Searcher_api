from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from django.conf.urls import include, url

from rest_framework import routers, serializers, viewsets

from api.views.stock import kospi, kosdaq, nasdaq, dji
from api.views.issue import issue_list
from api.views.login import login, logout, token_check
from api.views.community import community_list, get_community, community_post, delete_community
from api.views.push import fcm_push, pushToken
from api.views.condition import get_conditionlist, get_condition_item, get_condition_items
from api.views.rank import rank_one, rank_down, kosdaq_up, kosdaq_down


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ('url', 'username', 'email', 'is_staff')
        model = User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^kospi/$', kospi),
    url(r'^kosdaq/$', kosdaq),
    url(r'^nasdaq/$', nasdaq),
    url(r'^dji/$', dji),
    url(r'^issue/$', issue_list),

    url(r'^board/$', community_list),
    url(r'^board/get/$', get_community),
    url(r'^board/delete/$', delete_community),
    url(r'^board/post/$', community_post),
    url(r'^set_pushToken/$', pushToken),
    url(r'^push_condition/$', fcm_push),

    url(r'^condition/gets/$', get_conditionlist),
    url(r'^condition_item/gets/$', get_condition_items),
    url(r'^condition_item/get/$', get_condition_item),
    url(r'^condition_push/$', fcm_push),
    url(r'fcm/', include('fcm.urls')),

    url(r'^rank/$', rank_one),
    url(r'^rank2/$', rank_down),
    url(r'^rank3/$', kosdaq_up),
    url(r'^rank4/$', kosdaq_down),

    url(r'^token_check/$', token_check),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]