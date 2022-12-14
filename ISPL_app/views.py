from rest_framework.views import APIView
import json
from rest_framework.response import Response
from ISPL_app.models import Student, Team
from rest_framework import status

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
                T1 = Team(team_name=team_name, project_idea=project_idea, project_discrapition=project_discrapition)
                T1.save()
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
                    T1.student.add(S1)
                
                response = {"success":True}
                return Response(response,status=status.HTTP_200_OK)

            except:
                        
                response = {"success": " " + team_name + " Team are all ready exist "}
                return Response(response)

        except KeyError:
            return Response({"success":False},status=status.HTTP_400_BAD_REQUEST)




class Registration_updateAPIView(APIView):
    def put(self, request, format=None):
        
        
        try:
            data = request.data
            id = data["id"] 
            team_name = data["team_name"]
            project_idea = data["project_idea"]
            project_discrapition = data["project_discrapition"]
            student_data = data["students"]
            try:
                T2 = Team.objects.get(id = id)
                T2.team_name = team_name
                T2.project_idea = project_idea
                T2.project_discrapition = project_discrapition
                T2.save()
                for ele in student_data:
                    id = ele["id"]
                    contact = ele["contact"]
                    name = ele["name"]
                    email = ele["email"]
                    school_name = ele["school_name"]
                    address = ele["address"]
                    is_lead = ele["is_lead"]
                    S = Student.objects.get(id = id)
                    S.name = name
                    S.contact = contact
                    S.email = email    
                    S.school_name = school_name
                    S.address = address
                    S.is_lead = is_lead
                    S.save()
                response = {"success":True, "message":"update data successfully"}
                return Response(response,status=status.HTTP_200_OK)
            except:
                response = {"success":False, "message":"data not update"}
                return Response(response)

        except KeyError:
            response = {"message":"Please choose correct key"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
