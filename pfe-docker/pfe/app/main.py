from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse
from starlette.testclient import TestClient

import os

import shutil
import paramiko
from enum import Enum


app = FastAPI(title='Deploying a ML Model with FastAPI')

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------ skinseg --------------------------------------------

@app.post("/batata")
async def batata():
    return {"batata"}

@app.post("/api/predict_skinseg")
async def predict_skinseg(file: UploadFile = File(...)):
    import app.skinseg
    # 0. VALIDATE INPUT FILE
    fileExtension = file.filename.split(".")[-1] in ("nii", "gz", "jpeg", "jpg", "png")
    if not fileExtension:
        raise HTTPException(status_code=415, detail="Unsupported file provided.")

    # 1. Upload images:
    file_location = f"/src/app/files/skinseg/inputs_skinseg/Nifti_inputs/{file.filename}"
    
    app.fileInputName = file.filename
    DATA_PATH_without_extention = file.filename.rsplit('.', 1)[0]
    print(DATA_PATH_without_extention)

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)  

    app.skinseg.predict_data(file_location, DATA_PATH_without_extention)  
    return {file.filename}


@app.get("/api/export_skinseg/{file_name}", responses={200: {"description": "A picture of a cat.", "content" : {"image/jpeg" : {"example" : "No example available. Just imagine a picture of a cat."}}}})
def export_skinseg(file_name):
    print(file_name)
    input_extention = ".nii.gz"
    output_jpeg_file_name = "Output_" + file_name + ".jpeg"
    output_nifti_file_name = "Output_" + file_name + ".nii.gz"
    path = "/src/app/files/skinseg/outputs_skinseg/JPEG_outputs/"
    file_path = os.path.join(path, output_jpeg_file_name)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="image/jpeg", filename=output_jpeg_file_name)
    return {"error" : "File not found!"}




# ------------------------------------------ yolov --------------------------------------------

# List available models using Enum for convenience. This is useful when the options are pre-defined.
class Model(str, Enum):
    yolov3tiny = "yolov3-tiny"
    yolov3 = "yolov3"


# This endpoint handles all the logic necessary for the object detection to work.
# It requires the desired model and the image in which to perform object detection.
@app.post("/api/predict_yolov") 
# def predict_yolov(model: Model, file: UploadFile = File(...)):
def predict_yolov(file: UploadFile = File(...)):

    # 0. VALIDATE INPUT FILE
    filename = file.filename
    fileExtension = filename.split(".")[-1] in ("jpg", "jpeg", "png", "mp4")
    if not fileExtension:
        raise HTTPException(status_code=415, detail="Unsupported file provided.")

    # 1. Upload images:
    file_location = f"/src/app/files/yolov/inputs_yolov/{filename}" 
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)  
    
    # import app.yolov3
    # app.yolov3.detect_and_draw_box(filename)

    import app.detect
    opt = {'weights': 'yolov5s.pt', 'source': '', 'imgsz': [640, 640], 'conf_thres': 0.25, 'iou_thres': 0.45, 'max_det': 1000, 'device': '', 'view_img': False, 'save_txt': False, 'save_conf': False, 'save_crop': False, 'nosave': False, 'classes': None, 'agnostic_nms': False, 'augment': False, 'visualize': False, 'update': False, 'project': '/src/app/runs/detect', 'name': 'exp', 'exist_ok': False, 'line_thickness': 3, 'hide_labels': False, 'hide_conf': False, 'half': False}
    app.detect.main(opt, "/src/app/files/yolov/inputs_yolov/" + filename , "/src/app/files/yolov/outputs_yolov/")
    return {file.filename}


@app.get("/api/export_yolov/{file_name}", responses={200: {"description": "A picture of a cat.", "content" : {"image/jpeg" : {"example" : "No example available. Just imagine a picture of a cat."}}}})
def export_skinseg(file_name):
    output_jpeg_file_name = file_name + ".mp4"
    path = "/src/app/files/yolov/outputs_yolov/"
    file_path = os.path.join(path, output_jpeg_file_name)
    if os.path.exists(file_path):
        print(file_name)
        return FileResponse(file_path, media_type="image/jpeg", filename=output_jpeg_file_name)
    return {"error" : "File not found!"}





















































# @app.get("/export_yolov", responses={200: {"description": "A picture of a cat.", "content" : {"image/jpeg" : {"example" : "No example available. Just imagine a picture of a cat."}}}})
# def export_yolov():
#     path = "/src/app/files/yolov/outputs_yolov/"
#     file_path = os.path.join(path, "oranges.jpg")
#     if os.path.exists(file_path):
#         return FileResponse(file_path, media_type="image/jpeg", filename="oranges.jpeg")
#     return {"error" : "File not found!"}










# @app.post("/image")
# async def image(image: UploadFile = File(...)):
#     file_location = f"/src/Inputs/Nifti_images/{image.filename}"
#     return {"filename": image.filename}

# @app.post("/execute")
# async def execute():
#     print('start')

#     # ssh import and params
#     ssh = paramiko.SSHClient()
#     ssh.load_system_host_keys()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     print('loaded')

#     # ssh connection
#     ssh.connect(hostname='0.0.0.0', username='pfe', password='pfe', port=22, allow_agent=False, look_for_keys=False, banner_timeout=200)
#     print('connected')

#     # # Run a command and catch the result
#     stdin, stdout, stderr = ssh.exec_command('cd /src/notebooks \n ls \n ipython pfe.ipynb')
#     print('executed')

#     print(f'STDOUT: {stdout.read().decode("utf8")}')
#     print(f'STDERR: {stderr.read().decode("utf8")}')

#     return_ssh_code = stdout.channel.recv_exit_status()
#     print(f'Return code: {return_ssh_code}')
#     if return_ssh_code != 0:
#         print('ssh connenction failed')
#     else:
#         print('ssh connenction stablished')

#     # Because they are file objects, they need to be closed
#     stdin.close()
#     stdout.close()
#     stderr.close()

#     # Close the client itself
#     ssh.close()

#     return "executed"



# @app.post("/download")
# async def download():
#     print('start')

#     # ssh import and params
#     ssh = paramiko.SSHClient()
#     ssh.load_system_host_keys()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     print('loaded')

#     # ssh connection
#     ssh.connect(hostname='0.0.0.0', username='pfe', password='pfe', port=22, allow_agent=False, look_for_keys=False, banner_timeout=200)

#     print('connected')

#     # # Run a command and catch the result
#     command = "cp /src/Outputs/JPEG_Outputs/Output_img1.jpeg /src/app/files"
#     stdin, stdout, stderr = ssh.exec_command(command)
    
#     print('executed')

#     print(f'STDOUT: {stdout.read().decode("utf8")}')
#     print(f'STDERR: {stderr.read().decode("utf8")}')

#     return_ssh_code = stdout.channel.recv_exit_status()
#     print(f'Return code: {return_ssh_code}')
#     if return_ssh_code != 0:
#         print('ssh connenction failed')
#     else:
#         print('ssh connenction stablished')

#     # Because they are file objects, they need to be closed
#     stdin.close()
#     stdout.close()
#     stderr.close()

#     # Close the client itself
#     ssh.close()

#     return "downloaded"



# # path = "/home/pfe/projet/pfe-docker/pfe/app"
# path = "/src/app/"

# @app.get("/output", responses={200: {"description": "A picture of a cat.", "content" : {"image/jpeg" : {"example" : "No example available. Just imagine a picture of a cat."}}}})
# def export_skinseg():
#     # file_path = os.path.join(path, "files/cat.jpg")
#     file_path = os.path.join(path, "files/Output_img1.jpeg")
#     if os.path.exists(file_path):
#         # return FileResponse(file_path, media_type="image/jpeg", filename="cat.jpg")
#         return FileResponse(file_path, media_type="image/jpeg", filename="Output_img1.jpeg")
#     return {"error" : "File not found!"}













# # path = "/home/pfe/projet/pfe-docker/pfe/app"
# path = "/src/app/"

# @app.get("/output", responses={200: {"description": "A picture of a cat.", "content" : {"image/jpeg" : {"example" : "No example available. Just imagine a picture of a cat."}}}})
# def export_skinseg():
#     # file_path = os.path.join(path, "files/cat.jpg")
#     file_path = os.path.join(path, "files/Output_img1.jpeg")
#     if os.path.exists(file_path):
#         # return FileResponse(file_path, media_type="image/jpeg", filename="cat.jpg")
#         return FileResponse(file_path, media_type="image/jpeg", filename="Output_img1.jpeg")
#     return {"error" : "File not found!"}

# -----------------------------------------
@app.get("/cat", responses={200: {"description": "A picture of a cat.", "content" : {"image/jpeg" : {"example" : "No example available. Just imagine a picture of a cat."}}}})
def cat():
    path = "/src/app/"
    file_path = os.path.join(path, "files/cat.jpg")
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="image/jpeg", filename="mycat.jpg")
    return {"error" : "File not found!"}










# @app.post("/api/predict_skinseg_two")
# async def predict_skinseg(file: UploadFile = File(...)):
#     # 0. VALIDATE INPUT FILE
#     fileExtension = file.filename.split(".")[-1] in ("nii", "gz", "jpeg", "jpg", "png")
#     if not fileExtension:
#         raise HTTPException(status_code=415, detail="Unsupported file provided.")

#     # 1. Upload images:
#     file_location = f"/src/app/files/skinseg/inputs_skinseg/Nifti_inputs/{file.filename}"
#     app.fileInputName = file.filename
    
#     with open(file_location, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)  

#     # 2. ssh import and params
#     ssh = paramiko.SSHClient()
#     ssh.load_system_host_keys()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     print('loaded')

#     # 3. ssh connection
#     ssh.connect(hostname='0.0.0.0', username='pfe', password='pfe', port=22, allow_agent=False, look_for_keys=False, banner_timeout=200)
    
#     # command = "cd /src/notebooks \n ipython skinseg.ipynb --input=" + app.fileInputName
#     # command = "cd /src/notebooks \n ipython skinseg.ipynb "  + app.fileInputName 
#     command = "cd /src/notebooks \n ipython skinseg.py "  + app.fileInputName

#     stdin, stdout, stderr = ssh.exec_command(command)
    
#     print('executed')

#     print(f'STDOUT: {stdout.read().decode("utf8")}')
#     print(f'STDERR: {stderr.read().decode("utf8")}')

#     return_ssh_code = stdout.channel.recv_exit_status()
#     print(f'Return code: {return_ssh_code}')
#     if return_ssh_code != 0:
#         print('ssh connenction failed')
#     else:
#         print('ssh connenction stablished')

#     # Because they are file objects, they need to be closed
#     stdin.close()
#     stdout.close()
#     stderr.close()

#     # Close the client itself
#     ssh.close()
#     return 'haha'

# @app.get("/export_skinseg", responses={200: {"description": "A picture of a cat.", "content" : {"image/jpeg" : {"example" : "No example available. Just imagine a picture of a cat."}}}})
# def export_skinseg():
#     path = "/src/app/files/skinseg/outputs_skinseg/"
#     file_path = os.path.join(path, "JPEG_outputs/Output_img1.jpeg")
#     if os.path.exists(file_path):
#         return FileResponse(file_path, media_type="image/jpeg", filename="Output_img1.jpeg")
#     return {"error" : "File not found!"}



# # This endpoint handles all the logic necessary for the object detection to work.
# # It requires the desired model and the image in which to perform object detection.
# @app.post("/api/predict_yolov") 
# def predict_yolov(file: UploadFile = File(...)):
#     import app.yolov3

#     # 0. VALIDATE INPUT FILE
#     filename = file.filename
#     fileExtension = filename.split(".")[-1] in ("jpg", "jpeg", "png")
#     if not fileExtension:
#         raise HTTPException(status_code=415, detail="Unsupported file provided.")

#     # 1. Upload images:
#     file_location = f"/src/app/files/yolov/inputs_yolov/{filename}" 
#     app.fileInputName = file.filename


#     with open(file_location, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)  
    
#     app.yolov3.detect_and_draw_box(filename)
#     return {file.filename}

#     # 2. ssh import and params
#     ssh = paramiko.SSHClient()
#     ssh.load_system_host_keys()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     print('loaded')

#     # 3. ssh connection
#     ssh.connect(hostname='0.0.0.0', username='pfe', password='pfe', port=22, allow_agent=False, look_for_keys=False, banner_timeout=200)
    
#     command = "cd /src/notebooks \n ipython yolov3.py " + app.fileInputName

#     stdin, stdout, stderr = ssh.exec_command(command)
    
#     print('executed')

#     print(f'STDOUT: {stdout.read().decode("utf8")}')
#     print(f'STDERR: {stderr.read().decode("utf8")}')

#     return_ssh_code = stdout.channel.recv_exit_status()
#     print(f'Return code: {return_ssh_code}')
#     if return_ssh_code != 0:
#         print('ssh connenction failed')
#     else:
#         print('ssh connenction stablished')

#     # Because they are file objects, they need to be closed
#     stdin.close()
#     stdout.close()
#     stderr.close()
