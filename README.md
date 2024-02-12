# FoodScaningProject
This project utilizes Google Gemini API along with Flask framework to create a web application that scans images of food items, identifies them, provides nutritional information, and suggests whether the food is healthy or not.

## Features
- Image Upload: Users can upload images containing various food items.
- Food Identification: The system accurately detects and labels different types of food items within the image.
- Nutritional Information: Extracts nutritional details of identified foods.
- Categorization: Categorizes the type of food based on the detected items (e.g., fruits, vegetables, grains, etc.).
- Health Assessment: Suggests whether the identified foods are healthy or not.

## Technologies Used
- Flask: Python web framework used for handling HTTP requests and responses.
- Google Gemini: AI-powered API used for generating content and identifying objects within images.
- HTML/CSS: Frontend for the web application.

## Prerequisites
#### Before running the project, ensure you have the following installed:

- Python 3.x
- Flask
- Google Gemini API key
- PIL (Python Imaging Library)
- dotenv

## Getting Started
Clone this repository to your local machine:

      git clone https://github.com/yourusername/food-scanning-project.git

Navigate to the project directory:

      cd food-scanning-project

Install dependencies:

      pip install -r requirements.txt

Set up your Google Gemini API key:
- Obtain an API key from the Google Cloud Console.   
- Set the API key in the .env file:

       GEMINI_API_KEY=YOUR_API_KEY

Run the Flask application:

       python app.py     

Access the application in your web browser at http://localhost:5000.   

## Usage
1. Open the web application in your browser.
2. Upload an image containing food items.
3. Add any additional notes if required.
4. Submit the form.
5. The application will process the image, identify food items, extract nutritional information, and provide health assessments.
6. The results will be displayed on the result page.

## License
This project is licensed under the MIT License.

## Contributors
Neeraj Kumar Sharma - Full Stack Data Scientist



