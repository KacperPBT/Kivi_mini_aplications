import my_pdf
from time import sleep
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (700,150)

Builder.load_file('main.kv')

class MyLayout(Widget):
    def press(self):
        path1 = self.ids.path1.text
        path2 = self.ids.path2.text
        if my_pdf.sprawdz_plik_pdf(path1) and my_pdf.sprawdz_plik_pdf(path2):
            my_pdf.merge_pdfs(path1,path2,"merged.pdf")
            self.ids.path1.text = ""
            self.ids.path2.text = ""
        if not my_pdf.sprawdz_plik_pdf(path1):
            self.ids.path1.text = "Nie prawidłowe"
        if not my_pdf.sprawdz_plik_pdf(path2):
            self.ids.path2.text = "Nie prawidłowe"
        
    def un_press(self):
        sleep(0.5)
        if self.ids.path1.text == "Nie prawidłowe":
            self.ids.path1.text = ""
        if self.ids.path2.text == "Nie prawidłowe":
            self.ids.path2.text = ""

class PDF_MergerApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    PDF_MergerApp().run()