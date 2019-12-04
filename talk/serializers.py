from rest_framework import serializers
from talk.models import Talk

class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talk
        fields = ('id','content')

    def create(self, validated_data):
        return Talk.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance