import re


def find_email(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    emails = re.findall(email_pattern, text)

    text_with_email_placeholder = re.sub(email_pattern, 'EMAIL_ADDRESS', text)

    return emails, text_with_email_placeholder


if __name__ == '__main__':
    emails, text_with_email_placeholder = find_email('nicolas@gmail.com')
    print(emails, text_with_email_placeholder)
