from rest_framework import serializers

from job.models import Job


class JoSerializer(serializers.ModelSerializer):
    class Meta :
        model =Job
        fields ='__all__'