export const models = [
    {
        id: 0,
        name: 'Skin Segmentation',
        image: "/images/skinSeg/skinseg-cover.jpg",
        description: 'Skin medical image segmentation that you can use is your medical research',
        detailLink: '/modelDetails/0',
        inputImageExempleLink: '/images/skinSeg/skinseg-input.jpg',
        outputImageExempleLink: '/images/skinSeg/skinseg-output.jpeg',
        executeLink: 'http://34.136.35.194:8000/api/predict_skinseg',
        exportLink: 'http://34.136.35.194:8000/api/export_skinseg',
        fileExtentions: '*.nii'
        
    },
    {
        id: 1,
        name: 'Object Detection',
        image: "/images/object/object-cover.jpeg",
        description: "Object detection is a computer technology related to computer vision and image processing that deals with detecting instances of semantic objects of a certain class in digital images and videos. Well-researched domains of object detection include face detection and pedestrian detection. \n this product is based on yolo-v5 model",
        detailLink: '/modelDetails/1',
        inputImageExempleLink: '/images/object/object-input-2.jpg',
        outputImageExempleLink: '/images/object/object-output-2.jpg',
        executeLink: 'http://34.136.35.194:8000/api/predict_yolo',
        exportLink: 'http://34.136.35.194:8000/api/export_yolo',
        fileExtentions: "*.bmp,  *.jpg,  *.jpeg,  *.png,  *.tif,  *.tiff,  *.dng,  *.webp,  *.mpo,  *.mov,  *.avi,   *.mp4,  *.mpg,  *.mpeg,  *.m4v,  *.wmv,  *.mkv"

    },
    {
        id: 2,
        name: 'Face/Gender Detection',
        image: "/images/faceGender/face-gender-cover.jpeg",
        description: "The algorithm starts by detecting input face, once face is detected, it can be passed to recognize gender. It will return the labels (man, woman) and associated probabilities.",
        detailLink: '/modelDetails/2',
        inputImageExempleLink: '/images/faceGender/face-gender-input.jpg',
        outputImageExempleLink: '/images/faceGender/face-gender-output.jpg',
        executeLink: 'http://34.136.35.194:8000/api/predict_cvlib',
        exportLink: 'http://34.136.35.194:8000/api/export_cvlib',
        fileExtentions: "*.jpg,  *.jpeg,  *.png"

    }
]

