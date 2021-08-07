from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.navigationdrawer import NavigationLayout
from kivymd.uix.list import MDList
from kivymd.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivy.core.text import LabelBase
import requests
import webbrowser
from dijkstra import *

LabelBase.register(name="MontserratBold", fn_regular="font/Montserrat-Bold.ttf")
LabelBase.register(name="Montserrat", fn_regular="font/Montserrat-Medium.ttf")


class FactCheckerApp(MDApp):

    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass

    def build(self):
        self.file = Builder.load_file('projeto.kv')
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Amber"
        return self.file

    def press(self):
        text_1 = self.root.ids.input_box_1.text
        text_2 = self.root.ids.input_box_2.text
        answer = dijkstra(text_1)
        if answer[text_2] == float('infinity'):
            name = f"Infelizmente não encontramos uma boa rota para esses pontos :("
        else:
            name = f"A menor distância entre {text_1} e {text_2} é de {answer[text_2]} milhas nauticas"
        close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
        self.dialog = MDDialog(title='Resultado', text=name, size_hint=(0.5, 1), buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def check(self, checkbox, active):
        if active:
            self.answer = 'True'

    def check1(self, checkbox, active):
        if active:
            self.answer = 'Fake'

    def access(self):
        webbrowser.open("https://drive.google.com/file/d/1Mi-AFcJArAtvtSc354WMdS31BLtrTL67/view?usp=sharing")


if __name__ == '__main__':
    FactCheckerApp().run()