import cv2
import detect_face, detect_eyes, detect_mouth, detect_smile

def image_pose_detector(image, detect_face_func, detect_eyes_func, detect_mouth_func, detect_smile_func):
    is_face_facing_camera = detect_face(image)
    are_eyes_facing_camera = detect_eyes(image)
    is_smiling = detect_smile(image)
    is_mouth_open = detect_mouth(image)

    return is_face_facing_camera, are_eyes_facing_camera, is_smiling, is_mouth_open

# Usage example:
# Replace the following 'image' with your actual image data
sample_image = "/Sample Photos/smile.jpg"

# Replace the following functions with your actual detection functions
result = image_pose_detector(sample_image, detect_face, detect_eyes, detect_mouth, detect_smile)

print("Is face facing the camera?", result[0])
print("Are eyes facing the camera?", result[1])
print("Is the person smiling?", result[2])
print("Is the mouth open?", result[3])

