from decimal import Context
from os import name, read
from .models import Paper, Project, Note
from rest_framework import fields, serializers, generics, permissions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


#User Serializer        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password':{'write_only':True}}

#Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username', 'email','password')
            extra_kwargs ={'password':{'write_only':True}}

        def create(self, validated_data):
            user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
            return user

#Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

#Serializer for upload Paper
class UploadPDFSerializer(serializers.ModelSerializer):
    # owner = serializers.PrimaryKeyRelatedField(
    #     read_only = True
    # )
    owner = serializers.ReadOnlyField(source='owner.username')

    # def create(self, validated_data):
    #     paper = Paper.objects.create(owner=self.context['request'].user,
    #                              **validated_data)
    #     return paper
    class Meta:
        model = Paper
        fields = ("file_Name", "owner", "paper", "created_at")
        
#Serializer for paper list
class ViewPaperSerializer(serializers.ModelSerializer):

    class Meta:

        model = Paper
        fields = ("file_Name", "owner", "paper", "created_at")

#Serializer for upload Note
class UploadNoteSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    related_to = serializers.PrimaryKeyRelatedField(read_only=True)
    project = serializers.PrimaryKeyRelatedField(read_only=True)
    # owner = serializers.ReadOnlyField(source='owner.username')
    # related_to = serializers.ReadOnlyField()
    # project = serializers.ReadOnlyField()
    # project_title = serializers.CharField()
    # paper_name = serializers.CharField()
    

    def create(self, validated_data):
        # name1=validated_data.get('project_title',None)
        # file_Name1=validated_data.get('paper_name', None)
        # if(name1 == None):
        #     print("name is NULL")
        #     return
        # if(file_Name1 == None):
        #     print("file Name 1 is NULL")
        #     return    
        project = Project.objects.filter(owner=self.context['request'].user).filter(name=self.context['request'].data.get('project_title')).first()
        paper = Paper.objects.filter(owner=self.context['request'].user).filter(file_Name=self.context['request'].data.get('paper_name')).first() 
        # project = Project.objects.filter(owner=self.context['request'].user).filter(name=name1).first()
        # paper = Paper.objects.filter(owner=self.context['request'].user).filter(file_Name=file_Name1).first()  
        if project == None or paper == None:
            return {""}
        note = Note.objects.create(title = validated_data['title'], note = validated_data['note'],
                                    owner = self.context['request'].user,
                                    project = project,
                                    related_to = paper)
        return note

    class Meta:
        model = Note
        fields = ("title", "note", "owner","project", "related_to")


class CreateProjectSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
  

    class Meta:
        model = Project
        fields = ("name", "owner", "created_at")


class ProjectDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ("name","owner", "created_at")

class NoteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("title", "note", "owner","project", "related_to")