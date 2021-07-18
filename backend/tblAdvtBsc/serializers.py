from rest_framework import serializers
from .models import tblAdvtBsc

class tblAdvtBscSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'AdvtNo',
            'AdvtTpCd',
        )
        model = tblAdvtBsc