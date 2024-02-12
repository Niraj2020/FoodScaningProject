from flask import Flask, render_template, request
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key='Give your API_key')
model = genai.GenerativeModel('gemini-pro-vision')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    input_prompt = """
    You are an expert in indentify different types of food in images,
    The system should accurately detect and label various foods displayed in the image, providing the name 
    of the food and its location within the image (e.g., bottom left, right corner, etc.). Additionally, 
    the system should extract nutritional information and categorize the type of food (e.g., fruits, vegetables, grains, etc.) 
    based on the detected items. The output should include a comprehensive report or display showing the
    identified foods, their positions, names, and corresponding nutritional details, and also calculate total of corresponding nutritional details.
    also suggest me wheater the food is healthy or not-healthy.
    additionally write a short notes on that image.
    """

    input_text = request.form.get('input_text')
    image_file = request.files['image']

    # Process the image
    if image_file:
        image = Image.open(image_file)
        image_data = input_image_details(image_file)
        response = get_gemini_response(input_prompt, image_data, input_text)
        return render_template('result.html', response=response)
    else:
        return 'No image uploaded'

def input_image_details(upload_file):
    if upload_file is not None:
        bytes_data = upload_file.getvalue()
        image_parts = [{    
            "mime_type": upload_file.mimetype,
            "data": bytes_data
        }]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

def get_gemini_response(input_prompt, image, prompt):
    response = model.generate_content([input_prompt, image[0], prompt])
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
