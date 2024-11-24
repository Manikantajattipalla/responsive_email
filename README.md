# **Responsive Email**

This project is a simple Python Flask application that uses OpenAI's GPT-3.5-turbo API to generate professional email responses based on user-provided details.

## **Features**

- Generates professional email responses.
- Formats responses in HTML for easy integration with frontend applications.
- Modular design with clear separation of responsibilities.
- Supports prompt customization and multiple use cases.
- Responsive Design: The email templates are designed to be fully responsive and adapt to different screen sizes and devices.
- Cross-Client Compatibility: Ensures compatibility across various email clients such as Gmail, Outlook, Yahoo Mail, and more.
- Inline CSS: Uses inline CSS to ensure styles are applied consistently across different email clients.
- Media Queries: Utilizes media queries to adjust the layout and content for different screen sizes.
- Fallbacks for Non-Supporting Clients: Provides fallbacks for email clients that do not support certain CSS properties or media queries.
- Optimized Images: Includes techniques for optimizing images to reduce load times and improve performance.
- Accessible Design: Ensures that the email templates are accessible to users with disabilities, including proper use of alt text for images and semantic HTML.
- Modular Components: Uses modular components to make it easy to reuse and customize parts of the email templates.
- Testing and Validation: Includes tools and methods for testing and validating the email templates to ensure they render correctly in different email clients.
- Documentation: Comprehensive documentation to help users understand how to use and customize the email templates.

## **Getting Started**

### **Prerequisites**

- Python: Install Python (v3.7 or later) from [Python Official Website](https://www.python.org/).
- OpenAI API Key: Sign up at [OpenAI](https://www.openai.com/) and obtain your API key.

### **Installation**

1. Clone the Repository:
```sh
git clone https://github.com/yourusername/responsive_email.git
cd responsive_email

2.Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3.Install the required dependencies:

pip install -r requirements.txt

4.Set Up Environment Variables: Create a .env file in the root directory and add your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key

Usage
1.Run the application:

python app.py

2.Access the application at http://localhost:5000.

Example Input
Make a POST request to the /generate-response endpoint with the following JSON structure:

{
  "fromName": "John Doe",
  "clientName": "Jane",
  "clientLastName": "Smith",
  "clientEmail": "jane.smith@example.com",
  "projectType": "Website Development",
  "clientMessage": "I need a professional website for my business."
}

Example Output
The API will return a response in the following format:

{
  "response": "<p><strong>Subject:</strong> Proposal for Your Website Development</p><p><strong>Dear Jane Smith,</strong></p><p>Thank you for reaching out. We specialize in creating professional websites tailored to your business needs...</p><p><strong>Best regards,</strong><br>John Doe</p>"
}

Contact For any issues or queries, feel free to reach out at:
Email: manikanta@kvgengg.com
GitHub: Manikantajattipalla