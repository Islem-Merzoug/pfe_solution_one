from fastapi import FastAPI, File, UploadFile, HTTPException, Form, Body

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse
from starlette.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from datetime import datetime

import os

import shutil
import paramiko
from enum import Enum

from fastapi import FastAPI, BackgroundTasks, UploadFile, File, Form
from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import BaseModel, EmailStr
from typing import List

from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()                    #for python-dotenv method

import os 

app = FastAPI(title='Deploying a ML Models with FastAPI')

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


# ------------------------------------------ contact --------------------------------------------

class EmailSchema(BaseModel):
    email: List[EmailStr]

class EmailContent(BaseModel):
    message: str
    subject: str



@app.post("/email")
async def simple_send(
    email: EmailSchema, content:EmailContent
    ) -> JSONResponse:

    print(email.email[0])
    conf = ConnectionConfig(
        MAIL_USERNAME = os.environ.get('EMAIL'),
        MAIL_PASSWORD = os.environ.get('PASS'),
        MAIL_FROM = email.email[0],
        MAIL_PORT = 587,
        MAIL_SERVER = "smtp.gmail.com",
        MAIL_TLS = True,
        MAIL_SSL = False,
        USE_CREDENTIALS = True,
        VALIDATE_CERTS = True
    )
    
    html = f""" {content.message} """

    message = MessageSchema(
        subject=content.subject,
        recipients=email.dict().get("email"),  # List of recipients, as many as you can pass 
        body=html,
        subtype="text"
        )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "Email has been sent"})



# ---------------------------------------- file ------------------------------

from app.routes.file import router
from app.model.file import FileSchema
from app.model.file import ResponseModel, ErrorResponseModel
from app.database import add_file, delete_file, retrieve_file, retrieve_files, update_file, retrieve_all_files


# @app.post("/add_file", response_description="File data added into the database")
# async def add_file_data(file: FileSchema = Body(...)):
#     print(file)
#     file = jsonable_encoder(file)
#     new_file = await add_file(file)
#     return ResponseModel(new_file, "File added successfully.")


@app.post("/auth/is_admin/", responses={200: {"description": "A picture of a cat.", "content" : {"image/jpeg" : {"example" : "No example available. Just imagine a picture of a cat."}}}})
async def is_admin(user_id: str = Form(...),):
    from app.database import is_admin
    admin = await is_admin(user_id)
    print("the admin is: ", admin)
    # return user_id


@app.get("/get_files/{user_id}", response_description="Files retrieved")
async def get_files(user_id):
    from app.database import is_admin
    if user_id: 
        is_admin = await is_admin(user_id)
        if is_admin:
            files = await retrieve_all_files()
            return ResponseModel(files, "Files data retrieved successfully")
        else:
            files = await retrieve_files(user_id)
            print(files)
            if files:
                return ResponseModel(files, "Files data retrieved successfully")
            return ResponseModel(files, "Empty list returned")
    else: 
        print("no user_id")
        return "no user_id"

@app.get("/retrieve_file/{id}", response_description="File data retrieved")
async def get_file_data(id):
    file = await retrieve_file(id)
    if file:
        return ResponseModel(file, "File data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "File doesn't exist.")




# ------------------------------------------ authentification --------------------------------------------
from fastapi import FastAPI, Body

from app.model.user import UserSchema, UserLoginSchema
from app.auth.auth_handler import signJWT
from app.routes.file import router
from app.database import add_file, delete_file, retrieve_file, retrieve_files, retrieve_user

@app.post("/user/signup", response_description="user sign up", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    from app.database import add_user
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    print(signJWT(str(user['_id']), user['fullname'], user['email']))
    return signJWT(str(user['_id']), user['fullname'], user['email'])


@app.post("/user/signin/", response_description="user sign in", tags=["user"])
async def sign_in(user: UserLoginSchema = Body(...)):
    user = jsonable_encoder(user)
    user = await retrieve_user(user)
    print(user)
    if user:
        print(signJWT(str(user['id']), user['fullname'], user['email']))
        return signJWT(str(user['id']), user['fullname'], user['email'])

    return ErrorResponseModel("An error occurred.", 404, "User doesn't exist.")

























# ------------------------------------------ skinseg --------------------------------------------

@app.post("/api/predict_skinseg")
async def predict_skinseg(userID: str = Form(...), choice: str = Form(...), file: UploadFile = File(...)):

    # configs
    inputDir = "/src/app/files/skinseg/inputs_skinseg/Nifti_inputs/"
    outputDir = "/src/app/files/skinseg/outputs_skinseg/JPEG_outputs/"
    fileName = file.filename
    fileNameWithoutExtension = file.filename.rsplit('.', 1)[0]
    fileExtension = file.filename.split(".")[-1]


    import app.skinseg
    # 0. VALIDATE INPUT FILE
    isExtension = fileName.split(".")[-1] in ('nii')
    if not isExtension:
        raise HTTPException(status_code=415, detail="Unsupported file provided.")

    # 1. Upload images:
    with open(inputDir + fileName, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)  

    # 2. Predict images:
    app.skinseg.predict_data(fileName, inputDir, outputDir, fileNameWithoutExtension)  

    # 3. Store file data:
    fileData = {
        "name": fileNameWithoutExtension,
        "date": datetime.today(),
        "type": fileExtension,
        "service": "Skin Segmentation",
        "choice": choice,
        "inputLink": inputDir + fileName,
        "outputLink": "http://localhost:8000/api/export_skinseg/"+ fileNameWithoutExtension + "/"+ fileExtension,
        "user_id": userID
    }
    file = jsonable_encoder(fileData)
    new_file = await add_file(file)

    return ResponseModel(new_file, "File added successfully.")
















@app.get("/api/export_skinseg/{file_name}/{extention_name}", responses={200: {"description": "A picture of a cat.", "content" : {"image/jpeg" : {"example" : "No example available. Just imagine a picture of a cat."}}}})
async def export_skinseg(file_name, extention_name):
    output_jpeg_file_name = file_name + "." + "jpeg"
    path = "/src/app/files/skinseg/outputs_skinseg/JPEG_outputs"
    file_path = os.path.join(path, output_jpeg_file_name)
    if os.path.exists(file_path):
        print(file_name)
        return FileResponse(file_path, media_type="image/jpeg", filename=output_jpeg_file_name)
    return {"error" : "File not found!"}




# ------------------------------------------ yolov3 --------------------------------------------

# List available models using Enum for convenience. This is useful when the options are pre-defined.
class Model(str, Enum):
    yolov3tiny = "yolov3-tiny"
    yolov3 = "yolov3"


@app.post("/api/predict_yolo") 
# def predict_yolo(model: Model, file: UploadFile = File(...)):
async def predict_yolo(userID: str = Form(...), choice: str = Form(...), file: UploadFile = File(...)):

    # configs
    inputDir = "/src/app/files/yolo/inputs_yolo/"
    outputDir = "/src/app/files/yolo/outputs_yolo/"
    fileName = file.filename
    fileNameWithoutExtension = file.filename.rsplit('.', 1)[0]
    fileExtension = file.filename.split(".")[-1]
    
    # 0. VALIDATE INPUT FILE
    isExtension = fileName.split(".")[-1] in ('bmp', 'jpg', 'jpeg', 'png', 'tif', 'tiff', 'dng', 'webp', 'mpo', 'mov', 'avi', 'mp4', 'mpg', 'mpeg', 'm4v', 'wmv', 'mkv')
    if not isExtension:
        raise HTTPException(status_code=415, detail="Unsupported file provided.")

    # 1. Upload images:
    with open(inputDir + fileName, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)  
    
    # 2. Predict images:
    # import app.yolov3
    # app.yolov3.detect_and_draw_box(filename)

    import app.detect
    opt = {'weights': 'yolov5s.pt', 'source': '', 'imgsz': [640, 640], 'conf_thres': 0.25, 'iou_thres': 0.45, 'max_det': 1000, 'device': '', 'view_img': False, 'save_txt': False, 'save_conf': False, 'save_crop': False, 'nosave': False, 'classes': None, 'agnostic_nms': False, 'augment': False, 'visualize': False, 'update': False, 'project': '/src/app/runs/detect', 'name': 'exp', 'exist_ok': False, 'line_thickness': 3, 'hide_labels': False, 'hide_conf': False, 'half': False}
    app.detect.main(opt, inputDir + fileName , outputDir)
    
    # 3. Store file data:
    fileData = {
        "name": fileNameWithoutExtension,
        "date": datetime.today(),
        "type": fileExtension,
        "service": "Object Detection",
        "choice": choice,
        "inputLink": inputDir + fileName,
        "outputLink": "http://localhost:8000/api/predict_yolo/"+ fileNameWithoutExtension + "/"+ fileExtension,        
        "user_id": userID
    }
    file = jsonable_encoder(fileData)
    new_file = await add_file(file)

    return ResponseModel(new_file, "File added successfully.")

@app.get("/api/export_yolo/{file_name}/{extention_name}", responses={200: {"description": "A picture of a cat.", "content" : {"image/jpeg" : {"example" : "No example available. Just imagine a picture of a cat."}}}})
async def export_skinseg(file_name, extention_name):
    output_jpeg_file_name = file_name + "." + extention_name
    path = "/src/app/files/yolo/outputs_yolo/"
    file_path = os.path.join(path, output_jpeg_file_name)
    if os.path.exists(file_path):
        print(file_name)
        return FileResponse(file_path, media_type="image/jpeg", filename=output_jpeg_file_name)
    return {"error" : "File not found!"}





# ------------------------------------------ cvlib --------------------------------------------

@app.post("/api/predict_cvlib") 
async def predict_cvlib(userID: str = Form(...), choice: str = Form(...), file: UploadFile = File(...)):
    # configs
    inputDir = "/src/app/files/cvlib/inputs_cvlib/"
    outputDir = "/src/app/files/cvlib/outputs_cvlib/"
    fileName = file.filename
    fileNameWithoutExtension = file.filename.rsplit('.', 1)[0]
    fileExtension = file.filename.split(".")[-1]
    
    # 0. VALIDATE INPUT FILE
    isExtension = fileName.split(".")[-1] in ("jpg", "jpeg", "png")
    if not isExtension:
        raise HTTPException(status_code=415, detail="Unsupported file provided.")

    # 1. Upload images:
    with open(inputDir + fileName, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)   
    
    # 2. Predict images:
    import app.cvlib
    output_dir = "/src/app/files/cvlib/outputs_cvlib"
    app.cvlib.detection(choice, fileName, inputDir + fileName , output_dir)

    # 3. Store file data:
    fileData = {
        "name": fileNameWithoutExtension,
        "date": datetime.today(),
        "type": fileExtension,
        "service": "Face/Gender Detection",
        "choice": choice,
        "inputLink": inputDir + fileName,
        "outputLink": "http://localhost:8000/api/predict_cvlib/"+ fileNameWithoutExtension + "/"+ fileExtension,
        "user_id": userID
    }
    file = jsonable_encoder(fileData)
    new_file = await add_file(file)
    
    return ResponseModel(new_file, "File added successfully.")


@app.get("/api/export_cvlib/{file_name}/{extention_name}", responses={200: {"description": "A picture of a cat.", "content" : {"image/jpeg" : {"example" : "No example available. Just imagine a picture of a cat."}}}})
async def export_cvlib(file_name, extention_name):
    output_jpeg_file_name = file_name + "." + extention_name
    path = "/src/app/files/cvlib/outputs_cvlib/"
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
