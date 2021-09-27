export const models = [
    {
        id: 0,
        name: 'Skin Segmentation',
        image: "/images/skinSeg/skinseg-cover.jpg",
        description: 'Beginning with a color image, the first stage is to transform it to a skin-likelihood image. This involves transforming every pixel from RGB representation to chroma representation and determining the likelihood value based on the equation given in the previous section. The skin-likelihood image will be a gray-scale image whose gray values represent the likelihood of the pixel belonging to skin. A sample color image and its resulting skin-likelihood image are shown in Figure 3. All skin regions (like the face, the hands and the arms) were shown brighter than the non-skin region.',
        detailLink: '/modelDetails/0',
        inputImageExempleLink: '/images/skinSeg/skinseg-input.jpg',
        outputImageExempleLink: '/images/skinSeg/skinseg-output.jpeg',
        executeLink: 'http://34.141.52.228:8000/api/predict_skinseg',
        exportLink: 'http://34.141.52.228:8000/api/export_skinseg'
        
    },
    {
        id: 1,
        name: 'Object Detection',
        image: "/images/object/object-cover.jpeg",
        description: "En vision par ordinateur on désigne par détection d'objet une méthode permettant de détecter la présence d'une instance ou d'une classe d'objets dans une image numérique. Une attention particulière est portée à la détection de visage et la détection de personne.",
        detailLink: '/modelDetails/1',
        inputImageExempleLink: '/images/object/object-input-2.jpg',
        outputImageExempleLink: '/images/object/object-output-2.jpg',
        executeLink: 'http://34.141.52.228:8000/api/predict_yolov',
        exportLink: 'http://34.141.52.228:8000/api/export_yolov'
        
    },
    {
        id: 2,
        name: 'Face/Gender Detection',
        image: "/images/faceGender/face-gender-cover.jpeg",
        description: "En vision par ordinateur on désigne par détection d'objet une méthode permettant de détecter la présence d'une instance ou d'une classe d'objets dans une image numérique. Une attention particulière est portée à la détection de visage et la détection de personne.",
        detailLink: '/modelDetails/2',
        inputImageExempleLink: '/images/faceGender/face-gender-input.jpg',
        outputImageExempleLink: '/images/faceGender/face-gender-output.jpg',
        executeLink: 'http://34.141.52.228:8000/api/predict_cvlib',
        exportLink: 'http://34.141.52.228:8000/api/export_cvlib'
        
    }
]

