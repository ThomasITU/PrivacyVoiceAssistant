import datetime
from model.Entity import Entity
from model.PrivacyPolicy import DCR, DUR, PrivacyPolicy
from model.Profile import Profile,PrivacyPolicy
from model.enumerations.Purpose import Purpose


class Generate():

    def dummyProfile() -> Profile: 
        dataUsageRules = DUR(purposes = {Purpose.WEATHER, Purpose.SEARCH},timestamp = datetime.datetime(1972, 1, 1))
        dataCommunicationRule = DCR({},Entity.GOOGLE,dataUsageRules)
        pilot = PrivacyPolicy("Audio",{dataCommunicationRule},{})
        voiceFiles = "unknown"

        profile = Profile("Test Profile", policy=pilot, voiceSamples=voiceFiles)
        return profile