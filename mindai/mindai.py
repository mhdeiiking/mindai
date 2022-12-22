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
                self.error = r.json()['message']
                return {"error":True,"message":self.error}
        except Exception as e:
            self.error = r.json()['message']
            return {"error":True,"message":self.error}
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
                self.error = r.json()['message']
                return {"error":True,"message":self.error}
        except Exception as e:
            self.error = r.json()['message']
            return {"error":True,"message":self.error}
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
                self.error = r.json()['message']
                return {"error":True,"message":self.error}
        except Exception as e:
            self.error = r.json()['message']
            return {"error":True,"message":self.error}
    def audio_to_text(self,url=None):
        """
        Search for image was maked by ai,
        :param query:
        """
        try:
            r = requests.get(self.main_api2+"stt",params={"url":url})
            if r.status_code ==200:
               
                self.textt = r.json()['text']

                self.confidence = (r.json()['confidence'])
                return {"error":None,"text":self.textt,"success_percentg":self.confidence}
            else:
                self.error = r.json()['message']
                return {"error":True,"message":error}
        except Exception as e:
            self.error = r.json()
            
            return {"error":True,"message":self.error['message']}
    def explain_code(self,code=None,lang=None):
        """
        This defition explain your code.
        :param code:
        :param lang:
        """
        try:
            r = requests.get(self.main_api2+"explain",params={"code":code})
            if r.status_code ==200:
                if lang == "english" or lang == "en" or lang == None:
                    self.textt = r.json()['explain']
                    return {"error":None,"explained":self.textt,}
                elif lang == "arabic" or lang == "ar":
                    self.textt = r.json()['explain']
                    c = requests.get(self.main_api2+"trans",params={"text":self.textt})
                    self.translated = c.json()['text']
                    return {"error":None,"explained":self.translated,}
                else:
                    return {"error":None,"explained":self.textt,}
            else:
                self.error = r.json()['message']
                return {"error":True,"message":error}
        except Exception as e:
            self.error = r.json()
            return {"error":True,"message":self.error['message']}
    def image_search(self,query=None):
        """
        Search for image was maked by ai,
        :param query:
        """
        try:
            r = requests.get(self.main_api2+"sai",params={"word":query})
            if r.status_code ==200:
                self.code = r.json()['imgs']
                self.count = len(r.json()['imgs'])
                return {"error":None,"images":self.code,"count":self.count}
            else:
                self.error = r.json()['message']
                return {"error":True,"message":self.error}
        except Exception as e:
            self.error = r.json()['message']
            return {"error":True,"message":self.error}
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
                self.error = r.json()['message']
                return {"error":True,"message":self.error}
        except Exception as e:
            self.error = r.json()['message']
            return {"error":True,"message":self.error}
# print(Ai().audio_to_text(url="https://ttsmp3.com/created_mp3/2e14d53d4285fe4b0d43245902171fcf.mp3"))
# print(Ai().image_search("cars"))
# print(Ai().chat("hi, bro"))
# print(Ai().code_gen(lang="python",prompt="hello"))
# print(Ai().word_mean("what"))
# print(Ai().explain_code("""
# d = 0
# print(d)
# d+=1
# print(d)
# """,lang="ar"))
