import csv

from django.shortcuts import render
from django.views.generic import CreateView

from .forms import UploadFileForm
from .models import Upload


class UploadCreateView(CreateView):
    model = Upload
    form_class = UploadFileForm
