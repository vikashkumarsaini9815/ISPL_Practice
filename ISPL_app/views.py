from rest_framework.views import APIView
import json
from rest_framework.response import Response
from ISPL_app.models import Student, Team
from rest_framework import status
from ISPL_app.serializers import *

# Create your views here.


class All_infoAPIView(APIView):
    def get (self, request, format = None):
        file = open("ISPL_data.json","r")
        x = file.read()
        reference_data = json.loads(x)
        return Response(reference_data)


class registration_GET_APIView(APIView):
    def get (self, request, format = None):
        file = open("registration_data.json","r")
        x = file.read()
        reference_data = json.loads(x)
        return Response(reference_data)


class RegistrationAPIView(APIView):
    def post (self, request, format = None):
        try:
        
            data = request.data
            team_name = data["team_name"]
            project_idea = data["project_idea"]
            project_discrapition = data["project_discrapition"]
            try:
                # T1 = Team(team_name=team_name, project_idea=project_idea, project_discrapition=project_discrapition)
                # T1.save()
                student = data["students"]
                for ele in student:
                    name = ele["name"]
                    contact = ele["contact"]
                    email = ele["email"]
                    school_name = ele["school_name"]
                    address = ele["address"]
                    is_lead = ele["is_lead"]
                    S1 = Student(name=name, contact=contact, email=email, school_name=school_name, address=address,is_lead = is_lead)
                    S1.save()
                T1 = Team(team_name=team_name, project_idea=project_idea, project_discrapition=project_discrapition)
                T1.save()
                response = {"success":True}
                return Response(response,status=status.HTTP_200_OK)

            except:
                        
                response = {"success": "This contact Number all ready exist"}
                return Response(response)

        except KeyError:
            return Response({"success":False},status=status.HTTP_400_BAD_REQUEST)




# class Registration_updateAPIView(APIView):
#     def put(self, request, format=None):
#         data = request.data
#         team_name = data["team_name"]
#         project_idea = data["project_idea"]
#         project_discrapition = data["project_discrapition"]
#         Te = Team.objects.get(team_name = team_name)
#         serializer = TeamSerializer(Te, many = True)
#         all_data = serializer.data
#         T1 = Team(team_name=team_name, project_idea=project_idea, project_discrapition=project_discrapition)
#         T1.save()
#         for i in all_data:
#             aa = i["student"]
#             length = len(aa)
#             print(length)
#             if length <= 6:
#                 # T1 = Team(team_name=team_name, project_idea=project_idea, project_discrapition=project_discrapition)
#                 # T1.save()
#                 student = data["students"]
#                 for ele in student:
#                     name = ele["name"]
#                     contact = ele["contact"]
#                     email = ele["email"]
#                     school_name = ele["school_name"]
#                     address = ele["address"]
#                     is_lead = ele["is_lead"]
#                     S1 = Student(name=name, contact=contact, email=email, school_name=school_name, address=address,is_lead = is_lead)
#                     S1.save()
#                 # T1 = Team(team_name=team_name, project_idea=project_idea, project_discrapition=project_discrapition)
#                 # T1.save()
#                 response = {"success":True}
#                 return Response(response, status=status.HTTP_201_CREATED)
#     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class Registration_updateAPIView(APIView):
#     def put(self, request, format = None):
#         data = request.data
#         team_name = data["team_name"]
#         project_idea = data["project_idea"]
#         project_discrapition = data["project_discrapition"]
#         T1 = Team.objects.filter(team_name=team_name)
#         serializer = TeamSerializer(T1, many = True)
#         all_data = serializer.data
#         for i in all_data:
#             aa = i["student"]
#             length = len(aa)
#             print(length)
#             if length <= 6:
#                 print("ff")
#         return Response("hogya")


