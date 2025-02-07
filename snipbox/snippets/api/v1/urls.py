from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets.api.v1.views import SnippetViewSet, TagListAPI, TagDetailAPI

router = DefaultRouter()
router.register(r"snippets", SnippetViewSet, basename='snippets')
urlpatterns = [
    path("", include(router.urls)),
    path("tags/", TagListAPI.as_view(), name="tag_list"),
    path("tags/<int:pk>/", TagDetailAPI.as_view(), name="tag_detail"),
]
