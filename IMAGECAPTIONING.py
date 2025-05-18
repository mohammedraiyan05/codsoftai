from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests

# Load the BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Function to process the image
def load_image_from_url(img_url):
    try:
        # Fetch the image from the URL
        response = requests.get(img_url, stream=True)
        if response.status_code == 200:
            try:
                # Open the image
                image = Image.open(response.raw)
                return image
            except Exception as e:
                print(f"Error loading image: {e}")
                return None
        else:
            print(f"Failed to fetch image. HTTP Status Code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching image from URL: {e}")
        return None

# Function to generate a caption
def generate_caption(image):
    if image is None:
        print("No valid image provided for captioning.")
        return None
    
    # Process the image and generate a caption
    try:
        inputs = processor(image, return_tensors="pt")
        out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)
        return caption
    except Exception as e:
        print(f"Error generating caption: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Provide a valid image URL (replace with your desired URL)
    img_url = "https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png"  # Replace with a valid image URL
    image = load_image_from_url(img_url)
    
    if image:
        # Generate and print the caption
        caption = generate_caption(image)
        if caption:
            print(f"Generated Caption: {caption}")
        else:
            print("Failed to generate a caption.")
    else:
        print("No image to process.")