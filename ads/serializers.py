from rest_framework import serializers
from ads.models import Ad

# 2-07
class NameLenValid:
    def __call__(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Name is less then 10 chars")

# 2-07
class NotTrueValidator:
    def __call__(self, value):
        if value:
            raise serializers.ValidationError("New Ad cant be create")

# 2-07
class AdCreateSerializers(serializers.ModelSerializer):
    is_published = serializers.BooleanField(validators=[NotTrueValidator()])
    name = serializers.CharField(validators=[NameLenValid()])
    class Meta:
        model = Ad
        fields = '__all__'

class AdSerializer(serializers.ModelSerializer):
    author = serializers.CharField()
    category = serializers.CharField()
    class Meta:
        model = Ad                                                 # по умолчанию ВЫВОДИТ ИНДЕКС!
        fields = ["id", "name", "price", "description", "author", "category"]

'''
class AdDetailSerializer(serializers.ModelSerializer):
    author = serializers.CharField()
    category = serializers.CharField()
    class Meta:
        model = Ad                                                 # ВЫВОДИТ ИНДЕКС!
        fields = '__all__'
'''
# 2-07
class AdDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='first_name',
        read_only=True,
    )

    class Meta:
        model = Ad                                                 # ВЫВОДИТ ИНДЕКС!
        fields = '__all__'