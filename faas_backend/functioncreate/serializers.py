from rest_framework import serializers

from .models import FunctionCreate, FunctionFile

import os


class FunctionFileSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='functionfile-detail')

    class Meta:
        model = FunctionFile
        fields = '__all__'


class FunctionSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='functioncreate-detail')
    file = FunctionFileSerializer(read_only=True)
    file_id = serializers.IntegerField(
        write_only=True,
        allow_null=True,
        required=False
    )
    def validate_avatar_id(self, value):
        if not FunctionFile.objects.filter(id=value).exists() and value is not None:
            raise serializers.ValidationError("Avatar with id {} not exists.".format(value))

        return value

    class Meta:
        model = FunctionCreate
        fields = '__all__'

    # def to_internal_value(self, data):
    #     tags_data = data['file_id']
    #     a = tags_data.read()
    #     os.system('cd upload && cd 20220317 && python test.py')
    #     print(a)
    #     print(tags_data.size)
    #     print(type(tags_data))
    #     print("afsdgr :", tags_data)
    #     return super().to_internal_value(data)



