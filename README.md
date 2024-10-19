# quotes
This is a web application I built that allows me to create and store quotes for my partner. It offers a simple user interface through [FastHTML](https://fastht.ml/) and sends email reminders to that special someone.

## Local Setup
1. Clone the repository

2. Create a virtual environment (optional)
   - `python -m venv venv`

3. Activate the virtual environment (optional)
   - Windows: `venv\Scripts\activate`
   - Linux: `source venv/bin/activate`

4. Install the dependencies
   - `pip install -r requirements.txt`

5. Run the application
   - `python main.py`
   
6. Navigate to `http://localhost:5001/` to view the application.

## Example .env File
A .env file will be needed to configure email reminders upon creating a quote. Here is what it should look like:
```
SENDER="<email address of sender>"
RECIPIENT="<email address of recipient>"
GMAIL_SMTP_PW="<google app password>"
APP_URL="<URL of your application>"
```
To send emails from your gmail account using google's SMTP server, create a [Google App Password](https://myaccount.google.com/apppasswords) and paste it here.