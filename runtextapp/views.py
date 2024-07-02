from django.http import FileResponse
import cv2
import numpy as np
from .models import Request
import os

def create_runtext(request):
    text = request.GET.get('text', 'default')
    Request.objects.create(text=text)

    width, height = 100, 100

    out = cv2.VideoWriter("runtext.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 24, (width, height))

    frame = np.zeros((height, width, 3), dtype=np.uint8)

    pink_color = np.array([255, 105, 255], dtype=np.uint8)


    x, y = width, height // 2

    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1
    font_thickness = 2
    font_color = (255, 255, 255)

    for t in range(72): 
        frame[:] = pink_color

        x -= 10

        cv2.putText(frame, text, (x, y), font, font_scale, font_color, font_thickness)

        out.write(frame)

    out.release()
    video_path = "runtext.mp4"
    video_file = open(video_path, 'rb')
    response = FileResponse(video_file, as_attachment=True, filename=os.path.basename(video_path))

    return response
