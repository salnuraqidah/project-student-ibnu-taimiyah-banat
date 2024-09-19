function validateform() {
    let name = document.forms["myform"]
    ['name'].value;
    if (name ==""|| name =="-") {
        alert("name must be filled out")
        return false
    }
    let age = document.forms["myform"]
    ['age'].value;
    if (age ==""|| age =="0") {
        alert("age must be filled out without 0")
        return false
    }
    }
