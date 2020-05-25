from django.contrib.auth import authenticate,login
from django.db.models.signals import pre_save
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from Event.models import Session,Event
from rest_framework import exceptions

class EventUpdateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields = [
            'name',
            'start_date',
            'end_date',
            'timezone',
            'session'
        ]
        def check_date(sender, instance, *args, **kwargs):
            if instance.start_date > instance.end_date:
                raise serializers.ValidationError('Start date must be less than end date')
        pre_save.connect(check_date, sender=Event)
class EventListSerializer(serializers.ModelSerializer):
    session_name = serializers.SerializerMethodField(method_name='session_name_method')
    class Meta:
        model=Event
        fields = [
            'id',
            'name',
            'start_date',
            'end_date',
            'timezone',
            'session_name',
        ]

    def session_name_method(self, obj):
        return str(obj.session.name)
class EventDetailSerializer(ModelSerializer):
    class Meta:
        model=Event
        fields=[
            'id',
            'name',
            'start_date',
            'end_date',
            'timezone',
            'session_name',
            'slug',
        ]









