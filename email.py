import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import webbrowser
import speech_recognition as sr
import os
import threading
from mtranslate import translate
from colorama import Fore,Style,init
init(autoreset=True)

def trans_hindi_to_english(txt):
    english_txt = translate(txt, to_language="en-in")
    return english_txt

def print_loop():
    while True:
        print(Fore.LIGHTGREEN_EX + "I am listening....",end="",flush=True)
        print(Style.RESET_ALL,end="",flush=True)
        print("",end="",flush=True)



def listen():
    recognizer= sr.Recognizer()
    recognizer.dynamic_energy_threshold=False
    recognizer.energy_threshold=35000
    recognizer.dynamic_energy_adjustment_damping=0.03
    recognizer.dynamic_energy_ratio=1.9
    recognizer.pause_thresholds=0.4
    recognizer.operation_timeout=None
    recognizer.pause_threshold=0.4
    recognizer.non_speaking_duration=0.3


    with sr.Microphone() as  source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print(Fore.LIGHTGREEN_EX + "i am listening...",end="",flush=True)
            try:
                audio = recognizer.listen(source,timeout=None)
                print("\r"+Fore.LIGHTBLUE_EX + "answering ...",end="",flush=True)
                recognized_txt = recognizer.recognize_google(audio).lower()
                if recognized_txt:
                    translated_txt = trans_hindi_to_english(recognized_txt)
                    data=translated_txt
                    print("\r" + Fore.BLUE + "jarvis : " + translated_txt)

                    return translated_txt
                else:
                    return ""
            except sr.UnknownValueError:
                    recognized_txt=""
            finally:
                    print("\r",end="",flush=True)


            os.system("cls" if os.name =="nt" else "clear")
            listen_thread = threading.Thread(target=listen)
            print_thread = threading.Thread(target=print_loop)
            listen_thread.start()
            print_thread.start()
            listen_thread.join()
            print_thread.join()


# Sender and receiver details
sender_email = "shuklaramakant631@gmail.com"
sender_password = "kadj kqto wszw pptn"  # NOT your normal Gmail password, use App Password!
receiver_email = "rajakharish027@gmail.com"

# Create the email
subject = listen()
body = "This is a test email sent from Python script."

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

message.attach(MIMEText(body, 'plain'))

# Connect to Gmail server and send mail
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()
    print("✅ Email sent successfully!")

except Exception as e:
    print(f"❌ Error sending email: {e}")
