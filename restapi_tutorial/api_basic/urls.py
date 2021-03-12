from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, \
    GenericAPIView, ArticleViewSet

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:id>/', include(router.urls)),

    #path('listall/', article_list),
    path('listall/', ArticleAPIView.as_view()),
    path('generic/listall/<int:id>/', GenericAPIView.as_view()),

    #path('articleinfo/<int:article_id>/', article_detail)
    path('articleinfo/<int:article_id>/', ArticleDetails.as_view())
]