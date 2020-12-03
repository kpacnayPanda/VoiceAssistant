import os
import time
import playsound
import pyttsx3
import speech_recognition as sr
from gtts import gTTS

flag = True


def speak(text):
    tts = pyttsx3.init()
    rate = tts.getProperty('rate')  # Скорость произношения
    tts.setProperty('rate', rate - 30)

    volume = tts.getProperty('volume')  # Громкость голоса
    tts.setProperty('volume', volume + 0.9)

    voices = tts.getProperty('voices')

    # Задать голос по умолчанию
    tts.setProperty('voice', 'ru')

    # Попробовать установить предпочтительный голос
    for voice in voices:
        if voice.name == 'Anna':
            tts.setProperty('voice', voice.id)

    tts.say(text)
    tts.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Настраиваюсь...")
        r.adjust_for_ambient_noise(source, duration=1)
        print('Слушаю...')
        audio = r.listen(source)
        said = ""
        print('Услышала...')
        try:
            said = r.recognize_google(audio, language='ru-RU')
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said


speak("Добрый день, я вас слушаю")

while flag:
    text = get_audio()
    if ("Привет" or "привет") in text:
        speak("привет чупакабра!")

    if ("тебя" and "зовут") in text:
        speak("Привет, меня зовут ПЯТНИЦА")
    if ("Выключись" or "отключись") in text:
        speak("Отключаюсь, до встречи")
        flag = False


