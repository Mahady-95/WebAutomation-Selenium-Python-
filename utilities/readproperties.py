import configparser
config=configparser.RawConfigParser()

config.read("C:\\Users\\User\\PycharmProjects\\DemoWebApp\\configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info', 'baseUrl')
        return url