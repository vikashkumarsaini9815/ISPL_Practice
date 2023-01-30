from rest_framework.views import APIView
import json
from django.http import JsonResponse
from rest_framework.response import Response
from ISPL_app.models import Student, Team
from rest_framework import status
from ISPL_app.serializer import *
from django.http import Http404 
from django.core.serializers import serialize
from django.core.exceptions import ObjectDoesNotExist
import  traceback

# Create your views here.


class All_infoAPIView(APIView):
    def get (self, request, format = None):
        file = open("ISPL_data.json","r")
        x = file.read()
        reference_data = json.loads(x)
        return Response(reference_data)



class Add_StudentAPIView(APIView):
    def post (self, request, format = None):
        data = request.data
        team_id = data["team_id"]
        try:
            return Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            raise Http404
    def post (self, request, format = None):
        data = request.data
        try:
            team_id = data["team_id"]
            name = data["name"]
            contact = data["contact"]
            email = data["email"]
            school_name = data["school_name"]
            address = data["address"]
            is_lead = data["is_lead"]

            try:
                student = Student.objects.get(contact=contact)
                return Response({"message":"This contact alredy exist"})
            except:

                T1 = Team.objects.get(id=team_id)
                S1 = Student(name=name, contact=contact, email=email, school_name=school_name, address=address,is_lead = is_lead)
                S1.save()
                T1.student.add(S1)
                print(traceback.format_exc())        
                response = {"success":"Students Successfully Add"}
                print(traceback.format_exc()) 
                return Response(response, status=status.HTTP_200_OK)
                       
                
        except KeyError:
            print(traceback.format_exc())
            return Response({"success":"BAD Request"},status=status.HTTP_400_BAD_REQUEST)



class registration_GET_APIView(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request,pk, format=None):
        student = self.get_object(pk=pk)
        #student = Student.objects.get(pk = pk)
        team = Team.objects.filter(student = student)
        serializer = serialize("json",team)
        data = serializer
        student_data = {}
        y = json.loads(data)
        for idx, ee in enumerate(y):
            list1 =[]
            student_id_hold =ee["fields"]["student"]
            for stu in student_id_hold:
                S = Student.objects.get(pk = stu)
                student_data = {
                    "id":S.id,
                    "name":S.name,
                    "contact":S.contact,
                    "email":S.email,
                    "school_name":S.school_name,
                    "address":S.address,
                    "create_time":S.create_time,
                    "update_time":S.update_time,
                    "is_lead":S.is_lead
                }
                list1.append(student_data)
            
        y[idx]["fields"]["student"] = list1
        response = {"Data":y}
        return Response(response)



class RegistrationAPIView(APIView):
    def post (self, request, format = None):
        data = request.data
        print("Team Data...............",data)
        try:
        
            # data = request.data
            # print(data)
            team_name = data["team_name"]
           # print("team ....",team_name)
            project_idea = data["project_idea"]
            print("project.....",project_idea)
            project_discrapition = data["project_discrapition"]
            try:
                T1 = Team(team_name=team_name, project_idea=project_idea, project_discrapition=project_discrapition)
                T1.save()
                student = data["students"]
               # print(student)
                for ele in student:
                    print("student..............",ele)
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
                print(traceback.format_exc())        
                response = {"success": " " + team_name + " Team are all ready exist "}
                return Response(response)

        except KeyError:
            print(traceback.format_exc())
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
            response = {"message":"Please choose correct key and check request data"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
