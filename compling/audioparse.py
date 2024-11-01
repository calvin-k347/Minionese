import speech_recognition as sr

recognizer = sr.Recognizer()

def transcribe(path):
    with sr.AudioFile(path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.RequestError as e:
            return e
        
print(transcribe("C:/Users/clark/OneDrive/Documents/Minionese-1/my-vue-app/src/assets/Minionese Data/buhdiz.wav"))