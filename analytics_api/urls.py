from django.conf.urls import url
from django.contrib import admin
from archives import views as api_views
from archives import view_reports as unit_report

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^battalion/$', api_views.BattalionView.as_view({
        'get':'list'
    })),
    url(r'^battalion/(?P<pk>[0-9a-z-]+)/$', api_views.BattalionView.as_view({
        'get': 'retrieve'
    })),
    url(r'^post/(?P<pk>[0-9a-z-]+)/$', api_views.PostView.as_view({
        'get': 'retrieve'
    })),
    url(r'^morcha/(?P<pk>[0-9a-z-]+)/$', api_views.MorchaView.as_view({
        'get': 'retrieve'
    })),
    url(r'^intrusion/morcha/(?P<pk>[0-9a-z-]+)/day/(?P<date>\d{4}-\d{2}-\d{2})/$', api_views.MorchaDayView.as_view({
        'get': 'retrieve'
    })),
    url(r'^intrusion/morcha/(?P<pk>[0-9a-z-]+)/week/(?P<date>\d{4}-\d{2}-\d{2})/$', api_views.MorchaWeekView.as_view({
        'get': 'retrieve'
    })),
    url(r'^intrusion/morcha/(?P<pk>[0-9a-z-]+)/month/(?P<date>\d{4}-\d{2}-\d{2})/$', api_views.MorchaMonthView.as_view({
        'get': 'retrieve'
    })),
    url(r'^intrusion/post/(?P<pk>[0-9a-z-]+)/recent/$', api_views.PostRecentView.as_view({
        'get': 'retrieve'
    })),
    url(r'^intrusion/post/(?P<pk>[0-9a-z-]+)/day/(?P<date>\d{4}-\d{2}-\d{2})/$', api_views.PostDayView.as_view({
        'get': 'retrieve'
    })),
    url(r'^intrusion/post/(?P<pk>[0-9a-z-]+)/week/(?P<date>\d{4}-\d{2}-\d{2})/$', api_views.PostWeekView.as_view({
        'get': 'retrieve'
    })),
    url(r'^intrusion/post/(?P<pk>[0-9a-z-]+)/month/(?P<date>\d{4}-\d{2}-\d{2})/$', api_views.PostMonthView.as_view({
        'get': 'retrieve'
    })),
    url(r'^intrusion/battalion/(?P<pk>[0-9a-z-]+)/recent/$', api_views.BattalionRecentView.as_view({
        'get': 'retrieve'
    })),
    url(r'^intrusion/battalion/(?P<pk>[0-9a-z-]+)/week/(?P<date>\d{4}-\d{2}-\d{2})/$', api_views.BattalionWeekView.as_view({
        'get': 'retrieve'
    })),
    url(r'^intrusion/battalion/(?P<pk>[0-9a-z-]+)/month/(?P<date>\d{4}-\d{2}-\d{2})/$', api_views.BattalionMonthView.as_view({
        'get': 'retrieve'
    })),
    url(r'^intrusion/dashboard/battalion/$', api_views.BattalionDashboardView.as_view({
        'get': 'retrieve'
    })),

    url(r'^unit/morcha/(?P<pk>[0-9a-z-]+)/day/(?P<date>\d{4}-\d{2}-\d{2})/$', unit_report.MorchaDayView.as_view({
        'get': 'retrieve'
    })),
    url(r'^unit/morcha/(?P<pk>[0-9a-z-]+)/week/(?P<date>\d{4}-\d{2}-\d{2})/$', unit_report.MorchaWeekView.as_view({
        'get': 'retrieve'
    })),
    url(r'^unit/morcha/(?P<pk>[0-9a-z-]+)/month/(?P<date>\d{4}-\d{2}-\d{2})/$', unit_report.MorchaMonthView.as_view({
        'get': 'retrieve'
    })),
    url(r'^unit/post/(?P<pk>[0-9a-z-]+)/day/(?P<date>\d{4}-\d{2}-\d{2})/$', unit_report.PostDayView.as_view({
        'get': 'retrieve'
    })),
    url(r'^unit/post/(?P<pk>[0-9a-z-]+)/week/(?P<date>\d{4}-\d{2}-\d{2})/$', unit_report.PostWeekView.as_view({
        'get': 'retrieve'
    })),
    url(r'^unit/post/(?P<pk>[0-9a-z-]+)/month/(?P<date>\d{4}-\d{2}-\d{2})/$', unit_report.PostMonthView.as_view({
        'get': 'retrieve'
    })),
    url(r'^unit/post/(?P<pk>[0-9a-z-]+)/live/$', unit_report.PostLiveView.as_view({
        'get': 'retrieve'
    })),
    url(r'^unit/battalion/(?P<pk>[0-9a-z-]+)/live/$', unit_report.BattalionLiveView.as_view({
        'get': 'retrieve'
    })),


    url(r'^insert/$', api_views.insert),
    url(r'^test/$', api_views.test)
]