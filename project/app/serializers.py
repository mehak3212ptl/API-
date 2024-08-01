from rest_framework import serializers
from .models import StudentModel

# class StudentSerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=45)
#     city=serializers.CharField(max_length=42)
#     roll=serializers.IntegerField()

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return StudentModel.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.name = validated_data.get('title', instance.name)
    #     instance.city = validated_data.get('code', instance.city)
    #     instance.roll = validated_data.get('linenos', instance.roll)

# ---------------------------------second type of writting serializers -----------------

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentModel
        fields =["id","name","city","roll"]