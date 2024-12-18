const poga = document.querySelector('button')

const buttonHeight = 150;
const buttonWidth = 150;

const buttonTexts = [
    "No",
    "Nu uh",
    "Nope",
    "Wont happen",
    "Faliure"
]
let textIndex = 0

const maxWidth = window.innerWidth - buttonWidth;
const maxHeight = window.innerHeight - buttonHeight;

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