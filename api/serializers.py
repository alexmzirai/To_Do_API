from rest_framework import serializers
from todos import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        # the meta class just holds the fields and the name of the model
        fields = (
            'id',
            'title',
            'description',
        )

        model = models.Todo
