import cv2

def detect_smile(image):
    image = cv2.imread(image)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)

        # Determine if a smile is detected and draw rectangles accordingly
        if len(smiles) > 0:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle for face
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(image, (x + sx, y + sy), (x + sx + sw, y + sy + sh), (0, 255, 0), 2)  # Green rectangle for smile
                cv2.imshow(image)
                return "Smiling"
        else:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Red rectangle for face
            cv2.imshow(image)
            return "Not Smiling"

detect_smile('/Sample Photos/smile.jpg')

detect_smile('/Sample Photos/no_smile.jpg')