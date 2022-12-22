import requests,os
# See and Enjoy ;)
# Apis are public to use.

class Ai:

    def __init__(self):
        self.main_api = "https://reback.ml/v1/api/make/"
        self.main_api2 = "https://reback.ml/"
    def image_to_text(self,url=None):
        """
        You can get text in image, only URLS!
        :param url:
        :return: JSon response
        """
        try:
            r = requests.get(self.main_api2+"as",params={"url":url,})
            if r.status_code ==200:
                self.code = r.json()['text']
                return {"error":None,"text":self.code}
            else:
                return {"error":True,"message":"Unknown error, maybe server down."}
        except Exception as e:
            return {"error":e}
    def word_mean(self,word=None):
        """
        Get word meaning and get example to use it.
        :param word: 
        :return: JSon response
        """
        try:
            r = requests.get(self.main_api2+"mean",params={"word":word})
            if r.status_code ==200:
                self.code = r.json()['examples']
                return {"error":None,"mean":self.code}
            else:
                #print(r.text)
                return {"error":True,"message":"Unknown error, maybe server down."}
        except Exception as e:
            return {"error":e}
    def chat(self,message=None):
        """
        Chat with an ai.
        :param message:
        :return Json response
        """
        try:
            r = requests.get(self.main_api2+"chat",params={"message":message})
            if r.status_code ==200:
                self.code = r.json()['reply']
                return {"error":None,"reply":self.code}
            else:
                #print(r.text)
                return {"error":True,"message":"Unknown error, maybe server down."}
        except Exception as e:
            return {"error":e}
    def code_gen(self,prompt=None,lang=None):
        """
        Prompt to Code, (code generateor).
        :param prompt: 
        :param lang: 
        :return: JSon response
        """
        try:
            r = requests.get(self.main_api,params={"prompt":prompt,"lang":lang,})
            if r.status_code ==200:
                self.code = r.json()['code']
                return {"error":None,"code":self.code}
            else:
                #print(r.text)
                return {"error":True,"message":"Unknown error, maybe server down."}
        except Exception as e:
            return {"error":e}
# print(Ai().image_to_text("https://telegra.ph//file/3381da14831562cb2dd0e.png"))
# print(Ai().code_gen(prompt="for loop 100 with hello world after end loop print done",lang="lua"))
# print(Ai().word_mean(word="women"))
# print(Ai().chat("hi how are you?"))
