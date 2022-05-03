from django.shortcuts import render
from .forms import UploadFileForm
from django.views.decorators.csrf import ensure_csrf_cookie
import torch
import os

from django.http import FileResponse
from django.core.files.storage import FileSystemStorage


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
            # print(file.name)
            handle_uploaded_file(file)

            # model 적용 시도
            # model = torch.hub.load(
            #     'ultralytics/yolov3', 'custom', path='0502_epoch_100.pt', force_reload=True)
            # xmin, ymin, xmax, ymax, confidence, class_num, name = model(
            #     "IMG_4485.PNG").pandas().xyxy[0].values.tolist()[0]

            # Remove existing folders (runs/detect/)
            cmd = f"rm -rf ../yolov3/runs/detect/"
            returned_value = os.system(cmd)

            # Detection
            cmd = f"python ../yolov3/detect.py --source {file.name}"
            cmd_weights = ' --weights 0502_epoch_100.pt'
            #cmd = cmd + cmd_weights
            returned_value = os.system(cmd)
            response = {}
            response['filename'] = file.name

            # Move video file
            file_name_output = f"{(file.name).split('.')[0]}_output.mp4"
            cmd_mv = f"mv ../yolov3/runs/detect/exp/{file.name} ./{file_name_output}"
            returned_value = os.system(cmd_mv)
            response['filename_output'] = file_name_output

            return render(request, "index.html", response)
            # return render(request, "upload-display-video.html", {
            #     'filename': file.name,
            #     'xmin': xmin,
            #     'ymin': ymin,
            #     'xmax': xmax,
            #     'ymax': ymax,
            #     'confidence': confidence,
            #     'class_num': class_num,
            #     'name': name,
            # })
    else:
        form = UploadFileForm()

    return render(request, 'index.html', {'form': form, 'filename_output': 'test'})


def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
