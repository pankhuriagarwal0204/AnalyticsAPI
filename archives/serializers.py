from rest_framework import serializers
from models import *

class GeospaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geospace
        fields = ('latitude', 'longitude')


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('repr', )


class MorchaSerializer(serializers.ModelSerializer):
    geospace = GeospaceSerializer()
    qrt_id = DeviceSerializer()
    units = DeviceSerializer(many=True)
    class Meta:
        model = Morcha
        fields = ('name', 'geospace', 'uuid', 'qrt_id', 'units', )


class PostMorchaSerializer(serializers.ModelSerializer):
    morchas = MorchaSerializer(many=True, read_only = True)
    geospace = GeospaceSerializer()
    class Meta:
        model = Post
        fields = ('name', 'geospace', 'uuid', 'morchas', )


class PostNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('name', 'uuid')


class BattalionSerializer(serializers.ModelSerializer):
    geospace = GeospaceSerializer()
    posts = PostNameSerializer(many=True)
    class Meta:
        model = Morcha
        fields = ('name', 'geospace', 'uuid', 'posts')


class IntrusionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intrusion
        fields = ('detected_datetime', 'verified_datetime', 'neutralized_datetime',
                  'non_human_intrusion_datetime', 'duration')


class MorchaNameSerializer(serializers.ModelSerializer):
    post = PostNameSerializer()
    class Meta:
        model = Morcha
        fields = ('name', 'uuid', 'post')


class LongestIntrusionSerializer(serializers.ModelSerializer):
    morcha = MorchaNameSerializer()
    class Meta:
        model = Intrusion
        fields = ('detected_datetime', 'verified_datetime', 'neutralized_datetime',
                  'non_human_intrusion_datetime', 'duration', 'morcha', 'morcha')



