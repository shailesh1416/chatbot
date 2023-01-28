submit_btn = document.getElementById('submit-btn')
// submit_btn = document.getElementById('submit-btn')
const input_box = document.getElementById('input_box')
const response_box = document.getElementById('response_box')
const page_title = document.getElementById('page-title')
const chat_title = document.getElementById('chat-title')
const chat_form = document.getElementById('chat-form')





var input_box_error = document.getElementById('input_box_error')
var counter = 1
getChatHistory()

function createName() {
            chatlist = document.getElementById('chat-list')
            firstChild = chatlist.firstElementChild
            chatItem = document.createElement('li')
            chatItem.setAttribute("id",localStorage.getItem('chat_id'))
            chatItem.classList.add('chat-item','current-chat')
            chatItem.innerHTML = 'New Chat'
            console.log(chatItem)
            console.log(chatlist)
            chatlist.insertBefore(chatItem,firstChild)
}

function getReply() {
    fetch(`http://127.0.0.1:5000/getAnswer?question=${text}&chat_id=${localStorage.getItem('chat_id')}`)
    // fetch(`http://127.0.0.1:5000/getAnswer?question=${text}`)
    .then((response) => response.json())
    .then((data) => {
        answer = document.createElement("div")
        answer.innerHTML = `<div id='answer${counter}' class='answer-list'><div class='answer-list-item message'>${data.answer}</div></div>`
        info_box.appendChild(answer)
        var chatHistory = document.getElementById(`answer${counter}`);
        console.log(chatHistory)
        chatHistory.scrollIntoView({block: "end"});
        }
    );
    // input_box.value = ""
    counter=counter+1
}



function createId(callback,callback2){
    fetch(`http://127.0.0.1:5000/getNewChatId?userId=${1}`)
    .then((response) => response.json())
    .then((data) => {
        id2 =data.id
        console.log(id2)
        // document.cookie =JSON.stringify({chat_id:id2})
        localStorage.setItem('chat_id', id2)
        callback(id2)
        createName()
    }).catch(err=>{return `ERR: ${err}`})
}

function getChatHistory(){
    fetch(`http://127.0.0.1:5000/getChatHistory?userId=${1}`)
    .then((response) => response.json())
    .then((data) => {
        h = data.history
        chatlist = document.getElementById('chat-list')
        h.forEach((item)=>{
            chatItem = document.createElement('li')
            chatItem.setAttribute("id",item.id)
            chatItem.classList.add('chat-item')
            if(item.title!==null){
                chatItem.innerHTML = item.title
            }else{
                // console.log(item.timestamp)
                chatItem.innerHTML = "No name"
            }
            // console.log(chatItem)
            chatlist.appendChild(chatItem)
            })
        
    }).catch(err=>{return `ERR: ${err}`})
}

// save title of chat
function saveChatTitle(title,chatId){
    fetch(`http://127.0.0.1:5000/saveChatTitle?title=${title}&chat_id=${chatId}`)
    .then((response) => response.json())
    .then((data) => {
       if(data.status){
          console.log("renamed")
       }else{
            console.log("Title not saved")
       }
    }).catch(err=>{return `ERR: ${err}`})
}

// action when submit button is clicked
submit_btn.addEventListener('click',(e)=>{
    e.preventDefault()
    text = input_box.value.trim()
    if(text.length <1){
        input_box_error.innerHTML = " <b>⚠️Please type something and then click submit<b>"
            setTimeout(() => {
                input_box_error.innerHTML = ""
            }, 2000);
            return
        }
        var info_box = document.getElementById('info_box')
        question = document.createElement("div")
        question.innerHTML = `<div id='question${counter}' class='question-list'><div class='question-list-item message'>${text}</div></div>`
        info_box.appendChild(question)
        if (counter==1){
            createId(getReply,createName)
        }else{
            getReply()
        }
})


// page_title.addEventListener('click',(e)=>{
//     if (counter>1){
//         chat_form.style.display = 'block'
//     }else{
//         alert("First ask some questions")
//     }
// })

// chat_title.addEventListener('focusout',(e)=>{
//     if (counter>1){
//         title = chat_title.value
//         chatdId = localStorage.getItem('chat_id')
//         chat_form.style.display = 'none'
//         newTitle = saveChatTitle(title,chatdId)
//     }
// })


// remane code

document.addEventListener('dblclick',(e)=>{
    if(e.target.classList.contains('chat-item')){
        t = e.target.innerText
        e.target.innerHTML = `<input type="text" class="rename" value="${t}">`
    }
})


document.addEventListener('focusout',(e)=>{
    if(e.target.classList.contains('rename')){
        t = e.target.value
        chatId = e.target.parentNode.getAttribute('id')
        console.log(chatId)
        saveChatTitle(t,chatId)
        e.target.parentNode.innerText = t
    }
})

