from kivy.app import App
from kivy.lang import Builder
class LoginApp(App):
    def build(self):
        print("LoginApp is running")
if __name__ == "__main__":
    app = LoginApp()
    app.run()