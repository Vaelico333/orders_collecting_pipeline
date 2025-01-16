import imaplib
import email
from email.header import decode_header

def read_emails():
    # Conectar al servidor de correo
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login("your_email@gmail.com", "your_password")
    mail.select("inbox")

    # Buscar emails no leídos
    status, messages = mail.search(None, 'UNSEEN')
    email_ids = messages[0].split()

    emails = []
    for email_id in email_ids:
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else "utf-8")
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True).decode()
                            emails.append((subject, body))
                else:
                    body = msg.get_payload(decode=True).decode()
                    emails.append((subject, body))
    return emails