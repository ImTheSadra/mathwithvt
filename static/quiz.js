let url = window.location.href;
let splited = url.split("/");
let level = splited[splited.length-1]
// console.log(level);

let answered = 0;
const maxAnswer = 3;
let score = 0;

let time = 0;
const maxTime = 60;

function timer(){
    time += 1;
    document.getElementById("timer").innerText = (maxTime-time).toString()
}

function getQuiz(){
    let req = new XMLHttpRequest;
    req.open("GET", "/quiz/"+level.toString());
    req.onload = (ev)=>{
        result = JSON.parse(faNum(req.responseText));
        document.getElementById("quiz-text").innerText = result["text"];

        let options = document.getElementById("answers");
        for (let i = 0; result["options"].length; i++){
            console.log(result["options"][i]);

            let click = (ev=null)=>{answered+=1;score-=1;update()}
            let id = i; //result["options"][i]["id"]
            if (result["answer"] == id){
                click = (ev=null)=>{answered+=1;score+=1;update();}
            }
            let btn = document.createElement("button");
            btn.id = id;
            btn.innerText = result["options"][i]["txt"];
            btn.className = "btn btn-primary";

            let br2 = document.createElement("br");
            options.appendChild(br2);
            options.appendChild(btn);
            let br = document.createElement("br");
            options.appendChild(br);
        }

        let place = document.getElementById("place");
        
        place.innerText = result["place"];
        place.style.display = "block";
        place.style = "block";
    }
    req.send();
}

function faNum(text){
    let ennums = "123456789";
    let fanums = "۱۲۳۴۵۶۷۸۹۰";

    for(let i = 0; i < text.length; i++){
        if (ennums.indexOf(text.charAt(i)) != -1){
            text[i] = fanums.charAt(ennums.indexOf(text[i]));
        }
    }
    return text;
}

function update(){
    getQuiz();
    document.getElementById("vtDisplay").src = "/vt/"+level.toString()+"/"+(answered+1).toString();
}

setTimeout(update, 100);