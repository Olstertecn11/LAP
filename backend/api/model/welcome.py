
class WelcomeModel:
    def __init__(self):
        self.message = "Hello World"

    def welcome(self):
        return self.message

    def welcome_post(self, request):
        return 'Hola' + request.form['username']
