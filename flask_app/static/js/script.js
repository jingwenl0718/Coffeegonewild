function add_comment(event) {
    event.preventDefault()
    let comment_form = document.querySelector("#add_form")
    let comment_list = document.querySelector("#comment_list")
    let formData = new FormData(comment_form)
    fetch('/api/coffeegonewild/add_comment', {
        method: 'post',
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        if (data.msg == "NoUserError") {
            alert("Please log in or register. Thank you!")
            window.location = "/coffeegonewild/login_form";
        }
        else {
            let today = new Date()
            let dd = String(today.getDate()).padStart(2, '0')
            let mm = String(today.getMonth() + 1).padStart(2, '0')
            let yyyy = today.getFullYear();
            today =  mm + '/' + dd + '/' + yyyy;
            comment_list.innerHTML += `
            <li>
                <div style="display: flex">
                    <div class="mr-3" id="starbackground">
                        <div style="width: calc(20px * ${data.form.rating}); background-color: gold">
                            <img id="star-rating" src="/static/img/stars.png" alt="${data.form.rating}" title="${data.form.rating}"/>
                        </div>
                    </div>                        
                    <span id="comment_date">${today}</span>
                </div>  
                <span id="comment_name">${data.form.name}</span><br/>
                <span id="comment_content">${data.form.content}</span><br/>
                <span id="posted_by">Posted by </span><span id="commenter_name">${data.user_name}</span>
                <hr>
            </li>
            `    
            comment_form.reset()
        }
    })
    .catch(err => {
        alert("All fields are required. Thank you!")
    })
}