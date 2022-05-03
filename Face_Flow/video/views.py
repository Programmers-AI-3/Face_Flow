from django.shortcuts import render
from .forms import UploadFileForm
from django.views.decorators.csrf import ensure_csrf_cookie
import os


@ensure_csrf_cookie
def upload_display_video(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']

            handle_uploaded_file(file)

            cmd = f"python ../../yolov3/detect.py --weights ../../0502_epoch_100.pt --source {file.name}"
            _ = os.system(cmd)

            return render(request, "index.html", {'filename': file.name})
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})


def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)