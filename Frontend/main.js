const body = document.body
const button = body.querySelector('#pop')
const postList = body.querySelector('#posts')
const form = body.querySelector('form')
async function poster(){
    let res = await fetch("http://localhost:5000/api/v1/users")
    let data = await res.json()
    postList.innerHTML = ''
    data.users.forEach(user => {
        let el = document.createElement('li')
        el.textContent = user.username
        postList.appendChild(el)
    });
}
button.addEventListener('click', e=>{
    poster()
})
// form.addEventListener('submit', e =>{
//     e.preventDefault()
//     let formdata = new FormData(form)
//     let data = Object.fromEntries(formdata)
//     let jsondata = JSON.stringify(data)
//     fetch('http://localhost:5000/api/v1/users', {
//         method: 'POST',
//         headers : {
//             'Content-Type': 'application/json'
//         },
//         body: jsondata
//     }).then(res => res.json()).then(console.log).catch(console.error)
// })
