

const userInput = document.getElementById('user-input')
userInput.addEventListener('change', detect)

async function detect(e) {
    flipLoading()
    displayImage(e)
    getResult()
    flipLoading()
}

const updateUI = async (data) => {
    document.querySelector('.result').classList.add('display')
    document.querySelector('.result-class').innerHTML = data.class
    document.querySelector('.result-score').innerHTML = data.score + "%"
    document.querySelector('.user-input-label').innerHTML = "Go Again <i class='fa-solid fa-upload'></i>"
}

const postDataFile = async (url='', data) => {

    const response = await fetch(url, {
        method: 'POST',
        body: data,
    })
    try {
        const newData = await response.json()
        return newData
    }
    catch (error) {
        console.log("error: " + error)
    }
}

function flipLoading() {
    document.getElementById('preload').classList.toggle('display')
}

function displayImage(e) {


    const url = URL.createObjectURL(e.target.files[0])
    const userImage = document.querySelector('.user-input-image')
    userImage.setAttribute('src', url)
    userImage.classList.add('display')



}
async function getResult() {
    const file = userInput.files[0]
    const fd = new FormData()
    fd.append('omarImage', file)
    await postDataFile('/detect', fd)
    .then (data => {
        updateUI(data)
    })
}


// validation function return true only when jpg files are uploaded
//function isFileImage(file) {
//    const userInput = document.getElementById('user-input')
//    var isValid = /\.jpe?g$/i.test(userInput.value);
//
//    if (!isValid) {
//        displayPop('Only jpg files allowed!')
//        return false
//    } else {
//        removePop()
//        return true
//    }
//
//}

// popup functionality

const popup = document.getElementById('popup')
const textbox = document.querySelector('.popup-text')
const popupClose = document.querySelector('.popup-close')

popupClose.addEventListener('click', () => {
    removePop()
})


function displayPop(message) {
    textbox.childNodes[0].nodeValue = message;
    popup.classList.add('display')
}
function removePop() {
    textbox.childNodes[0].nodeValue = '';
    popup.classList.remove('display')
}

//Scroll up button functionality

const scrollUpButton = document.querySelector('.scroll-up')
scrollUpButton.addEventListener('click', ()=> {
    window.scrollTo(0, 0);
})



window.addEventListener('scroll', ()=> {
    if(window.scrollY > 850) {
        scrollUpButton.classList.add('display')
    } else {
        scrollUpButton.classList.remove('display')
    }
})

