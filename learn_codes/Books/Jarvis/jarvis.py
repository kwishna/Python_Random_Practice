import pyttsx3 as speaker
import speech_recognition as listener


# engine = speaker.init()
# a = engine.getProperty('voices')
# for v in a:
#     print(v)
# engine.say("Hello Sir")
# engine.runAndWait()


class FirstClass:

    def __init__(self, engine):
        self.engine = speaker.init(engine)
        voices = self.engine.getProperty('voices')
        print(voices[0], voices[1])
        self.engine.setProperty('voice', voices[0].id)

    def listen(self, instruction):
        pass

    def greet(self):
        self.speak("Hello Sir, How May I Help You?")

    def speak(self, output):
        self.engine.say(output)
        self.engine.runAndWait()

    def takeInput(self):
        r = listener.Recognizer()
        source = listener.Microphone
        self.speak("Please Give Me Instruction. I Am Listening...")
        print("Listening You...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio, 'en-in')

        except Exception as e:
            print("Nothing Is Listened!!")
            return None

        return query

if __name__ == '__main__':
    obj = FirstClass('sapi5')
    while True:
        obj.greet()
        query = obj.takeInput()
        obj.speak("You Just Said..", query)


