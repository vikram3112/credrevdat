import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\Dreamer\\Documents\\pythonProject1\\pythonProject\\credkartjanproject\\Configuration\\config.ini")


class Readconfig():

    @staticmethod
    def getLoginUrl():
        LoginUrl = config.get('user info', 'loginUrl')
        return LoginUrl

    @staticmethod
    def getRegistrationUrl():
        RegistrationUrl = config.get('user info', 'RegistrationUrl')
        return RegistrationUrl

    @staticmethod
    def getUsername():
        Username = config.get('user info', 'User_email')
        return Username

    @staticmethod
    def getPassword():
        Password = config.get('user info', 'Password')
        return Password
