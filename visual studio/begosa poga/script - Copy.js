const poga = document.querySelector("button");

const buttonWidth = 250;
const buttonHeight = 100;

const maxWidth = window.innerWidth - buttonWidth;
const maxHeight = window.innerHeight - buttonHeight;

const buttonTexts = [
    "Ha Ha Ha, mīkstais",
    "Atkal netrāpīji",
    "LLLOOOOOLLLL",
    "Zābaks",
    "Bots"
]
let textIndex = 0

poga.addEventListener("mouseover", () => {
    poga.style.top = Math.floor(Math.random() * maxHeight) + "px"
    poga.style.left = Math.floor(Math.random() * maxWidth) + "px"

    poga.innerText = buttonTexts[textIndex]

    if(textIndex === buttonTexts.length - 1){
        textIndex = 0 
    } else {
        textIndex = textIndex + 1
    }
})