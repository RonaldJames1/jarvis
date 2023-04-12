import subprocess
import webbrowser
import os
import nltk
import deeplake
import speech_recognition as sr
import git

nltk.download('punkt')
from nltk.tokenize import word_tokenize

ds_train = deeplake.load('hub://activeloop/LibriSpeech-train-clean-360')
ds_test = deeplake.load('hub://activeloop/LibriSpeech-test-clean')
ds_dev = deeplake.load('hub://activeloop/LibriSpeech-dev-clean')

def listen_command():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("Google Speech Recognition thinks you said: " + text)
            tokens = word_tokenize(text)
            if 'open Google' in text:
                webbrowser.open('https://www.google.com')
            elif 'open YouTube' in text:
                webbrowser.open('https://www.youtube.com')
            elif 'open LinkedIn' in text:
                webbrowser.open('https://www.linkedin.com')
            elif 'open Twitter' in text:
                webbrowser.open('https://www.twitter.com')
            elif 'iClone' in text:
                launch_iclone()
            elif 'Spline' in text:
                launch_spline()
            elif 'tell me a joke' in text:
                tell_joke()
            elif 'GitHub' in text:
                access_github()
            else:
                print("Sorry, I didn't understand the command. Please try again.")

        except sr.UnknownValueError:
            print("Sorry, I could not understand audio. Please try again.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

def launch_iclone():
    iclone_path = r'C:\Program Files\Reallusion\iClone 8\Bin64\iClone.exe'
    subprocess.Popen([iclone_path])

def launch_spline():
    webbrowser.open("https://spline.design/")

def tell_joke():
    print("Why don't scientists trust atoms? Because they make up everything!")

def access_github():
    print("What do you want me to do on GitHub?")
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        text = r.recognize_google(audio)
        if 'clone' in text:
            clone_repository()
        elif 'push' in text:
            push_to_repository()
        elif 'pull' in text:
            pull_from_repository()
        else:
            print("Sorry, I didn't understand the command. Please try again.")
            access_github()

    except sr.UnknownValueError:
        print("Sorry, I could not understand audio. Please try again.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except Exception as e:
        print("An error occurred. Please try again. Error message: ", e)

def clone_repository():
    repo_url = "https://github.com/opencog/opencog"
    target_dir = "opencog"
    try:
        git.Repo.clone_from(repo_url, target_dir)
        print("Repository cloned successfully.")
    except Exception as e:
        print("An error occurred while cloning repository. Error message: ", e)

def pull_from_repository():
    try:
        repo = git.Repo('openc')








       
