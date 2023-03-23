import datetime
from model.Entity import Entity
from model.PrivacyPolicy import DCR, DUR, PrivacyPolicy
from model.Profile import Profile,PrivacyPolicy
from model.enumerations.Purpose import Purpose


class Generate():

    def dummyProfile() -> Profile: 
        dataUsageRules = DUR(purposes = {Purpose.WEATHER, Purpose.SEARCH},timestamp = datetime.datetime(1972, 1, 1))
        dataCommunicationRule = DCR(set(),Entity.GOOGLE,dataUsageRules)
        pilot = [PrivacyPolicy("Audio",dataCommunicationRule,set())]
        voiceFiles = ["unknown/hello.wav", "unknown/what_is_lorem_ipsum.wav"]

        profile = Profile("TestProfile", pilot, voiceFiles, [])
        return profile