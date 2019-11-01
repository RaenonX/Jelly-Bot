from django.urls import path, include

from .index import HomePageView
from .about import AboutView
from .exctnt import ExtraContentView


urlpatterns = [
    path('', HomePageView.as_view(), name="page.home"),
    path('about/', AboutView.as_view(), name="page.about"),
    path('extra/<str:page_id>/', ExtraContentView.as_view(), name="page.extra"),
    path('account/', include('JellyBot.views.account.urls')),
    path('ar/', include('JellyBot.views.ar.urls')),
    path('doc/', include('JellyBot.views.doc.urls')),
    path('info/', include('JellyBot.views.info.urls'))
]
