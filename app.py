from flask import Flask
from gmail_setup import get_gmail_service
from gmail_to_db import insert_task   # your function name
import base64
from datetime import datetime

app = Flask(__name__)

def fetch_and_store_emails():
    service = get_gmail_service()

    results = service.users().messages().list(
        userId='me',
        labelIds=['INBOX', 'UNREAD'],
        maxResults=5
    ).execute()

    messages = results.get('messages', [])

    if not messages:
        print("No new emails")
        return

    for msg in messages:
        message = service.users().messages().get(
            userId='me', id=msg['id'], format='full'
        ).execute()

        headers = message['payload']['headers']
        subject = sender = ""

        for h in headers:
            if h['name'] == 'Subject':
                subject = h['value']
            if h['name'] == 'From':
                sender = h['value']

        body = ""
        if message['payload']['body'].get('data'):
            body = base64.urlsafe_b64decode(
                message['payload']['body']['data']
            ).decode('utf-8')

        insert_task(subject, body)
        print("Email stored:", subject)

@app.route("/")
def home():
    fetch_and_store_emails()
    return "Emails fetched and stored successfully!"

if __name__ == "__main__":
    app.run(debug=True)
c