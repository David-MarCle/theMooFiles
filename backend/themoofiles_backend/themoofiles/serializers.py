from rest_framework import serializers
from themoofiles.models import Abductions


class AbductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abductions
        fields = ('id', 'latitude', 'longitude', 'name', 'place', 'description', 'photo')