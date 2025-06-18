from django.shortcuts import render,get_object_or_404
from students.models import Student,Teachers
from .serializers import StudentSerializer,TeacherSerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import *
from django.http import Http404
from blogs.models import *
from rest_framework import generics,viewsets,mixins
from blogs.serializer import *
from .pagination import CustomPagination
from employees.filters import EmployeeFilter
from rest_framework.filters import SearchFilter,OrderingFilter
"""
1) function based view
2) class based view
3)MIXINS 
4) generics
"""
# # generics use , simple and less code
# class Employees(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
 
# class Employee_detail(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field = 'pk'
    
# BY VIEWSETS
# class EmployeeViewSet(viewsets.ViewSet):
#     def list(self,request):
#         queryset = Employee.objects.all()
#         serializer = EmployeeSerializer(queryset,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def create(self,request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def retrieve(self,request,pk):
#         employee = get_object_or_404(Employee,pk=pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     def update(self,request,pk):
#         employee = get_object_or_404(Employee,pk=pk)
#         serializer = EmployeeSerializer(employee)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         employee = get_object_or_404(Employee,pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination
    filterset_class = EmployeeFilter
    
    

class BlogView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends={SearchFilter,OrderingFilter}
    search_fields = ['blog_title','blog_body']
    ordering_fields = {'id'}
    

class BlogDetailView(generics.DestroyAPIView,generics.UpdateAPIView,generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommnetSerializer
    
class CommentDetailView(generics.DestroyAPIView,generics.RetrieveAPIView,generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommnetSerializer
    lookup_field = 'pk'



"""
PageNumberPagination => takes the page size as 10 and returns the response
accordingly

LimitOffSetPagination = > takes two parameters
limit = > the parameter controls the count of items to see in a single page
offset = this parameter tells the API where to start fetching from
if offset = 0 => 1-10 and limit is 10
offset = 10 => 11-20 and limit is 10

"""





































"""
# Create your views here.
from django.http import JsonResponse
from rest_framework import mixins,generics
#MIXINS
class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class =  EmployeeSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
#MIXINS    
class Employee_detail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class =  EmployeeSerializer
    
    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)
        
#MIXINS
class studentView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
#MIXINS    
class studentDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)
"""
    
    
    
  
"""
  GENERIC API VIEWS
  ListAPIView
  CreateAPIView
  RetrieveAPIView
  UpdateAPIView
  DestroyAPIView 
  can have combo of all the API view also
  """  

"""
THESE ARE FUCNTION BASED VIEWS AND CLASS BASED VIEWS FOR NOTES
@api_view(['GET','POST','PUT'])
def studentView(request):
    
    # students = Student.objects.all() # this returns a query set and we need to serializze or convert 
    # # it into list to pass it
    # student_list = list(students.values())
    
   #
    
        
    if(request.method == 'GET'):
        students = Student.objects.all()
        # many - true , indicating that the serailzer should be used for all the model values
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK) 
        
   
    elif request.method=='POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
            
    
    
    serialization=	Converts model/queryset (Python object) → JSON for API responses.
     deserialization = Converts JSON input (from request) → Python objects for validation and saving to the database.
    
@api_view(['GET','PUT','DELETE'])
def studentDetailView(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
         student.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
         

@api_view(['GET','POST'])
def teacherView(request):
    if(request.method == 'GET'):
        teachers=Teachers.objects.all()
        serializer = TeacherSerializer(teachers,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
def teacherDetailView(request,pk):
    try:
        teacher = Teachers.objects.get(pk=pk)
    except Teachers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data,status=status.HTTP_200_OK) 
    

class Employees(APIView): # no need to mention like function based view
    # class based view will automatically go to its respective method
    def get(self,request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class Employee_detail(APIView):
    def get_object(self,pk):
        try:
            employee = Employee.objects.get(pk=pk)
            return employee
        except Employee.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    # def get(self,request,em_id):
    #     employee = self.get_object(em_id)
    #     serializer = EmployeeSerializer(employee)
    #     return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


MIXINS : mixins are built in classes to handle 5 common fucntionalities
they are basically reusable code classes in OOP that provide special funcs

1)ListModelMIXIN => list all records
2)CreateModelMixin = > create a new record
3)retirewModelMixin => get a single record
4)UpdateModelMixin => update a record
5)DestroyModelMixin => delete a record


"""
        
        
    
            
        
    
    
        
        