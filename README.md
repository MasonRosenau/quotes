# quotes
This is a web application I built that allows me to create and store quotes for my partner. It offers a simple user interface through [FastHTML](https://fastht.ml/) and sends email reminders to that special someone.


## Setup
1. Clone the repository and `cd` into it
2. Follow the [Virtual Environment](#virtual-environment-setup) or [Docker](#docker-setup) steps below


### Virtual Environment Setup
1. Create a virtual environment
   - `python -m venv env`

2. Activate the virtual environment
   - Windows: `env\Scripts\activate`
   - Linux: `source env/bin/activate`

3. Install the dependencies
   - `pip install -r requirements.txt`

4. Run the application
   - `python main.py`
   
5. Navigate to `http://localhost:5001/` to view the application.
6. Deactivate virtual environment with `deactivate`


### Docker Setup
1. Build the image: `docker build -t quotes .`

2. Create and start the container:
    - Windows Powershell: `docker run --name quotes -it -v ${pwd}:/code -p 5001:5001 quotes`
    - MacOS and Linux: `docker run --name quotes -it -v $(pwd):/code -p 5001:5001 quotes`

3. Start the container if it already exists: `docker start -ai quotes`

4. Navigate to `http://localhost:5001/` to view the application.


## Example .env File
A .env file will be needed to configure email reminders upon creating a quote. Here is what it should look like:
```
SENDER="<email address of sender>"
RECIPIENT="<email address of recipient>"
GMAIL_SMTP_PW="<google app password>"
APP_URL="<URL of your application>"
```
To send emails from your gmail account using google's SMTP server, create a [Google App Password](https://myaccount.google.com/apppasswords) and paste it here.