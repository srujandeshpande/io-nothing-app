console.log("whats up")

var productDiv = document.getElementById("products")
productDiv.innerHTML = "Handbag"

axios({
    method: 'get',
    url: 'http://localhost:8000/date',
}).then(response => {
    var res = response.data
    console.log(response.data)
    var firstDiv = document.getElementById("hello-world")
    firstDiv.innerHTML = res.date
})

console.log("End")





function createUser(){
    var name = document.getElementById("name-field").value
    var age = document.getElementById("age-field").value

    axios({
        method: 'post',
        url: 'http://localhost:8000/name',
        data: {
            person_name: name,
            age: age
        }
    }).then(response => {
        var res = response.data
        console.log(response.data)
        var firstDiv = document.getElementById("hello-world")
        firstDiv.innerHTML = res.status
    })

    console.log("user created!")
}
