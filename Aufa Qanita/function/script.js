function greet() {
    console.log("hello, apa kabar?");
}
greet()
greet()
greet()
greet()
greet()

function hello(name, age, address) {
    console.log(`hello, ${name}! ${age} years old, live in ${address}`);
}

hello(`aufa`, `16`, `jakarta`)
hello(`nailah`, `16`, `makassar`)

function add(number1, number2) {
    let result = number1 + number2
    return result
    
}

let add1 = add(10,21)
console.log(add1 + 50);

function bagi(number1, number2) {
    if (number2 == 0){
        alert("pembagi tidak boleh 0")
        return false
    }
    let result = number1 / number2
    return result
}
let bagi1 = bagi(100, 4)
console.log(bagi1);

let bagi2 = bagi(20, 0)
console.log(bagi2);

function times(number1, number2) {
    let result = number1 * number2
    return result
    
}

let times1 = times(10,10)
console.log(times1);

function minus(number1, number2) {
    let result = number1 - number2
    return result
    
}

let minus1 = minus(10,10)
console.log(minus1);

function segitiga(number1, number2) {
    let result = number1 * number2 /2
    return result
    
}

let segitiga1 = segitiga(12,10)
console.log(segitiga1);

