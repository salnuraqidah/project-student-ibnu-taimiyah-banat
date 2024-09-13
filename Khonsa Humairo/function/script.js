function greet() {
    console.log("hello...")
}

greet()

function greet(name) {
    alert("Hai, apa kabar " + name + "?")
}

let yourName = prompt("siapa nama anda?")

greet(yourName)

function add(a, b){
    result = a + b;
    result_text = a + "+" + b + "=" + result;
    return result_text;
}

console.log(add(10,11))

function add(a, b){
    result = a + b;
    result_text = a + "+" + b + "=" + result;
    return result_text;
}

addition = add(10,11);
console.log("hasilnya adalah " + addition);

