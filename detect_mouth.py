import cv2
import dlib
def detect_mouth(img):
  # Load the pre-trained face detector from dlib
  detector = dlib.get_frontal_face_detector()

  # Load the pre-trained facial landmark predictor from dlib
  predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

  img = cv2.imread(img)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  # Detect faces in the image
  faces = detector(gray)

  for face in faces:
      # Get the facial landmarks for the face
      landmarks = predictor(gray, face)

      # Get the x and y coordinates of the mouth landmarks
      mouth_left = (landmarks.part(48).x, landmarks.part(48).y)
      mouth_right = (landmarks.part(54).x, landmarks.part(54).y)
      mouth_top = (landmarks.part(51).x, landmarks.part(51).y)
      mouth_bottom = (landmarks.part(57).x, landmarks.part(57).y)

      # Calculate the distance between the top and bottom of the mouth
      mouth_distance = mouth_bottom[1] - mouth_top[1]

      # Calculate the distance between the left and right edges of the mouth
      mouth_width = mouth_right[0] - mouth_left[0]

      # Define a threshold to determine if the mouth is open or closed
      mouth_open_threshold = 0.35  # You can adjust this value based on your needs

      # Check if the mouth is open or closed based on the distances
      if mouth_distance > mouth_open_threshold * mouth_width:
        cv2.imshow(img)
        return "Mouth is open."
        mouth_status = "Open"
      else:
        cv2.imshow(img)
        return "Mouth is closed."
        mouth_status = "Closed"

      # Draw a rectangle around the mouth
      cv2.rectangle(img, (mouth_left[0], mouth_top[1]), (mouth_right[0], mouth_bottom[1]), (0, 255, 0), 2)

      # Write the status (Open/Closed) below the mouth rectangle
      font = cv2.FONT_HERSHEY_SIMPLEX
      font_scale = 1
      thickness = 2
      text_size = cv2.getTextSize(mouth_status, font, font_scale, thickness)[0]
      text_x = mouth_left[0] + (mouth_width - text_size[0]) // 2
      text_y = mouth_bottom[1] + text_size[1] + 10
      cv2.putText(img, mouth_status, (text_x, text_y), font, font_scale, (0, 255, 0), thickness, cv2.LINE_AA)

  # Display the output image with the rectangle and text

detect_mouth('/Sample Photos/open_mouth.jpg')

detect_mouth('/Sample Photos/closed_mouth.jpg')
