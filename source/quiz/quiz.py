from .exams import exams
import json, random

levels = ["نقش جهان - اصفهان", "تخت جمشید - استان فارس", "حرم حضرت شاهچراغ - شیراز"]

def makeQuiz(level:int):
    exam = random.choice(exams)(level)
    data = exam.toJson()
    data["place"] = levels[level-1]
    return json.dumps(data)