import pyttsx3


def laugh():
    engine = pyttsx3.init()
    engine.say("ha ha ha  ha  ha ha ha")
    engine.runAndWait()


laugh()


def greet():
    engine = pyttsx3.init()
    engine.say("Good day, How may I help you?")
    engine.runAndWait()


greet()
