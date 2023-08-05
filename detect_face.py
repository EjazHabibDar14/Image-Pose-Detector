import cv2

def detect_face(img):
  face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
  # Read the input image
  img = cv2.imread(img)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.1, 4)

  # Check the number of detected faces
  num_faces = len(faces)

  for (x, y, w, h) in faces:
      cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
      # Print "Face" below each detected face with larger font and black color
      font = cv2.FONT_HERSHEY_SIMPLEX
      font_scale = 2.5
      font_thickness = 5
      text = "Face"
      text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
      text_x = x + (w - text_size[0]) // 2
      text_y = y + h + 30
      cv2.putText(img, text, (text_x, text_y), font, font_scale, (0, 0, 0), font_thickness)
  if num_faces == 1:
    cv2.imshow(img)
    return "Face is facing towards the camera."
  else:
    cv2.imshow(img)
    return "Face is not facing towards the camera."

  # Display the output using cv2_imshow

detect_face('/Sample Photos/front_face.jpg')

detect_face('/Sample Photos/side_face.jpg')