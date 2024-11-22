import os
from flask import Flask, request, jsonify, render_template
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Helper function to generate email response using OpenAI API
def generate_email_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=300,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error generating text: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML form

@app.route('/generate-response', methods=['POST'])
def generate_response():
    # Extract data from the form submission (JSON)
    data = request.get_json()
    from_name = data.get('fromName')
    client_name = data.get('clientName')
    client_last_name = data.get('clientLastName')
    client_email = data.get('clientEmail')
    client_country = data.get('clientCountry')
    client_location = data.get('clientLocation')
    client_language = data.get('clientLanguage')
    project_type = data.get('projectType')
    service_category = data.get('serviceCategory')
    client_website = data.get('clientWebsite')
    client_message = data.get('clientMessage')

    # Create the prompt to generate the email response
    prompt = f"""
        Generate a professional email response based on the following details:
        From: {from_name}
        To: {client_name} {client_last_name}
        Email: {client_email}
        Country: {client_country}
        Location: {client_location}
        Language: {client_language}
        Project Type: {project_type}
        Service Category: {service_category}
        Website: {client_website}
        Message: {client_message}

        The email should be professional and include:
        - A subject line
        - A greeting
        - An introduction
        - A brief overview of the client's message
        - A closing statement

        <p><strong>Subject:</strong> [Subject Line]</p>
        <p><strong>Dear {client_name} {client_last_name},</strong></p>
        <p>[Body of the email]</p>
        <p><strong>Best regards,</strong><br>{from_name}</p>
    """

    # Generate the email response using OpenAI API
    email_response = generate_email_response(prompt)

    if email_response:
        return jsonify({'response': email_response})
    else:
        return jsonify({'error': 'Error generating the response'}), 500

if __name__ == '__main__':
    app.run(debug=True)
