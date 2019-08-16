from django.urls import path

from commandments_app.views.demo_view import DemoView
from commandments_app.views.detail_view import DetailView
from commandments_app.views.index_view import IndexView
from commandments_app.views.listing_view import ListingView
from commandments_app.views.study_listing_view import StudyListingView


app_name = 'commandments'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('demo', DemoView.as_view(), name='demo'),
    path('listing', ListingView.as_view(), name='listing'),
    path('study_listing', StudyListingView.as_view(), name='study_listing'),
    path('detail/<int:commandment_id>/', DetailView.as_view(), name='detail'),
]
