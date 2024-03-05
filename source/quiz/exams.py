import math
from random import randint, choice
# from PIL import Image, ImageDraw
# from base64 import b64encode

# area

class Area:
    text = "مساحت مربعی {area} متر مربع است. یک ضلع ان چقدر است؟"
    def __init__(self, level:int) -> None:
        num = randint(1, 50+(level*20))
        while math.sqrt(num) != round(math.sqrt(num)):
            num = randint(1, 50+(level*20))
        self.num = num
        self.answer = math.sqrt(self.num)

    def toJson(self):
        result = {"text": "", "options": [], "answer": "0", "place": "", "image": None}
        result["text"] = self.text.format(area=str(self.num))

        options = [
            str(int(self.num**2)),
            str(int(self.num/2)),
            str(int(self.num*2)),
            str(int(self.num))
        ]

        for i, option in enumerate(options):
            t = options.copy()
            t[i] = None
            while option in t or option == str(int(self.answer)):
                option = str(int(randint(1,50)))
            result["options"].append([option, str(i)])

        index = choice(range(len(result["options"])))
        result["options"][index][0] = str(int(self.answer))
        result["answer"] = result["options"][index][1]
        return result

# abs

class Abs:
    def __init__(self, level:int) -> None:
        options = [
            ["x×√y", lambda x,y,z:abs(x*math.sqrt(y))],
            ["x×y+z", lambda x,y,z:abs(x*y+z)]
        ]
        result = choice(options)
        x = randint(-10,1+(level*20))
        y = randint(  1,1+(level*20))
        while math.sqrt(y) != round(math.sqrt(y)):
            y = randint(0, 100+(level*20))
        z = randint(-10,1+(level*20))
        text:str = result[0]
        text = text.replace("x", str(int(x)))
        text = text.replace("y", str(int(y)))
        text = text.replace("z", str(int(z)))
        self.x, self.y, self.z = x, y, z
        self.text = text
        self.answer = result[1](x,y,z)
    
    def toJson(self):
        result = {"text": "", "options": [], "answer": "0", "place": "", "image": None}
        result["text"] = "|"+self.text+"|"
        options = [
            str(int(-self.answer)),
            str(int(self.answer-self.x)),
            str(int(self.answer*self.y-randint(2,5))),
            str(int(self.x+self.y))
        ]

        for i, option in enumerate(options):
            t = options.copy()
            t[i] = None    
            while option in t or option == str(int(self.answer)):
                option = str(int(randint(1,50)))
            result["options"].append([option, str(i)])

        index = choice(range(len(result["options"])))
        result["options"][index][0] = str(int(self.answer))
        result["answer"] = result["options"][index][1]
        return result

# sub array

class SubArray:
    def __init__(self, level:int) -> None:
        self.text = "یک مجموعه {length} عضوی، چند زیر مجموعه دارد؟"
        self.length = randint(2, (level*5))
        self.answer = 2**self.length
    
    def toJson(self):
        result = {"text": "", "options": [], "answer": "0", "place": "", "image": None}
        result["text"] = self.text.format(length=str(self.length))
        options = [
            str(int(randint(0, self.length))),
            str(int(self.length**2)),
            str(int(randint(self.length, self.length*2))),
            str(int(randint(self.length, 2**self.length)))
        ]
        for i, option in enumerate(options):
            t = options.copy()
            t[i] = None
            while option in t or option == str(int(self.answer)):
                option = str(int(randint(1,50)))
            result["options"].append({"txt": option, "id": str(i)})

        index = choice(range(len(result["options"])))
        result["options"][index][0] = str(int(self.answer))
        result["answer"] = result["options"][index][1]
        return result

exams = [Area, Abs, SubArray]