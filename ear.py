import webbrowser
import speech_recognition as sr
import os
import wikipedia
import threading
from mtranslate import translate
from colorama import Fore,Style,init
from Head.Mouth import speak
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
                    if("open youtube"==translated_txt or "youtube"==translated_txt):
                        webbrowser.open_new_tab("https://www.youtube.com/")
                        speak("opening youtube")
                    elif("open microsoft365"==translated_txt or "microsoft365"==translated_txt):
                        webbrowser.open_new_tab("https://www.microsoft.com/")
                        speak("opening microsoft365")
                    elif("open google"==translated_txt or "google"==translated_txt):
                        webbrowser.open_new_tab("https://www.google.com/")
                        speak("opening google")
                    elif("open amazon"==translated_txt or "amazon"==translated_txt):
                        webbrowser.open_new_tab("https://www.amazon.com/")
                        speak("opening amazon")
                    elif("open flipkart"==translated_txt or "flipkart"==translated_txt):
                        webbrowser.open_new_tab("https://www.flipkart.com/")
                        speak("opening flipkart")
                    elif("open meesho"==translated_txt or "meesho"==translated_txt):
                        webbrowser.open_new_tab("https://www.meesho.com/")
                        speak("opening meesho")
                    elif("open insta"==translated_txt or "insta"==translated_txt):
                        webbrowser.open_new_tab("https://www.instagram.com/")
                        speak("opening instagram")
                    elif("open linkedin"==translated_txt or "linkedin"==translated_txt):
                        webbrowser.open_new_tab("https://www.linkedin.com/")
                        speak("opening linkedin")
                    elif("open email"==translated_txt or "mail"==translated_txt or "email"==translated_txt):
                        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
                        speak("opening mail")
                    elif("open weather"==translated_txt or "weather"==translated_txt or "jarvis what is the temperature now"==translated_txt):
                        webbrowser.open_new_tab("https://www.google.com/search?q=tempreture&oq=tempreture+&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQABgKGIAEMg0IAhAAGJIDGIAEGIoFMgwIAxAAGAoYsQMYgAQyCQgEEAAYChiABDIJCAUQABgKGIAEMgkIBhAAGAoYgAQyDAgHEAAYChixAxiABDIPCAgQABgKGIMBGLEDGIAEMgkICRAAGAoYgATSAQgzODcxajBqN6gCALACAA&sourceid=chrome&ie=UTF-8")
                        speak("opening weather")
                    else:
                        def search_wikipedia(query):
                            try:
                                # Fetch summary of the query
                                summary = wikipedia.summary(query, sentences=3)
                                print("Wikipedia Summary:")
                                speak(summary)
                                print(summary)
                            except wikipedia.exceptions.DisambiguationError as e:
                                print(f"Multiple results found. Please be more specific: {e}")
                            except wikipedia.exceptions.PageError:
                                print("No results found.")
                            except Exception as e:
                                print(f"An error occurred: {e}")

                        # Example: Replace 'Python programming' with your query
                        search_wikipedia(translated_txt)

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

while True:
    listen()

