loginlink = document.getElementById('login-link')
registerlink = document.getElementById('register-link')
register = document.getElementById('register-form')
login = document.getElementById('login-form')

loginBtn = document.getElementById('login-btn')
registerBtn = document.getElementById('register-btn')




loginlink.addEventListener('click',()=>{
    register.style.display='none'
    login.style.display = 'block'
})

registerlink.addEventListener('click',()=>{
    login.style.display='none'
    register.style.display = 'block'
})


registerBtn.addEventListener("click",(e)=>{
    e.preventDefault()
    uname = document.querySelector('#name').value
    email = document.querySelector('#email').value
    password = document.querySelector('#password').value
    console.log(uname)

    fetch(`http://127.0.0.1:5000/register?email=${email}&password=${password}&name=${uname}`)
    .then((response) => response.json())
    .then((data) => {
        console.log(data)
    }).catch(err=>{return `ERR: ${err}`})
    })
