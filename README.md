# Gmail AI Automation

A Python-based project that connects to the Gmail API, fetches unread emails from the inbox, and stores email information in a database using Flask.

## Features

- Connects to Gmail using the Gmail API.
- Authenticates securely using OAuth 2.0.
- Fetches up to five unread emails from the inbox.
- Extracts the sender and subject from emails.
- Decodes available email body content.
- Stores email information in a database.
- Uses Flask to trigger the email-fetching process through a web route.
- Includes sample scripts for testing GET and POST API requests.

## Technologies Used

- Python
- Flask
- Gmail API
- Google OAuth 2.0
- Google API Client
- Database integration
- Requests

## Project Structure

```text
gmail-ai-automation/
├── app.py
├── gmail_setup.py
├── gmail_to_db.py
├── db.py
├── gmail_read_test.py
├── get_api.py
├── test_api.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/Shloka369/gmail-ai-automation.git
cd gmail-ai-automation
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install Flask google-api-python-client google-auth-oauthlib google-auth-httplib2 requests
```

### 4. Configure Gmail API

1. Enable the Gmail API in the Google Cloud Console.
2. Configure OAuth consent and create OAuth client credentials.
3. Save your downloaded OAuth client file locally as `credentials.json`.
4. Keep `credentials.json` and `token.pickle` private. Never commit them to GitHub.

### 5. Run the application

```bash
python app.py
```

Open the local Flask address shown in your terminal to trigger the email-fetching process.

## How It Works

1. Flask starts the application.
2. The Gmail API authenticates the user.
3. The application retrieves up to five unread inbox emails.
4. Email details are extracted and passed to the database insertion function.
5. The application returns a success message.

## Security

- OAuth credentials and authentication tokens must remain private.
- Use environment variables for any API keys or database credentials.
- Do not commit personal emails or sensitive information to a public repository.

## Future Improvements

- Add automatic email classification using machine learning.
- Improve HTML and multipart email-body extraction.
- Add duplicate-email prevention and error handling.
- Add scheduled email fetching.
- Build a dashboard to view stored emails.
- Add automated tests and logging.

## Learning Outcomes

This project demonstrates practical experience with Python, Flask, REST APIs, Gmail API integration, OAuth authentication, and database operations.

## Author

Shloka Sonawane

GitHub: https://github.com/Shloka369
