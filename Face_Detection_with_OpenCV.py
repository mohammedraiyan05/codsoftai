import cv2
import numpy as np
import requests
from PIL import Image

# Function to load an image from a URL
def load_image_from_url(url):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            image = Image.open(response.raw)
            return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)  # Convert PIL image to OpenCV BGR format
        else:
            print(f"Error: Could not fetch the image from URL. HTTP Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching image: {e}")
        return None

# Face detection with OpenCV
def detect_faces(image):
    # Load pre-trained face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    if image is None:
        print(f"Error: No valid image provided.")
        return

    # Convert to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    return image

# Main function to run face detection
if __name__ == "__main__":
    # Replace with a valid image URL
    image_url = "https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg"  # Replace with a face image URL
    img = load_image_from_url(image_url)

    if img is not None:
        # Detect faces and display the result
        result_img = detect_faces(img)

        # Display the image with detected faces
        cv2.imshow('Face Detection', result_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Could not process the image.")