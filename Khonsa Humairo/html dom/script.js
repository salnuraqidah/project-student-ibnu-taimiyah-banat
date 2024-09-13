function validateform() {
    let name = document.forms["myform"] ['name'] . value;
    if (name == "" || name == "-") {
        alert("Name must be filled out")
        return false
    }

    let age = document.forms["myform"] ['age'] . value;
    if (age == "" || age == "0") {
        alert("Age must be filled out")
        return false
    }
}