from bardapi import Bard
import wikipedia
import pyautogui
import pyjokes
import pyttsx3
import webbrowser as wb
import datetime
import tkinter
import os
import customtkinter
from pytube import YouTube

print('Developed with hard work by Tech Extremer aka Goutham Kumar A')

# Extremer Assistant by Goutham Kumar A
"""
Dependencies

Python 3.8
and
Run this code in terminal

pip install bardapi wikipedia playsound pyautogui pyjokes pyttsx3 customtkinter pytube speechrecognition opencv-contrib-python cvzone mediapipe

That's It ! Now enjoy Extremer Assistant

"""

print('Which voice do you want.')
a = int(input('Enter 0 for Male and 1 for Female '))

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[a].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def notepad():
    from kivy.app import App
    from kivy.uix.textinput import TextInput

    class TechApp(App):
        def build(self):
            return TextInput(text='Start Typing')

    if __name__ == '__main__':
        TechApp().run()


def print_commands():
    print('Cal - Opens Calculator')
    print('HanMouse - A Beta Virtual Mouse')
    print('Bard - Opens Built-In Google Bard')
    print('Photo - Show you Hand and it takes your photo')
    print('My Web - Opens a Random Website of mine')
    print('Time - Tells you the time')
    print('Search - Searches Info for you in Wikipedia')
    print('Joke - Tells you a Joke')
    print('Snap - Opens Built-in SnapChat')
    print('Youtube - Opens Youtube')
    print('ChatGPT - Opens ChatGPT')
    print('Tables - Tells the tables for you')
    print('SBM - Speak Back To Me')
    print('Birthday - Tells you a Happy Birthday Song')
    print('TP - Just Prints what you input')
    print('YT Down - A GUI Youtube Downloader')
    print('Antifragile - Plays AntiFragile')
    print('Believer - Plays Believer')
    print('Unstoppable - Plays Unstoppable')
    print('Shape of you  - Plays Shape of you')
    print('Memories - Plays Memories')
    print('Hymn For The Weekend - Plays Hymn For The Weekend')
    print('Uri Medley - Plays Uri Medley')
    print('The Boys - Plays The Boys')
    print('Finish Line - Plays Finish Line')
    print('Feel Invincible - Plays Feel Invincible')
    print('Nee Sigoovaregu - Plays Nee Sigoovaregu')
    print('Kannada Bhaashe - Plays Kannada Bhaashe')
    print('Illegal Weapon - Plays Illegal Weapon')
    print('Kesariya - Plays Kesariya')
    print('Enemy - Plays Enemy')
    print('Centuries - Plays Centuries')
    print('Insta - Opens Instagram')
    print('SnapChat - Opens Official SnapChat')
    print('Exit - Closes the Assistant')


def screen_record():
    from PIL import ImageGrab
    import numpy as np
    import cv2
    from win32api import GetSystemMetrics

    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video = cv2.VideoWriter('Final.mp4', fourcc, 20.0, (width, height))

    while True:
        img = ImageGrab.grab(bbox=(0, 0, width, height))
        img_np = np.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        cv2.imshow('Extremer Recorder', img_final)
        video.write(img_final)
        if cv2.waitKey(10) == ord('a'):
            break


def time_greeting():
    time = datetime.datetime.now().strftime('%I:%M %p')
    print('Current Time is ' + time)
    talk('Current Time is ' + time)


def greeting():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        print('Good Morning')
        talk('Good Morning')

    elif 12 <= hour < 16:
        print('Good Afternoon')
        talk('Good Afternoon')

    elif 16 <= hour < 21:
        print('Good Evening')
        talk('Good Evening')

    else:
        print('Have A Good Night')
        talk('Have A Good Night')


greeting()
time_greeting()
talk('Enter Password')
passkey = str(input('Enter Password '))


def main_ext():
    def hanmou():
        import cv2
        import mediapipe as mp
        cap = cv2.VideoCapture(0)
        hand_detector = mp.solutions.hands.Hands()
        drawing_utils = mp.solutions.drawing_utils
        screen_width, screen_height = pyautogui.size()
        while True:
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            frame_height, frame_width, _ = frame.shape
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            output = hand_detector.process(rgb_frame)
            hands = output.multi_hand_landmarks
            if hands:
                for hands in hands:
                    drawing_utils.draw_landmarks(frame, hands)
                    landmarks = hands.landmark
                    for id_card, landmarks in enumerate(landmarks):
                        x = int(landmarks.x * frame_width)
                        y = int(landmarks.y * frame_height)
                        if id_card == 8:
                            cv2.circle(img=frame, center=(x, y), radius=10, color=(69, 196, 85))
                            index_x = screen_width / frame_width * x
                            index_y = screen_height / frame_height * y
                            pyautogui.moveTo(index_x, index_y)

            cv2.imshow('Extremer Mouse', frame)
            cv2.waitKey(1)

    def snap():
        import cvzone
        import cv2
        cap = cv2.VideoCapture(0)
        cascade = cv2.CascadeClassifier('snap/haarcascade_frontalface_default.xml')
        overlay = cv2.imread('snap/cool.png', cv2.IMREAD_UNCHANGED)
        while True:
            _, frame = cap.read()
            gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = cascade.detectMultiScale(gray_scale)
            for (x, y, w, h) in faces:
                # cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)
                overlay_resize = cv2.resize(overlay, (int(w * 1.5), int(h * 1.5)))
                frame = cvzone.overlayPNG(frame, overlay_resize, [x - 45, y - 75])
            cv2.imshow('Snap Dude', frame)
            if cv2.waitKey(10) == ord('q'):
                break

    talk('Correct Password Redirecting you to Extremer Assistant')
    talk('If you want to read Manual Press 1 or else press 2')
    redirector = str(input('if you want to read Manual Press 1 or else press 2  '))

    if redirector == '1':
        talk('Printing Available Commands')
        print_commands()
    else:
        print('Proceeding to Extremer Assistant')
        talk('Proceeding to Extremer Assistant')

    while True:
        talk('Tell me your Command')
        asd = str(input('Tell me your Command ? '))

        asdf = asd.lower()

        if 'play' in asdf:
            import pywhatkit
            talk(asdf)
            redirector = asdf.replace('play', '')
            print('Playing ' + redirector, "On Youtube")
            pywhatkit.playonyt(redirector)
            print('Check your Browser')

        def bard():
            a_var = 'Welcome To Google Bard'
            print(a_var)
            talk(a_var)
            talk('What Do You Want to Search Today')
            sea = str(input('What Do You Want to Search Today'))
            token = 'WghHqdJl9DDga7THj2XW76VcJklNfqqGX2g6Vv5gFZgkbl-qQvE8i8Ellr2GHzwyZS99Zw.'
            bard_api = Bard(token=token)
            var = bard_api.get_answer(sea)['content']
            print(var)

        def camera():
            import cv2
            import mediapipe as mp
            cap = cv2.VideoCapture(0)
            hand_dec = mp.solutions.hands.Hands()
            while True:
                _, frame = cap.read()
                output = hand_dec.process(frame)
                frame = cv2.flip(frame, 1)
                hands = output.multi_hand_landmarks
                cv2.imshow('Camera', frame)
                cv2.waitKey(10)
                time_now = datetime.datetime.now().strftime('%Y-%m-%d-%I-%M-%S-%p')
                file = f'Extremer Selfie-{time_now}.png'
                if hands:
                    print('Done at   ' + time_now)
                    cv2.imwrite(file, frame)

        def cal():
            # Extremer Calculator
            talk('Hello')
            print("Welcome to Extremer Calculator")
            talk('Welcome to Extremer Calculator')
            print('')
            print('Were do you want to go to')
            print('')
            print('Press 1 to go to Basic Calculator')
            print('Press 2 to go to the Formula section')
            talk(' ')
            talk("Tell me the number and I will teleport you to that world")
            main = int(input("Tell me the number and I will teleport you to that world🫠😁😊?   "))

            def basic():
                talk('If you want GUI Press 1 or else press 2')
                redirect = str(input('If you want GUI Press 1 or else press 2'))

                def basic_console():
                    print("Basic Calculator Py")
                    talk('Welcome to Basic Calculator')
                    talk(' ')
                    print('Available Operators  +  -  /  *')
                    talk('Available Operators are Add, Subtract, Multiply and Divide .')
                    o = input("Choose Operator")

                    def add():
                        first_num = int(input("Enter First Number  "))
                        b = int(input("Enter Second Number  "))
                        a_var = (b + first_num)
                        print(a_var)
                        talk(a_var)

                    if o == "+":
                        add()

                    def sub():
                        first = int(input("Enter First Number  "))
                        b = int(input("Enter Second Number  "))
                        print(b - first)
                        talk(b - first)

                    if o == "-":
                        sub()

                    def mul():
                        first_num = int(input("Enter First Number  "))
                        b = int(input("Enter Second Number  "))
                        print(b * first_num)
                        talk(b * first_num)

                    if o == "*":
                        mul()

                    def div():
                        first = int(input("Enter First Number  "))
                        b = int(input("Enter Second Number  "))
                        print(b / first)
                        talk(b / first)

                    if o == "/":
                        div()

                def basic_gui():
                    from kivy.app import App
                    from kivy.uix.boxlayout import BoxLayout
                    from kivy.uix.button import Button
                    from kivy.uix.textinput import TextInput

                    class MainApp(App):
                        def build(self):
                            self.operators = ["/", "*", "+", "-"]
                            self.last_was_operator = None
                            self.last_button = None
                            main_layout = BoxLayout(orientation="vertical")
                            self.solution = TextInput(
                                multiline=False, readonly=True, halign="right", font_size=55
                            )
                            main_layout.add_widget(self.solution)
                            buttons = [
                                ["7", "8", "9", "/"],
                                ["4", "5", "6", "*"],
                                ["1", "2", "3", "-"],
                                [".", "0", "C", "+"],
                            ]
                            for row in buttons:
                                h_layout = BoxLayout()
                                for label in row:
                                    button = Button(
                                        text=label,
                                        pos_hint={"center_x": 0.5, "center_y": 0.5},
                                    )
                                    button.bind(on_press=self.on_button_press)
                                    h_layout.add_widget(button)
                                main_layout.add_widget(h_layout)

                            equals_button = Button(
                                text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
                            )
                            equals_button.bind(on_press=self.on_solution)
                            main_layout.add_widget(equals_button)

                            return main_layout

                        def on_button_press(self, instance):
                            current = self.solution.text
                            button_text = instance.text

                            if button_text == "C":
                                # Clear the solution widget
                                self.solution.text = ""
                            else:
                                if current and (
                                        self.last_was_operator and button_text in self.operators):
                                    # Don't add two operators right after each other
                                    return
                                elif current == "" and button_text in self.operators:
                                    # First character cannot be an operator
                                    return
                                else:
                                    new_text = current + button_text
                                    self.solution.text = new_text
                            self.last_button = button_text
                            self.last_was_operator = self.last_button in self.operators

                        def on_solution(self, instance):
                            text = self.solution.text
                            if text:
                                solution = str(eval(self.solution.text))
                                self.solution.text = solution

                    if __name__ == "__main__":
                        app = MainApp()
                        app.run()

                if redirect == '1':
                    basic_gui()

                elif redirect == '2':
                    basic_console()

            def formula():

                print('')
                print("Available Formula's")
                print("Circle Sector")
                print("")
                print("1 for Area")
                print("2 for Perimeter")
                print('')
                print("Square Sector")
                print("Press 3 to find area of a square")
                print("Press 4 to find the Perimeter of a square")
                print('')
                print('Rectangle Area')
                print("Press 5 to find the area of a Rectangle")
                print("Press 6 to find the Perimeter of a Square")
                print('Press 7 to find profit')

                acer = str(input("Which formula do you wish to execute ? "))

                def carea():
                    ca = float(input("Tell me the raduis of the Circle"))
                    p = 22 / 7
                    ans = p * ca ** 2
                    print(ans)
                    talk(int(ans))

                if acer == "1":
                    carea()

                def cperi():
                    cp = float(input("Tell me the raduis of the Circle"))
                    cpans = 22 / 7
                    pans = 2 * cpans * cp
                    print(pans)
                    talk(int(pans))

                if acer == "2":
                    cperi()

                def sqarea():
                    sa = float(input("Tell me side length of the square"))
                    cans = sa * sa
                    print(cans)
                    talk(int(cans))

                if acer == "3":
                    sqarea()

                def sqperi():
                    spe = float(input("Tell me side length of the square"))
                    spans = spe * 4
                    print(spans)
                    talk(int(spans))

                if acer == "4":
                    sqperi()

                def recarea():
                    rab = float(input("Tell my the Breadth of the Rectangle"))
                    ral = float(input("Tell my the Length of the Rectangle"))
                    rans = rab * ral
                    print(rans)
                    talk(int(rans))

                if acer == "5":
                    recarea()

                def recperi():
                    rperb = float(input("Tell my the Breadth of the Rectangle"))
                    rperl = float(input("Tell my the Length of the Rectangle"))
                    rpans = (rperb + rperl) * 2
                    print(rpans)
                    talk(int(rpans))

                if acer == "6":
                    recperi()

                def profit():
                    sp = int(input('Enter Selling Price'))
                    cp = int(input('Enter Cost Price'))
                    fin = sp - cp
                    print(fin)
                    talk(int(fin))

                if acer == '7':
                    profit()

                def loss():
                    sp = int(input('Enter Selling Price'))
                    cp = int(input('Enter Cost Price'))
                    fin = cp - sp
                    print(fin)
                    talk(int(fin))

                if acer == '8':
                    loss()

                def profitper():
                    profit_1 = int(input('Enter Profit'))
                    cp = int(input('Enter Cost Price'))
                    profit_1 = (profit_1 / cp) * 100
                    print(profit_1 + '%')
                    talk(int(profit_1 + '%'))

                if acer == '9':
                    profitper()

                def losper():
                    loss_1 = int(input('Enter Loss'))
                    cp = int(input('Enter Cost Price'))
                    profit_2 = (loss_1 / cp) * 100
                    print(profit_2 + '%')
                    talk(int(profit_2 + "%"))

                if acer == '10':
                    losper()

                # def increadecreaper():
                #   Difference = int(input('Enter Difference between'))

            if main == 1:
                basic()

            if main == 2:
                formula()

        def tables():
            print('Table Generator')
            talk('Table Generator')
            numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
            num = int(input('Which Table do you want'))
            for number in numbers:
                result = num * int(number)
                random = (str(result))
                print(random)
                talk(random)

        def play(path):
            import cv2
            from playsound import playsound
            playsound(path)
            play_show = 'Assests/SP.png'
            cv2.imshow('Extremer Assistant', play_show)

        def ytdown():
            def start_download():
                try:
                    ytlink = link.get()
                    yt_down = YouTube(ytlink, on_progress_callback=on_progress)
                    video = yt_down.streams.get_by_resolution(resolution='720')
                    video.download()
                    des = yt_down.description
                    dis.configure(text='des')
                    des.update()
                    title.configure(text=yt_down.title, text_color='white')
                    finish_label.configure(text="Download Finish")
                    finish_label.configure(text='Download Complete', text_color='green')
                except:
                    finish_label.configure(text='Invalid URL', text_color='red')

            def on_progress(stream, chunk, bytes_remaining):
                total_size = stream.filesize
                bytes_downloaded = total_size - bytes_remaining
                percentofcomp = bytes_downloaded / total_size * 100
                per = str(int(percentofcomp))
                p_percent.configure(text=per + '%')
                p_percent.update()

                # Updating GUI Progress Bar
                progress_bar.set(float(percentofcomp) / 100)

            # Theme Settings
            customtkinter.set_appearance_mode('Light')
            customtkinter.set_default_color_theme('blue')

            # App Framework
            app = customtkinter.CTk()
            app.geometry('720x480')
            app.title('Extremer YT Downloader')

            # Adding UI Stuff
            title = customtkinter.CTkLabel(app, text='Insert YT link to download')
            title.pack(padx=10, pady=10)

            # Input Link
            url_var = tkinter.StringVar()
            link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
            link.pack()

            # Download Finished
            finish_label = customtkinter.CTkLabel(app, text='')
            finish_label.pack()

            # Progress Bar
            p_percent = customtkinter.CTkLabel(app, text="0%")
            p_percent.pack()

            progress_bar = customtkinter.CTkProgressBar(app, width=400)
            progress_bar.set(0)
            progress_bar.pack(padx=10, pady=10)

            # Buttons
            download = customtkinter.CTkButton(app, text='Extremer Download', command=start_download)
            download.pack(padx=10, pady=10)

            # Description
            dis = customtkinter.CTkLabel(app, text='Description Here')
            dis.pack(padx=10, pady=10)

            # Running the App
            app.mainloop()

        if 'photo' in asdf:
            print('Press a to stop taking Photos')
            print('The Photos you take will be saved where you are running this file from ')
            print('Show your Hand to take Photos')
            camera()

        elif 'my web' in asdf:
            wb.open('https://sites.google.com/view/gamer-kings/')

        elif 'time' in asdf:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print('Current Time is ' + time)
            talk('Current Time is ' + time)
        elif 'search' in asdf:
            df = asdf.replace('search ', '')
            lines_of_info = int(input('How many Lines of Info do you Want'))
            info = wikipedia.summary(df, lines_of_info)
            print(info)
            talk(info)

        elif 'joke' in asdf:
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)

        elif 'youtube' in asdf:
            print('Opening Youtube')
            talk('opening Youtube')
            print('Check your default browser')
            talk('Check your default browser')
            wb.open('https://www.youtube.com/')

        elif 'chatgpt' in asdf:
            print('Opening ChatGPT')
            talk('opening ChatGPT')
            print('Check your default browser')
            talk('Check your default browser')
            wb.open('https://chat.openai.com/')

        elif 'insta' in asdf:
            print('Opening Instagram')
            talk('opening Instagram')
            talk('Check your default browser')
            print('Check your default browser')
            wb.open('https://www.instagram.com/')

        elif 'cal' in asdf:
            cal()

        elif 'snapchat' in asdf:
            print('Opening SnapChat')
            talk('opening Snap Chat')
            talk('Check your default browser')
            print('Check your default browser')
            wb.open('https://www.snapchat.com/')

        elif 'snap' in asdf:
            snap()

        elif 'tables' in asdf:
            tables()
        elif 'yt down' in asdf:
            ytdown()

        elif 'tp' in asdf:
            tp = str(input('What do you want me to print'))
            print(tp)

        elif 'birthday' in asdf:
            play('song/Happy Birthday.mp3')

        elif 'bard' in asdf:
            bard()

        elif 'hanmouse' in asdf:
            hanmou()

        elif 'centuries' in asdf:
            play('song/Centuries.mp3')

        elif 'enemy' in asdf:
            play('song/Enemy.mp3')

        elif 'kesariya' in asdf:
            play('song/Kesariya.mp3.mp3')

        elif 'illegal weapon' in asdf:
            play('song/Illegal Weapon.mp3')

        elif 'kannada bhaashe' in asdf:
            play('song/Kannada Bhaashe.mp3')

        elif 'commands' in asdf:
            print_commands()

        elif 'nee sigoovaregu' in asdf:
            play('song/Nee Sigoovaregu.m4a')

        elif 'feel invincible' in asdf:
            play('song/Feel Invincible.mp3')

        elif 'finish line' in asdf:
            play('song/Finish Line.mp3.mp3')

        elif 'the boys' in asdf:
            play('song/The Boys.mp3')

        elif 'shutdown' in asdf:
            main_2 = str(input('Enter Time for Trigger'))
            if os.name == "nt":
                os.system('shutdown -s -t ' + main_2)
            else:
                os.system('shutdown -s -t ' + main_2)

        elif 'restart' in asdf:
            main_2 = str(input('Enter Time for Trigger'))
            if os.name == "nt":
                os.system('shutdown -r -t ' + main_2)
            else:
                os.system('shutdown -r -t ' + main_2)

        elif 'notepad' in asdf:
            notepad()

        elif 'hibernate' in asdf:
            if os.name == "nt":
                os.system('shutdown -h')
            else:
                os.system('shutdown -h')

        elif 'uri medley' in asdf:
            os.system('vlc %USERPROFILE%\\Extremer Assistant')

        elif 'hymn for the weekend' in asdf:
            play('song/hftw.mp3')

        elif 'memories' in asdf:
            play('song/memories.mp3')

        elif 'shape of you' in asdf:
            play('song/shape_of_you.mp3')

        elif 'unstoppable' in asdf:
            play('song/unstoppable.mp3')

        elif 'believer' in asdf:
            play('song/believer.mp3')

        elif 'antifragile' in asdf:
            play('song/antifragile.mp3')

        elif 'exit' in asdf:
            thankyou = 'Thank You For using Extremer Assistant'
            print(thankyou)
            talk(thankyou)
            exit(420)

        elif 'sbm' in asdf:
            talk('What do you want me to say ?')
            asd_var = str(input('What do you want me to say ?'))
            talk(asd_var)

        elif 'screen record' in asdf:
            screen_record()

        else:
            b_var = 'Maybe Command not defined, or unexpected error please try again, or read available commands list'
            print(b_var)
            talk(b_var)

        # Myself, Goutham the developer of this code will be available at tech.gk.official@gmail.com
        # Graphical Version will be available soon


if passkey == 'ILE':
    main_ext()


elif passkey == '032010':
    print('Opening Password Web')
    talk('Opening Password Web')
    print('Password = ILE')


else:
    talk('Wrong Password')
    talk('Try Again')
    password = str(input('Try Again '))
    if password == 'ILE':
        main_ext()
    else:
        print('Wrong Password')
        talk('Wrong Password')
        print('Contact Goutham')
        talk('Contact Goutham')
        exit(420)

"""
Logs are Written here from 12/6/2023

12/6/2023 = Created a new GUI Calculator and added it under Extremer Calculator(cal), Fixed a few bugs around in input spaces
Created a Playsound definition and got errors have to fix it
"""
