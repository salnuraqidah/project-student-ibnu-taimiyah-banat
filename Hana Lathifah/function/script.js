function greet() {
    console.log("hello, apa kabar?")
}

greet() //memanggil function

//function dengan parameter
function hello(name,age,address){
    console.log(`Hello,${name}! ${age} years old, live in ${address}`);
}
hello(`aufa`,`12`,`norway`)
hello(`hana`,`18`,`123.43.123`)

function add(number1,number2){
    let result = number1 + number2
    return result
}

let add1 = add(18,21)
console.log(add1);



function bagi(number1,number2){
    if (number2 == 0){
        alert("pembagi tidak boleh nol")
        return false
    }
    let result= number1/number2
    return result
}

let bagi1 = bagi(100,4)
console.log(bagi1);

function kurang(number1,number2){
    let result= number1-number2
    return result
}
let kurang1 = kurang(100,80)
console.log(kurang1);

function kali(number1,number2){
    let result= number1*number2
    return result
}
let kali1 = kali(100,80)
console.log(kali1);

function segitiga(number1,number2){
    let result= number1*number2*0.5
    return result
}
let segitiga1 = segitiga(20,5)
console.log(segitiga1);


