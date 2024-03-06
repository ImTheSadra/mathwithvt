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
    document.getElementById("timer").innerText = faNum((maxTime-time).toString())+" ثانیه وقت داری";
    if (time >= maxTime){
        alert("ببخشید باید بگم که وقتت تموم شده");
        window.location = "/";
    }
    setTimeout(timer, 1000);
}

function getQuiz(){
    let req = new XMLHttpRequest;
    req.open("GET", "/quiz/"+level.toString());
    req.onload = (ev)=>{
        let result = JSON.parse(req.responseText);
        document.getElementById("quiz-text").innerText = faNum(result["text"]);

        document.getElementById("place").innerText = result["place"];

        let options = document.getElementById("answers");
        options.innerHTML = "";
        for (let i = 0; result["options"].length; i++){
            // console.log(result["options"][i]);

            let click = (ev=null)=>{
                answered+=1;score-=1;
                update();
                // time = 0;
            }
            let id = result["options"][i][1];

            if (result["answer"] == id){
                click = (ev=null)=>{
                    answered+=1;score+=1;
                    update();
                    // time = 0;
                }
            }
            let row = document.createElement("div");
            row.className = "row";

            let btn = document.createElement("button");
            btn.onclick = click;
            btn.id = id;
            btn.innerText = faNum(result["options"][i][0]);
            btn.className = "btn btn-primary optionBtn";

            row.appendChild(document.createElement("br"));
            row.appendChild(btn);

            options.appendChild(row);
        }
    }
    req.send();
}

function faNum(text){
    let ennums = "1234567890";
    let fanums = "۱۲۳۴۵۶۷۸۹۰";

    for(let i = 0; i < text.length; i++){
        if (ennums.includes(text[i])) {
            text = text.replace(text[i], fanums[ennums.indexOf(text[i])])
        }
    }
    
    return text;
}

let codeInput = document.getElementById("code");
let code = codeInput.value;
codeInput.value = "";

function update(){
    time = 0;
    getQuiz();
    if (answered >= maxAnswer){
        if (score <= 1){
            alert("ببخشید باید بگم که این مرحله رو باختی. ولی مشکلی نیست دوباره تلاش کن");
            window.location = "/";
        } else {
            alert("هورااا. تو برنده شدی!!");
            window.location = "/win/"+level.toString()+"/"+code;
        }
    }
    document.getElementById("vtDisplay").src = "/vt/"+level.toString()+"/"+(answered+1).toString();
    document.getElementById("answerd"  ).innerText = faNum(answered.toString()+"/"+maxAnswer.toString());
    document.getElementById("score"    ).innerText = faNum("امتیاز : "+score.toString());
}

setTimeout(update, 100);
timer();