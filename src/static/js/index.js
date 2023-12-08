
// TensorFlow API CALL HANDEL
const userInputTf = document.getElementById('user-input-tf')
userInputTf.addEventListener('change', (e) => {
    detectTf(e)
})

async function detectTf(e) {
    flipLoading()

    if (userInputTf.files.length === 0) {
        console.log("CANCEL")
        flipLoading()
        return
    }
    displayImage(e, "tf")
    await getResult("tf")
    flipLoading()
}

async function detectYolo(e) {
    flipLoading()

    if (userInputYolo.files.length === 0) {
        console.log("CANCEL")
        flipLoading()
        return
    }
    displayImage(e, "yolo")
    await getResult("yolo")
    flipLoading()
}

const updateUI = async (data, model) => {
    let userImage;
    if (model === "tf") {
        userImage = document.querySelector('.user-input-image-tf')
        console.log("TF: " + userImage)
    } else if (model === "yolo") {
        userImage = document.querySelector('.user-input-image-yolo')
        console.log("YOLO: " + userImage)
    }

    userImage.setAttribute('src', data.result_image)
    document.querySelector('.result').classList.add('display')
    if (model === "tf") {
        document.querySelectorAll('.result-class')[0].innerHTML = data.class
        document.querySelectorAll('.result-score')[0].innerHTML = data.score
    } else if (model === "yolo") {
        document.querySelectorAll('.result-class')[1].innerHTML = data.class
        document.querySelectorAll('.result-score')[1].innerHTML = data.score
    }

//    document.querySelector('.user-input-label').innerHTML = "Go Again <i class='fa-solid fa-upload'></i>"
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


function displayImage(e, model) {
    let userImage;
    const url = URL.createObjectURL(e.target.files[0])
    if (model === "tf") {
        userImage = document.querySelector('.user-input-image-tf')
        console.log(userImage)

    } else if (model === "yolo") {
        userImage = document.querySelector('.user-input-image-yolo')
        console.log(userImage)
    }

    userImage.setAttribute('src', url)
    userImage.classList.add('display')

}


async function getResult(model) {
    let inputUser;
    if (model === "tf") {
        inputUser = userInputTf
    } else if (model === "yolo") {
        inputUser = userInputYolo
    }
    const file = inputUser.files[0]
    const fd = new FormData()
    fd.append('omarImage', file)

    if (model === "tf") {
        await postDataFile('/detect-tf', fd)
        .then (data => {
            updateUI(data, model)
        })
    } else if (model === "yolo") {
        await postDataFile('/detect-yolo', fd)
        .then (data => {
            updateUI(data, model)
        })
    }


}


// YOLO API CALL
const userInputYolo = document.getElementById('user-input-yolo')
userInputYolo.addEventListener('change', (e) => {
    detectYolo(e, "yolo")
})


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

