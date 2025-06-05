import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from buildozer import Buildozer

Window.size = (360, 640)
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor=(1,1,1,1)
        backgroundImage = Image(source='/home/frank/Desktop/100_Days_Of_Python/churchOfGodJacksonMI/Assets/Images/IMG_6765.JPG', size_hint=(1,1), pos_hint={'x':0, 'top':1.33})
        self.add_widget(backgroundImage)
        backgroundImage2 = Image(source='/home/frank/Desktop/100_Days_Of_Python/churchOfGodJacksonMI/Assets/Images/sanct.jpg', size_hint=(1,1), pos_hint={'x':0, 'top':.66})
        self.add_widget(backgroundImage2)
        self.add_widget(Label(text='Welcome to the Church of God \nJackson Michigan!\nWhere salvation makes you a member and \nChrist is the standard.',outline_width=0.5, color='purple', halign="center",font_size=18,
            pos=(30,240),
            text_size=(300, 200),  # width and height of the area text can occupy
            size_hint=(None, None),
            size=(300, 200)))

class ChurchHoursScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        backgroundImage = Image(source='/home/frank/Desktop/100_Days_Of_Python/churchOfGodJacksonMI/Assets/Images/hours.png', size_hint=(1,1), pos_hint={'x':0, 'top':1.25})
        self.add_widget(backgroundImage)
        backgroundImage2 = Image(source='/home/frank/Desktop/100_Days_Of_Python/churchOfGodJacksonMI/Assets/Images/hours.png', size_hint=(1,1), pos_hint={'x':0, 'top':.65})
        self.add_widget(backgroundImage2)
class ChatRoomsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical')

        # Scrollable chat display
        self.chat_log = Label(size_hint_y=None, text="", valign='top', color='black')
        self.chat_log.bind(texture_size=self.update_log_height)

        scroll = ScrollView(size_hint=(1, 0.85))
        scroll.add_widget(self.chat_log)

        # Input and send button
        input_layout = BoxLayout(size_hint=(1, 0.15))
        self.input = TextInput(hint_text="Type your message", multiline=False)
        send_button = Button(text="Send", size_hint_x=0.3)
        send_button.bind(on_release=self.send_message)

        input_layout.add_widget(self.input)
        input_layout.add_widget(send_button)

        self.layout.add_widget(scroll)
        self.layout.add_widget(input_layout)
        self.add_widget(self.layout)

    def update_log_height(self, *args):
        self.chat_log.height = self.chat_log.texture_size[1]

    def send_message(self, instance):
        message = self.input.text.strip()
        if message:
            self.chat_log.text += f"\nYou: {message}"
            self.input.text = ""

class MinistryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pastor = Image(source='/home/frank/Desktop/100_Days_Of_Python/churchOfGodJacksonMI/Assets/Images/pastor.jpg', size_hint=(1,1), pos_hint={'x':0, 'top':1.33})
        self.add_widget(pastor)
        self.add_widget(Label(text="Call at (517) 782-1431\nPastor Lee Hampton", font_size=32, color='purple',outline_width=0.5))

class TestimoniesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(Label(text="FrankM: God Delivered me from 16 years of marijuana,\n 3 years of pain,\n and is making a \nhuge difference in my life!",outline_width=0.5, font_size=20, color='purple', halign="center",
            pos=(30,333),
            text_size=(300, 200),  # width and height of the area text can occupy
            size_hint=(None, None),
            size=(300, 200),))
        
        self.add_widget(Label(text="Anonymous: I got delivered from drinking\n Salvation never felt better!", outline_width=0.5,font_size=20, color='purple', halign="center",
            pos=(30,500),
            text_size=(300, 200),  # width and height of the area text can occupy
            size_hint=(None, None),
            size=(300, 200),))

        self.add_widget(Label(text="Anonymous: I got delivered from drinking\n Salvation never felt better!", outline_width=0.5,font_size=20, color='purple', halign="center",
            pos=(30,200),
            text_size=(300, 200),  # width and height of the area text can occupy
            size_hint=(None, None),
            size=(300, 200),))

# Main layout
class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        # Screen Manager
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name='home'))
        self.sm.add_widget(ChurchHoursScreen(name='church_hours'))
        self.sm.add_widget(ChatRoomsScreen(name='chat_rooms'))
        self.sm.add_widget(MinistryScreen(name='ministry'))
        self.sm.add_widget(TestimoniesScreen(name='testimonies'))

        # Top Navigation
        nav_bar = BoxLayout(size_hint_y=None, height=60)

        btn_specs = [
            ('Home', 'home'),
            ('Church Hours', 'church_hours'),
            ('Chat Rooms', 'chat_rooms'),
            ('Ministry', 'ministry'),
            ('Testimonies', 'testimonies')
        ]

        for label, screen_name in btn_specs:
            btn = Button(
                text=label,
                background_color=(0.5, 0, 0.5, 1),  # purple RGBA
                color=(1, 1, 1, 1),  # white text
                font_size=11,
                width=180,
            )
            btn.bind(on_release=lambda btn, name=screen_name: self.change_screen(name))
            nav_bar.add_widget(btn)

        self.add_widget(nav_bar)
        self.add_widget(self.sm)

    def change_screen(self, screen_name):
        self.sm.current = screen_name

class ChurchApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    ChurchApp().run()