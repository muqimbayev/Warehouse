from rest_framework import serializers
from .models import *

class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'

class XomashyoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xomashyo
        fields = '__all__'

class Mahsulot_XomashyoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot_Xomashyo
        fields = '__all__'

class OmborxonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Omborxona
        fields = '__all__'