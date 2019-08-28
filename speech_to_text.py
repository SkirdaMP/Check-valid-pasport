import speech_recognition as sr


# obtain path to "english.wav" in the same folder as this script.  path.join(path.dirname(path.realpath(__file__)),)
#from os import path
def SpeechToText():
    text_in_audio = ""
    for i in range(1, 7):
        AUDIO_FILE = "C:\\Users\\Skirda\\Desktop\\" + str(i) + ".wav"
        # use the audio file as the audio source
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file
        # recognize speech using Wit.ai
        # Wit.ai keys are 32-character uppercase alphanumeric strings
        WIT_AI_KEY = "BHKRRZVCRA456NELAYDKN5GB72QLVPPB"
        try:
            text_in_audio+=(r.recognize_wit(audio, key=WIT_AI_KEY))#дописать обработку полученного числа типа: если ... == "семь": то что-то
        except sr.UnknownValueError:
            return "Wit.ai could not understand audio"
        except sr.RequestError as e:
            return "Could not request results from Wit.ai service; {0}".format(e)
    return text_in_audio
