from .exams import exams
import json, random

levels = ["نقش جهان - اصفهان", "تخت جمشید - استان فارس", "حرم حضرت شاهچراغ - شیراز"]

def makeQuiz(level:int):
    exam = random.choice(exams)(level)
    data = exam.toJson()
    data["place"] = levels[level-1]

    fanums = "۱۲۳۴۵۶۷۸۹۰"
    nums = {
        "1": fanums[0],
        "2": fanums[1],
        "3": fanums[2],
        "4": fanums[3],
        "5": fanums[4],
        "6": fanums[5],
        "7": fanums[6],
        "8": fanums[7],
        "9": fanums[8],
        "0": fanums[0],
    }

    text = json.dumps(data)

    return text