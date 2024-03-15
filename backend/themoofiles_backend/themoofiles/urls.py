from django.urls import path
# from themoofiles.views import AbductionListAPIView
from themoofiles.views import AbductionViewSet
from rest_framework.routers import DefaultRouter

# urlpatterns = [
# path('abductions/', AbductionListAPIView.as_view())
# ]


router = DefaultRouter()
router.register('abductions', AbductionViewSet, basename='abductions')
urlpatterns = router.urls


# urlpatterns = [
#     path('films/', FilmListAPIView.as_view()), 
#     path('films/<int:pk>/', FilmDetailAPIView.as_view()) 
# ]