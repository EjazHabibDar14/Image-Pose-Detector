import cv2

def detect_eyes(img):
  eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
  face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
  img = cv2.imread(img)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.1, 4)

  eyes_detected = False

  for (x, y, w, h) in faces:
      roi_gray = gray[y:y+h, x:x+w]
      roi_color = img[y:y+h, x:x+w]
      eyes = eye_cascade.detectMultiScale(roi_gray)

      # To detect only 2 eyes, limit the loop to 2 iterations
      eye_count = 0
      for i, (ex, ey, ew, eh) in enumerate(eyes):
          if eye_count >= 2:
              break
          cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 5)

          # Print "Eye" below each detected eye with larger font and black color
          font = cv2.FONT_HERSHEY_SIMPLEX
          font_scale = 1
          font_thickness = 2
          text = "Eye"
          text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
          text_x = ex + (ew - text_size[0]) // 2
          text_y = ey + eh + 30
          cv2.putText(roi_color, text, (text_x, text_y), font, font_scale, (0, 0, 0), font_thickness)

          eye_count += 1

      if eye_count > 0:
          eyes_detected = True

  if eyes_detected:
    cv2.imshow(img)
    return "Eyes looking directly at the camera"
  else:
    cv2.imshow(img)
    return "Eyes not looking directly at the camera"

detect_eyes('/Sample Photos/front_face.jpg')

detect_eyes('/Sample Photos/side_face.jpg')
