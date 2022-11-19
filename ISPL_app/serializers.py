from rest_framework import serializers
from ISPL_app.models import Student,Team



class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'



class TeamSerializer(serializers.ModelSerializer):
    challenges=StudentSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        fields = '__all__'