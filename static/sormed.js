const read = {
    t1: ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'ü', 'õ'],
    t2: ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ö', 'ä'],
    t3: ['z', 'x', 'c', 'v', 'b', 'n', 'm']
  };

const sormed =  {
    v1: ["a", "z", "<", "q"], //vasak väike (roosake)
    v2: ["w", "s", "x"],
    v3: ["e", "d", "c"],
    v4: ["r", "t", "f", "g", "v", "b"],

    p1: ["p", "ü", "õ", "ö", "ä", "'", "-"],
    p2: ["o", "l", "."],
    p3: [",", "k", "i"],
    p4: ["m", "n", "j", "h", "u", "y"],
}



//ma vihkan htmli südamest
v = document.getElementById("v")
m = document.getElementById("m")
p = document.getElementById("p")
valik = document.getElementById("valitud") //see tekst seal ülal 
rida = document.getElementById("rida").innerHTML //loll viis leida prg rida
console.log(v, m, p, rida)

function vahetus (x){
  valik.innerHTML = x.innerHTML
  
}
// miks see syntax nii väärakas olema peab 😭😭
v.addEventListener("click", function (){vahetus(p)})
m.addEventListener("click", function (){vahetus(m)})
p.addEventListener("click", function (){vahetus(p)})
//ts pmo 💔🥀

console.log(read[rida])
//reavalik tehtud, tuleb välja mõelda mida nendega teha, ma ei jaksa hetkel tegeleda sellega