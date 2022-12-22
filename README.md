# mindai
mindai is a package has alot of ai tools like chat with ai or code generate and more.


**Examples**
<b>Chat with ai:</b>
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
#print(means['example'])
```

<b>Audio  to Text (STT) :</b>
```
import mindai
from mindai import Ai

ai = Ai()

tt = ai.audio_to_text(url="https://ttsmp3.com/created_mp3/2e14d53d4285fe4b0d43245902171fcf.mp3")

print(tt)
#print(means['text'])
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
""",lang=ar)
## lang None or english or arabic.
print(ex)
#print(ex['explain'])
```

<b>Image Search Engine (Ai Make, Images.) :</b>
```
import mindai
from mindai import Ai

ai = Ai()

eng = ai.image_search(query="Duck")

print(eng) # return list of images.
#print(eng['imgs']) 
```

# Thats all thank you.
