from core.settings import MEDIA_ROOT, MEDIA_URL
from django.conf import settings
from django.shortcuts import redirect, render
import os

import PyPDF2
from django.core.files.storage import FileSystemStorage
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from apiclient.discovery import build
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

API_KEY = "AIzaSyDAT4w2gVsDI0RJc35wVoBE71ouMbl2Zv4"


# this view is for fetching the data from youtube api
@api_view(('GET',))
def snippet_list(request, qu):
    yt = build('youtube', 'v3', developerKey = API_KEY)
    req = yt.search().list(q = qu, part='snippet', type='video', maxResults=10)
    res = req.execute()
    res_dict = []
    for item in res['items']:
        temp = {}
        temp["id"] = item['id']['videoId']
        temp["title"] = item['snippet']["title"]
        res_dict.append(temp)

        # res_dict['id'].append(item['id'])
        # res_dict["data"].append(item["snippet"])
    res_dict = {'videos': res_dict}
    return Response(res_dict)


#This returns the null set as default.
@api_view(('GET',))
def get_default(request):
    res_dict = {'videos': None}
    return Response(res_dict)


def get_pdf(request):
    if request.method == 'POST' and request.FILES['myFile']:
        myfile = request.FILES['myFile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        pdftotxt = open(MEDIA_ROOT+"1.pdf", 'rb')
        pdfreader=PyPDF2.PdfFileReader(pdftotxt)
        x=pdfreader.numPages
        pageobj=pdfreader.getPage(x+1)
        text=pageobj.extractText()
        file = fs.save("hello.txt", text)
        pdftotxt.close()
        


        return HttpResponsePermanentRedirect(reverse('frontend:home_page'))
