from flask import Flask, request, jsonify, render_template
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

# Set OpenAI API key from the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the homepage route to serve the frontend
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Function to generate email response using OpenAI API
def generate_email_response(data):
    try:
        # Create a prompt based on the input data
        prompt = f"""
        Generate an email response with the following details:
        From Name: {data['fromName']}
        Client First Name: {data['clientName']}
        Client Last Name: {data['clientLastName']}
        Client Email: {data['clientEmail']}
        Client Country: {data['clientCountry']}
        Client Location: {data['clientLocation']}
        Client Language: {data['clientLanguage']}
        Project Type: {data['projectType']}
        Service Category: {data['serviceCategory']}
        Client Website: {data['clientWebsite']}
        Client Message: {data['clientMessage']}
        Provide a professional and polite response.
        """

        # Call the OpenAI API to generate the email
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error generating email: {e}")
        return "Error generating email response."

# API endpoint to handle email response generation requests
@app.route("/generate-response", methods=["POST"])
def generate_response():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Generate an email response using OpenAI
        response = generate_email_response(data)

        # Return the generated response as JSON
        return jsonify({"response": response})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "An error occurred while generating the response."}), 500

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
