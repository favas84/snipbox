from rest_framework import serializers
from snippets.models import Tag, Snippet


class TagSerializer(serializers.ModelSerializer):
    """Serializer for handling tags."""

    class Meta:
        model = Tag
        fields = ["id", "title"]

    def to_internal_value(self, data):
        # Skip the uniqueness check during deserialization
        return data

class SnippetSerializer(serializers.ModelSerializer):
    """Serializer for handling snippets and linking them with tags."""

    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Snippet
        fields = ["id", "title", "note", "tags"]


    def create(self, validated_data):
        """
        Handles snippet creation and linking existing tags.
        Uses `get_or_create` to ensure unique tags.
        """

        tags_data = validated_data.pop("tags", [])
        snippet = Snippet.objects.create(**validated_data)

        user = self.context['request'].user

        defaults = dict(
            created_by=user, modified_by=user
        )

        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(
                title=tag_data["title"], defaults=defaults)
            snippet.tags.add(tag)

        return snippet

    def update(self, instance, validated_data):
        """
        Handles snippet updates and linking existing tags.
        """

        tags_data = validated_data.pop("tags", None)

        # Update snippet fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        user = self.context['request'].user

        defaults = dict(
            created_by=user, modified_by=user
        )

        # Update tags if provided
        if tags_data is not None:
            instance.tags.clear()
            for tag_data in tags_data:
                tag, _ = Tag.objects.get_or_create(
                    title=tag_data["title"], defaults=defaults)
                instance.tags.add(tag)

        return instance
