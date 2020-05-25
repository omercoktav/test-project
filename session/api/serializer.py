from django.db.models.signals import pre_save
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from session.models import Session


class SessionCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model=Session
        fields=[
            'name',
            'start_date',
            'end_date',
            'speaker'
        ]

    def check_date(sender, instance, *args, **kwargs):
        if instance.start_date > instance.end_date:
            raise serializers.ValidationError('Start date must be less than end date')

    pre_save.connect(check_date, sender=Session)

class SessionListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Session
        fields = [
            'id',
            'name',
            'start_date',
            'end_date',
            'speaker',
            'slug',
        ]

class SessionDetailSerializer(ModelSerializer):
    class Meta:
        model=Session
        fields=[
            'id',
            'name',
            'start_date',
            'end_date',
            'speaker',
            'slug'

        ]
