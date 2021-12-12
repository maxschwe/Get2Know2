const form_settings = document.getElementById("form-settings")

const form_data = new FormData(form_settings); 

function join(){
    fetch("/join", {
        method: "POST",
        body = JSON.stringify(form_data.get())
    }).then(res => {
        console.log(res)
    })
}