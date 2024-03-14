from django.urls import path
from themoofiles.views import AbductionListAPIView


urlpatterns = [
path('abductions/', AbductionListAPIView.as_view())
]