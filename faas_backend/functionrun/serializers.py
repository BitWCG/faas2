from rest_framework import serializers

from functionrun.models import RunPath
import subprocess
import os


class RunPathSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField('runpath-detail')
    # test = serializers.CharField(max_length=50,write_only=True)
    class Meta:
        model = RunPath
        fields = '__all__'

    def to_internal_value(self, data):
        print(data['path'])
        raw_path = data['path'].split('/')
        function_path = '\\'.join(raw_path[3:])
        run_path = os.getcwd()+'\\'+function_path
        print('raw_path',raw_path)
        print('function_path',function_path)
        print('run_path',run_path)
        # path = 'functionrun/tests.py'
        # popen = subprocess.Popen('python '+os.getcwd()+'\\'+path)
        popen = subprocess.Popen('python '+run_path)
        print('popen',popen)
        return super().to_internal_value(data)
