# mindai
mindai is a package has alot of ai tools like chat with ai or code generate and more.


**Examples**
<b>Chat with ai (Offline)+:</b>
```
import mindai
from mindai import Ai

ai = Ai()

chat = ai.chat(message="Hello! How are you?")

print(chat)
#print(chat['reply'])
```

<b>Text from image (OCR) :</b>
```
import mindai
from mindai import Ai

ai = Ai()

ocr = ai.image_to_text(url="https://telegra.ph//file/3381da14831562cb2dd0e.png")

print(ocr)
#print(ocr['text'])
```

<b>Code Generatetor :</b>
```
import mindai
from mindai import Ai

ai = Ai()

code = a.code_gen(prompt="hello world",lang="python")

print(code)
#print(code['code'])
```


<b>Word mean :</b>
```
import mindai
from mindai import Ai

ai = Ai()

means = ai.word_mean(word="men")

print(means)
#print(means['mean'])
```

<b>Audio  to Text (STT) :</b>
```
import mindai
from mindai import Ai

ai = Ai()

tt = ai.audio_to_text(url="https://ttsmp3.com/created_mp3/2e14d53d4285fe4b0d43245902171fcf.mp3")

print(tt)
#print(tt['text'])
```
<b>Explain Code :</b>
```
import mindai
from mindai import Ai

ai = Ai()

ex = ai.explain_code("""
d = 0
print(d)
exit()
""",lang='ar')
## lang None or english or arabic.
print(ex)
#print(ex['explained'])
```

<b>Image Search Engine (Ai Make, Images.) :</b>
```
import mindai
from mindai import Ai

ai = Ai()

eng = ai.image_search(query="Duck")

print(eng) 
#print(eng['images']) 
```

<b> Dalle-2 Text-To-Image (New!) :</b>
```
import mindai
from mindai import Ai

ai = Ai()

eng = ai.dalle_2("Duck eat sandwich")

print(eng) 
#print(eng['url']) 
```
<b>Complete Setenece  :</b>
```
import mindai
from mindai import Ai

ai = Ai()

eng = ai.complete_setnece("The Goal of life is *") # Must add (*) To complete your setnece.

print(eng) 
#print(eng['setneces']) 
```
<b>Text-To-Anime Image!  :</b>
```
import mindai
from mindai import Ai

ai = Ai()

eng = ai.text_to_anime("A Iraqi Men")

print(eng) 
#print(eng['url']) 
```
<b>Prompt Extend :</b>
```
import mindai
from mindai import Ai

ai = Ai()

eng = ai.prompt_extend("Elon Musk")

print(eng)
#print(eng['text']) 
```
<b> Get Verbs and Names and Company Names :</b>
```
import mindai
from mindai import Ai

ai = Ai()

eng = ai.get_verbs("Hello, my name is Elon and i CEO of SpaceX and Tesla Motors")

print(eng) 
#print(eng['verbs']) 
```


# Thats all thank you.
