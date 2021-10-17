import detect

opt = {'weights': 'yolov5s.pt', 'source': '', 'imgsz': [640, 640], 'conf_thres': 0.25, 'iou_thres': 0.45, 'max_det': 1000, 'device': '', 'view_img': False, 'save_txt': False, 'save_conf': False, 'save_crop': False, 'nosave': False, 'classes': None, 'agnostic_nms': False, 'augment': False, 'visualize': False, 'update': False, 'project': '/src/app/runs/detect', 'name': 'exp', 'exist_ok': False, 'line_thickness': 3, 'hide_labels': False, 'hide_conf': False, 'half': False}

print(type(opt))
detect.main(opt, "/src/app/data/images/zidane.jpg", "/src/app/runs/detect")