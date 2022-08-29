console.log('hello')

// function add_comment(event) {
//     event.preventDefault()
//     console.log('form submitted')
//     let comment_form = document.querySelector("#add_form")
//     let comment_list = document.querySelector("#comment_list")
//     console.log(comment_form)
//     let formData = new FormData(comment_form)
//     fetch('/api/coffeegonewild/add_comment', {
//         method: 'post',
//         body: formData
//     })
//     .then(res => {
//         if (res.status==200){
//             res.json()
//         }
//         })
//     .then(data => {
//         console.log(data)
//         comment_list.innerHTML += `
//         <li>${data.user_name} said: ${data.form.content}</li>
//         `    
//         comment_form.reset()
//     })
//     .catch(err => console.log(err))
// }




function add_comment(event) {
    event.preventDefault()
    console.log('form submitted')
    let comment_form = document.querySelector("#add_form")
    let comment_list = document.querySelector("#comment_list")
    console.log(comment_form)
    let formData = new FormData(comment_form)
    fetch('/api/coffeegonewild/add_comment', {
        method: 'post',
        body: formData
    })
    .then(res => {
        if (res.status==200){
            let data = res.json()
            console.log(data)
            comment_list.innerHTML += `
            <li>${data.user_name} said: ${data.form.content}</li>
            `    
            comment_form.reset()
            
        }
        else {
            // comment_list.innerHTML += `
            // <li>Please register! </li>
            // `    
            comment_form.reset()
            redirect('/coffeegonewild')
        }
        })
    .catch(err => console.log(err))
}
