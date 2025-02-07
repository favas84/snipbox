from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse

from snippets.api.v1.serializers import SnippetSerializer, TagSerializer
from snippets.models import Snippet, Tag


class TagListAPI(generics.ListAPIView):
    """
    Returns a list of all unique tags.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


class TagDetailAPI(generics.ListAPIView):
    """
    Returns all snippets linked to the selected tag.
    """
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        tag = get_object_or_404(Tag, id=self.kwargs["pk"])
        snippets = Snippet.objects.filter(tags=tag)
        return snippets


class SnippetViewSet(viewsets.ModelViewSet):
    model = Snippet
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_queryset(self):
        return self.model.objects.all()

    def perform_create(self, serializer):
        snippet = serializer.save(
            created_by=self.request.user, modified_by=self.request.user)
        return snippet

    def destroy(self, request, *args, **kwargs):
        snippet = self.get_object()
        snippet.delete()
        data = {
            "message": "Snippet {} deleted successfully.".format(snippet.title)
        }
        return Response(data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='overview',
            url_name='overview')
    def overview(self, request):
        """
        Returns the total snippet count and a list of snippets with hyperlinks.
        """
        snippets = self.get_queryset()
        snippet_data = [
            {
                "id": snippet.id,
                "title": snippet.title,
                "detail_url": reverse(
                    'snippet-api-v1:snippets-detail',
                    kwargs={'pk': snippet.pk}, request=request
                ),
            }
            for snippet in snippets
        ]

        data = {"total_snippets": snippets.count(), "snippets": snippet_data}

        return Response(data, status=status.HTTP_200_OK)
