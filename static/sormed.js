const read = {
  r1: ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "ü", "õ"],
  r2: ["a", "s", "d", "f", "g", "h", "j", "k", "l", "ö", "ä"],
  r3: ["z", "x", "c", "v", "b", "n", "m"],
  koikread: ["a", "z", "q", "w", "s", "x", "e", "d", "c", "r", "t", "f", "g", "v", "b", "p", "ü", "õ", "ö", "ä", "o", "l", "k", "i", "m", "n", "j", "h", "u", "y"]
};
  
const kaed =  {
  v: ["a", "z", "q", "w", "s", "x", "e", "d", "c", "r", "t", "f", "g", "v", "b"],
  p: ["p", "ü", "õ", "ö", "ä", "o", "l", "k", "i", "m", "n", "j", "h", "u", "y"],
  m : ["a", "z", "q", "w", "s", "x", "e", "d", "c", "r", "t", "f", "g", "v", "b", "p", "ü", "õ", "ö", "ä", "o", "l", "k", "i", "m", "n", "j", "h", "u", "y"]
}

viimane = ""
reake = ""
tase = document.getElementById("tase").innerHTML

//mashallah võtab sõnad failist
async function loadWords() {
  const response = await fetch("/static/sonad.txt");
  const text = await response.text();
  return text.split(/\r?\n/).filter(Boolean);
}

//main generatsioon yap, lege vaata seda kuidas ta töötab, et aru saada
function generatsioon () {
  tekst = ""
  if (tase == "t1" || tase == "t2") {
    kasi = viimane
    console.log(reake)
    valmista = read[reake].filter(item => kaed[kasi]?.includes(item));
    console.log(valmista)
    
    if (tase == "t1") {
      for (i = 0; i < 4; i++) {
        const randomIndex = Math.floor(Math.random() * valmista.length);
        tekst += (valmista[randomIndex]).toString().repeat(2) + " ";
      }
      tekst = tekst.slice(0, -1)
      console.log(tekst)
      startTypingAnimation(tekst)
    }
    if (tase == "t2") {
      for (i = 0; i < 9; i++) {
        if (i !== 4) {
          randomIndex = Math.floor(Math.random() * valmista.length);
          tekst += valmista[randomIndex];
        } else {
          tekst += " ";
        }
      }
      console.log(tekst)
      startTypingAnimation(tekst)
    }
  } else if (tase == "t3") {
    console.log("t3")
    async function tase3() {
      const words = await loadWords();
      const selected = [];
      while (selected.length < 2 && selected.length < words.length) {
        const word = words[Math.floor(Math.random() * words.length)];
        if (!selected.includes(word)) selected.push(word);
      }
    
    startTypingAnimation(selected.join(" "))
    console.log(selected.join(" "))
    }
    tase3()
  }
 }


//ma vihkan htmli südamest
v = document.getElementById("v")
m = document.getElementById("m")
p = document.getElementById("p")
r1 = document.getElementById("r1")
r2 = document.getElementById("r2")
r3 = document.getElementById("r3")
koikread = document.getElementById("koikread")
valik = document.getElementById("valitud")
rida = document.getElementById("rida")
console.log(v, m, p, rida)

function vahetus (x){
  valik.innerHTML = x.innerHTML
  viimane = x.id; console.log(viimane)
  generatsioon()
  this.blur();
}

function tumeJaKeerutatudVahetus (x){
  rida.innerHTML = x.innerHTML
  reake = x.id; console.log(reake)
  generatsioon()
  this.blur();
}

if (tase != "t3")
  {
  // miks see syntax nii väärakas olema peab 😭😭
  v.addEventListener("click", function (){this.blur(); vahetus(v)})
  m.addEventListener("click", function (){this.blur(); vahetus(m)})
  p.addEventListener("click", function (){this.blur(); vahetus(p)})

  r1.addEventListener("click", function (){this.blur(); tumeJaKeerutatudVahetus(r1)})
  r2.addEventListener("click", function (){this.blur(); tumeJaKeerutatudVahetus(r2)})
  r3.addEventListener("click", function (){this.blur(); tumeJaKeerutatudVahetus(r3)})
  koikread.addEventListener("click", function (){this.blur(); tumeJaKeerutatudVahetus(koikread)})
}

koik= ""
document.addEventListener('keydown', (event) => {
    const keyPressed = event.key;
    if (keyPressed == "Backspace") {
      koik = koik.slice(0, -1)
      document.getElementById("bigAssTaht").innerHTML=koik.slice(-17)
    }
    else if (keyPressed.length==1) {
      koik+=keyPressed
      document.getElementById("bigAssTaht").innerHTML=koik.slice(-17,-1)+keyPressed
    }
    if (keyPressed == "Enter") {
      if (koik == document.getElementById("output").innerText) {
        alert("TUBLI")
        generatsioon()
        koik = ""
        document.getElementById("bigAssTaht").innerHTML=""
      }
      koik = ""
    }
});

