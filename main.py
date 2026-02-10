
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        label = Label(text='بوت النشر التلقائي (مقالة يومياً)', font_size=24)
        btn_on = Button(text='تشغيل', font_size=22)
        btn_off = Button(text='إيقاف', font_size=22)
        layout.add_widget(label)
        layout.add_widget(btn_on)
        layout.add_widget(btn_off)
        return layout

if __name__ == '__main__':
    MainApp().run()
