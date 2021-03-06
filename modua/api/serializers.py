from rest_framework import serializers
from .models import Definition, Language


class DefinitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Definition
        fields = ('word', 'translation', 'transliteration', 'id')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('language', 'id')
