from .forms import UploadFileForm

from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

import os


def downloadFile(request, param):
    print(f"[downloadFile] param (File Name) : {param}")
    # Download file
    BASE_DIR = os.getcwd()
    file_path = os.path.abspath(BASE_DIR)
    file_name = os.path.basename(param)
    fs = FileSystemStorage(file_path)
    response = FileResponse(fs.open(file_name, 'rb'),
                            content_type='video/mp4')
    response['Content-Disposition'] = f'attachment; filename="{param}"'

    return response


@ensure_csrf_cookie
def upload_display_video(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            handle_uploaded_file(file)

            # Remove existing folders (runs/detect/)
            cmd = f"rm -rf ../yolov3/runs/detect/"
            os.system(cmd)

            # Detection
            cmd = f"python ../yolov3/detect.py --source {file.name}"
            cmd_weights = ' --weights 0505_epoch_46.pt'

            # cmd = cmd + cmd_weights
            cmd = cmd + cmd_weights
            os.system(cmd)
            response = {}
            response['filename'] = file.name

            # Move video file
            file_name_output = f"{(file.name).split('.')[0]}_output.mp4"
            cmd_mv = f"mv ../yolov3/runs/detect/exp/{file.name} ./{file_name_output}"
            os.system(cmd_mv)
            response['filename_output'] = file_name_output

            return render(request, "index.html", response)
    else:
        form = UploadFileForm()

    return render(request, 'index.html', {'form': form, 'filename_output': 'test'})


def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
