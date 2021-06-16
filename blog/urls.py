from django.urls import path
from django.urls.conf import include
from .views import ArticleViewSet, UserViewSet
from rest_framework.routers import DefaultRouter


# ArticleList, ArticleDetails
# article_details, article_list



router = DefaultRouter()
router.register('articles', ArticleViewSet, basename= 'articles')
router.register('users', UserViewSet)
urlpatterns = [
    path ('blog/', include(router.urls)),
    # path('articles/', ArticleList.as_view()),
    # path('articles/<int:id>/', ArticleDetails.as_view())

    # path('articles/', article_list),
    # path('articles/<int:pk>/', article_details),   
]