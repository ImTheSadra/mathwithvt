from flask import *
import json
from .level import level as Level
from .quiz import makeQuiz

app = Flask("app")

@app.route("/favicon.ico")
def favicon():
    return send_file("./assest/logo.ico")

def check(cookies, res:Response):
    if not cookies.get("levels") == None:
        levels = cookies.get("levels")
        levels = json.loads(levels)
        return res, levels
    levels = [
        {
            "lock": False,
            "index": 1,
            "name": "اول"
        },
        {
            "lock": True,
            "index": 2,
            "name": "دوم"
        },
        {
            "lock": True,
            "index": 2,
            "name": "سوم"
        }
    ]
    res.set_cookie("levels", json.dumps(levels))
    return res, levels

@app.route("/")
def index():
    res, _levels = check(request.cookies, make_response())
    # print(request.cookies.get("levels"))

    levels = []
    for i, level in enumerate(_levels):
        levels.append(Level(str(level["name"]), i+1, bool(level["lock"])))

    res.response = render_template("index.html", levels=levels)
    return res

@app.route("/assest/<path:path>")
def assest(path):
    return send_file("./assest/"+path)

@app.route("/play")
def playIndex():
    return render_template("index.html")

@app.route("/play/<int:level>")
def play(level:int):
    res = make_response()
    res, levels = check(request.cookies, res)
    _level = levels[level-1]
    level = Level(_level["name"], level, _level["lock"])
    res.response = render_template("game.html", level=level)
    return res

@app.route("/quiz/<int:level>")
def quiz(level:int):
    return makeQuiz(level)

@app.route("/reset")
def reset():
    res = make_response()
    levels = [
        {
            "lock": False,
            "index": 1,
            "name": "اول"
        },
        {
            "lock": True,
            "index": 2,
            "name": "دوم"
        },
        {
            "lock": True,
            "index": 2,
            "name": "سوم"
        }
    ]
    res.set_cookie("levels", json.dumps(levels))
    res.response = "<script>window.location = '/';</script>"
    return res

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/vt/<int:level>/<int:part>")
def vt(level:int, part:int):
    res = make_response()
    res.response = render_template("vt.html", level=level, part=part)
    return res

@app.route("/vt.xml/<int:level>/<int:part>")
def vtXml(level:int, part:int):
    res = make_response()
    result = ""
    with open("./assest/pano.xml", "r") as f:
        result = f.read()
    result = result.replace("[level]", str(level))
    result = result.replace("[part]",  str(part))
    res.response = result
    res.headers.add("Content-Type", "application/xml")
    return res

@app.route("/win/<int:level>")
def win(level:int):
    res = make_response()
    if request.headers.get("Content-Type") == "application/json":
        res.response = json.dumps({"status": res.status_code, "win": True})
    else:
        res.response = "<script>window.location = '/'</script>"
    levels = json.loads(request.cookies.get("levels"))
    if len(levels) <= level:return res
    levels[level]["lock"] = False
    print(levels)
    res.set_cookie("levels", json.dumps(levels))
    return res