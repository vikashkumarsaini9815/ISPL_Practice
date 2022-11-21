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
                    S1 = Student(name=name, contact=contact, email=email, school_name=school_name, address=address)
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




        