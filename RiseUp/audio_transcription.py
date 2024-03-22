import speech_recognition as sr

def transcript_audio_portuguese():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        print('Diga alguma coisa...')
        audio = mic.listen(source)
        try:
            frase = mic.recognize_google(audio,language='pt-BR')
            print('Transcription: ' + frase)
        except:
            print('It was not possible to understand... Try again!')
        return frase
    
transcript_audio_portuguese()

def transcript_audio_english():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        print('Diga alguma coisa...')
        audio = mic.listen(source)
        try:
            frase = mic.recognize_google(audio,language='en-US')
            print('Transcription: ' + frase)
        except:
            print('It was not possible to understand... Try again!')
        return frase
    