function starup(){
    let href = window.location.href;
    let splited = href.split("/");

    let name = splited[splited.length-1];
    
    // console.log(name);
    
    if (name == ""){
        document.getElementById("homeBtn").classList.add("active");
    } else if (name == "about") {
        document.getElementById("aboutBtn").classList.add("active");
    }

    let buttons = document.getElementsByClassName("lock-btn");
    for(let i = 0; i < buttons.length; i++){
        let button = buttons.item(i);
        button.addEventListener("click", (ev=null)=>{alert("این مرحله قفله برای باز شدنش باید مراحل قبلی رو انجام بدی")})
    }
}

function fuNum(){
    let ennums = "123456789";
    let fanums = "۱۲۳۴۵۶۷۸۹۰";
    let elements = document.getElementsByClassName("fa-num");
    for(let i = 0; i < elements.length; i++){
        let element = elements.item(i);
        for(let i = 0; i < element.innerHTML.length; i++){
            if (element.innerHTML[i] in ennums){
                element.innerHTML[i] = fanums.charAt(ennums.indexOf(element.innerHTML[i]));
            }
        }
        console.log(element.innerHTML)
    }
}

setTimeout(() => {
    fuNum
}, 200);

setTimeout(starup, 100);

let clearConsole = () => {
    console.clear();
    setTimeout(clearConsole, 10000)     
}

// setTimeout(clearConsole, 10000);