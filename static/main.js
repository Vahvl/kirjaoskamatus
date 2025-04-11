console.log("Tes!!")
koik= ""
document.addEventListener('keydown', (event) => {
    const keyPressed = event.key;
    console.log(keyPressed)
    if (keyPressed == "Backspace") {
        koik = koik.slice(0, -1)
        document.getElementById("koikTahed").innerHTML=koik
    }
    else if (keyPressed != "Shift" || keyPressed != "Control"){
        koik+=keyPressed
        document.getElementById("koikTahed").innerHTML=koik
    }
});