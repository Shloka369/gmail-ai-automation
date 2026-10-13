from gmail_setup import get_gmail_service
import gmail_setup
import base64

# THIS LINE ONLY TELLS WHICH FILE PYTHON IS USING
print("Using gmail_setup from:", gmail_setup.__file__)

def read_emails():
    service = get_gmail_service()

    results = service.users().messages().list(
        userId='me',
        labelIds=['INBOX'],
        maxResults=5
    ).execute()

    messages = results.get('messages', [])

    if not messages:
        print("No emails found")
        return

    for msg in messages:
        message = service.users().messages().get(
            userId='me',
            id=msg['id'],
            format='full'
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
            ).decode('utf-8', errors='ignore')

        print("\n----- EMAIL -----")
        print("From:", sender)
        print("Subject:", subject)
        print("Body:", body[:300])
        print("-----------------")

if __name__ == "__main__":
    read_emails()
