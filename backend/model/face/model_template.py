from deepface import DeepFace

image1 = r'backend\data\checkin_image\CaoThanhTrung(466583)\1740963100000-8631740963100644.jpg'
image2 = r'backend\data\checkin_image\DoDucManh(463419)\1740964847000-6251740964849667.jpg'

embedding1 = DeepFace.represent(img_path=image1, model_name="Facenet")[0]["embedding"]
embedding2 = DeepFace.represent(img_path=image2, model_name="Facenet")[0]["embedding"]

result = DeepFace.verify(image1, image2, model_name="Facenet")
print(result["verified"], result["distance"])


def callModel(image_1, image_2, model_name="Facenet"): # "VGG-Face", "Facenet", "Facenet512", "ArcFace", "DeepFace", "Dlib", "OpenFace", "DeepID", "SFace"
    result = DeepFace.verify(image_1, image_2, model_name=model_name)
    return result["verified"], result["distance"]