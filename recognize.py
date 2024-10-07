import speech_recognition as sr

# Online
def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Please say something... ")

        audio = r.listen(source)

        try:
            print(f'You have said: {r.recognize_google(audio)}')

        except Exception as e:
            print(f'Error: {str(e)}')

if __name__ == "__main__":
    main()