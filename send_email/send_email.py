import smtplib

from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'rkumar@groupon.com'
PASSWORD = 'ofskspludbypeokd'

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            emails.append(a_contact.split()[0])
            names.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    names, emails = get_contacts('mycontacts.txt') # read contacts
    message_template = read_template('message_na.txt')

    # set up the SMTP server
    s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
    #s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
        #print(message)

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="Incase you missed it!"
        
        # add in the message body
        msg.attach(MIMEText(message, 'html'))
        
        # send the message via the server set up earlier.
        s.send_message(msg)
        print('Email sent to {}'.format(email))
        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
    main()


# Great post by Arjun
#https://www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/