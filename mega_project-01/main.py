import pyttsx3
import speech_recognition as sr

recognizer = sr.Recognizer()

engine = pyttsx3.init()

engine.say("Hello")
engine.say("How are you?")
engine.say("Good Morning")

engine.runAndWait()