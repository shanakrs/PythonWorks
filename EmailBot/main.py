import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def get_information():
    try:
        with sr.Microphone() as source:
            print('Listening')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('Fill your email id', 'Fill your Password')  # please replace corresponding text with information
    # i.e. sender email id

    email = EmailMessage()
    email['From'] = 'multicloudpractice@gmail.com'  # Please replace with  sender email id
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'John': 'xxxxxxxx@gmail.com',  # Please replace with  receiver email id
    'Alex': 'xxxxxxxx@gmail.com',  # Please replace with  receiver email id
}


def get_email_info():
    talk('To whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)

    talk('Tell me the text in your email')
    message = get_info()

    talk('What is the subject of your email')
    subject = get_info()

    send_email(receiver, subject, message)

    talk('Your email is sent')
    talk('Do you want to send more email')
    send_more = get_info()
    print(send_more)
    if 'yes' in send_more:
        get_email_info()


get_email_info()
