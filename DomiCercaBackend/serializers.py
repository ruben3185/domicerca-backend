from rest_framework import serializers
from rest_framework.fields import empty


class AuditSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def perform_create(self, serializer):
        req = serializer.context['request']
        serializer.save(created_by=req.user)

    class Meta:
        fields = '__all__'