# from backend.views import PaperCreateView
from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserAPI #UploadPDFAPI
from .views import PaperCreateView, PaperListView, CreateProjectView, ProjectDetailView , NoteCreateView, NoteDetailView    
from knox import views as knox_views

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api/auth/pdf_upload', PaperCreateView.as_view()),
    path('api/auth/paper_detail/', PaperListView.as_view()),
    path('api/auth/create_note', NoteCreateView.as_view()),
    path('api/auth/note_detail', NoteDetailView.as_view()),
    path('api/auth/create_project', CreateProjectView.as_view()),
    path('api/auth/project_detail/', ProjectDetailView.as_view()),
    ]