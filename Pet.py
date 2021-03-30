class Pet:

    def __init__(self):
        self.__hp = 100
        self.__bot = 100
        self.__eat = 100
        self.__sleep = 100

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, hp):
        self.__hp = hp

    @property
    def bot(self):
        return self.__bot

    @bot.setter
    def bot(self, bot):
        self.__bot = bot

    @property
    def eat(self):
        return self.__eat

    @eat.setter
    def eat(self, eat):
        self.__eat = eat

    @property
    def sleep(self):
        return self.__sleep

    @sleep.setter
    def sleep(self, sleep):
        self.__sleep = sleep
