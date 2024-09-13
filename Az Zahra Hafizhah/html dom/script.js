function validateForm() {
    let name = document.forms["myForm"]
    ['name'].value;
    if (name == "" || name == "-") {
        alert("Name must be filled out")
        return false
    }
    
    let age = document.forms["myForm"]
    ['age'].value;
    if (age == "" || age == "0") {
        alert("Age must be filled out")
        return false
    }
}
