
from os import name
from PyPDF2.pdf import PdfFileReader
from django.db.models.query import QuerySet
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.fields import CurrentUserDefault
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import serializers, response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
# Create your views here.
from django.core.files.storage import FileSystemStorage
from .models import Paper , Project, Note
from .serializer import  UploadPDFSerializer, ViewPaperSerializer, CreateProjectSerializer, ProjectDetailSerializer, UploadNoteSerializer, NoteDetailSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class PaperCreateView(CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated,]
    serializer_class = UploadPDFSerializer
    # queryset = Paper.objects.all()
    
    # def perform_create(self, serializer):
    #     paper = Paper.objects.create(   
    #                              **serializer.data)
        

    # def get_serializer_context(self):
    #     return {"request": self.request}
    

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    

    # def post(self, request, format=None):
    #     # file_obj = request.FILES['file']
    #     # # do some stuff with uploaded file
    #     # fs = FileSystemStorage(location = '/media/papers')
    #     # fs.save(file_obj.name, file_obj)
    #     myfile = request.FILES['file']
    #     fs = FileSystemStorage()
    #     fs.save(myfile.name, myfile)
    #     #uploaded_file_url = fs.url(myfile)
    #     return response(status=204)   


class NoteCreateView(CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UploadNoteSerializer
    # def get_serializer_context(self):
    #     context = super(CommentViewSet, self).get_serializer_context()
    #     context.update({
    #         "exclude_email_list": ['test@test.com', 'test1@test.com']
    #         # extra data
    #     })
    #     return context

    # def perform_create(self, serializer):
        

    #     # project = Project.objects.filter(owner=self.request.user.id).filter(name=self.request.data.get('project_title')).first()
    #     # paper = Paper.objects.filter(owner=self.request.user.id).filter(file_Name=self.request.data.get('paper_name')).first()
    #     project = Project.objects.filter(owner=self.request.user).filter(name="First Project").first()
    #     paper = Paper.objects.filter(owner=self.request.user).filter(file_Name="PdfU2").first()
    #     if(project == None):
    #         return response("Nothing Created")
    #     if(paper == None):
    #         return response("Nothing Created")
    #     return serializer.save(owner=self.request.user, project = project, paper=paper)

    def get_serializer_context(self):
        return {"request": self.request}

class PaperListView(ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated,]
    serializer_class = ViewPaperSerializer
    
    filter_backends = [DjangoFilterBackend]

    filter_fields = ('file_Name',)
    def get_queryset(self):
        user = self.request.user
        return Paper.objects.filter(owner = user)

class CreateProjectView(CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated,]
    serializer_class = CreateProjectSerializer  
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ProjectDetailView(ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated,]

    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    filter_backends = [DjangoFilterBackend]

    filter_fields = ('name',)
    def get_queryset(self):
        user = self.request.user


        return Project.objects.filter(owner=user)


# note list view for viewing the list of notes
class NoteDetailView(ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated,]

    queryset = Note.objects.all()
    serializer_class = NoteDetailSerializer
    filter_backends = [DjangoFilterBackend]

    filter_fields = ('title',)
    def get_queryset(self):
        user = self.request.user


        return Note.objects.filter(owner=user)

