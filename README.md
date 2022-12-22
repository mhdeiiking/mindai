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

# Thats all thank you.
