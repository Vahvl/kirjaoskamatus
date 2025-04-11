console.log("Tes!!")
koik= ""
document.addEventListener('keydown', (event) => {
    const keyPressed = event.key;
    console.log(keyPressed)
    if (keyPressed == "Backspace") {
        koik = koik.slice(0, -1)
        document.getElementById("koikTahed").innerHTML=koik
        document.getElementById("bigAssTaht").innerHTML=koik.slice(-9,-1)
    }
    else if (keyPressed.length==1) {
        koik+=keyPressed
        document.getElementById("koikTahed").innerHTML=koik
        document.getElementById("bigAssTaht").innerHTML=koik.slice(-9,-1)
    }
});