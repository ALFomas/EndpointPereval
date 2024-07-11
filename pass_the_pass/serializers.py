from rest_framework import serializers
from .models import User, Coord, Level, Image, Camping, CampingImage


class UserSerializer(serializers.ModelSerializer):
    """ Serializer for User model"""

    class Meta:
        """Meta class"""
        model = User
        fields = '__all__'


class CoordSerializer(serializers.ModelSerializer):
    """ Serializer for Coord model"""

    class Meta:
        """Meta class"""
        model = Coord
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    """ Serializer for Level model"""

    class Meta:
        """Meta class"""
        model = Level
        fields = '__all__'


class CampingSerializer(serializers.ModelSerializer):
    """ Serializer for Camping model"""
    user = UserSerializer()
    coord = CoordSerializer()
    level = LevelSerializer()

    class Meta:
        """Meta class"""
        model = Camping
        fields = '__all__'

    def create(self, validated_data):
        """serializer create method """
        user_data = validated_data.pop('user')
        coord_data = validated_data.pop('coord')
        level_data = validated_data.pop('level')

        user_instance = User.objects.create(**user_data)
        coord_instance = Coord.objects.create(**coord_data)
        level_instance = Level.objects.create(**level_data)

        camping_instance = Camping.objects.create(
            user=user_instance,
            coord=coord_instance,
            level=level_instance,
            **validated_data
        )

        return camping_instance


class ImageSerializer(serializers.ModelSerializer):
    """ Serializer for User Image"""

    class Meta:
        """Meta class"""
        model = Image
        fields = '__all__'


class CampingImageSerializer(serializers.ModelSerializer):
    """ Serializer for CampingImage model"""

    class Meta:
        """Meta class"""
        model = CampingImage
        fields = '__all__'
