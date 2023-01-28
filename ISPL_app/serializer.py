from rest_framework import serializers
from ISPL_app.models import Student,Team



class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    # student = StudentSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        fields = ['team_name','project_idea', 'project_discrapition','student']


# class StudentSerializer(serializers.ModelSerializer):
#     team = TeamSerializer(many=True, read_only=True)
#     class Meta:
#         model = Student
#         fields = ['id','name','contact','email','school_name','address','create_time','update_time','is_lead','team']