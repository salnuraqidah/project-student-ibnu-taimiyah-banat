function greet() {
    console.log("Hello, Apa Kabar?");
}

greet() // memanggil function
greet()
greet()
greet()
greet()

// function dengan parameter atau argument
function hello(name,age,addres) {
    console.log(`Hello, ${name}! ${age} years old, live in ${addres}`);
}

hello('Aufa','16','Bekasi')
hello('Naila','16','Makassar')

function add(number1, number2) {
    let result = number1 + number2
    return result
} 

let add1 = add(10,21) // bukan bentuk cetakan
console.log(add1 + 50);

function bagi(number1, number2) {
    if (number2 == 0) {
    alert("pembagi tidak boleh nol")
    return false
}
let result = number1 / number2
return result
}


let bagi1 = bagi(100,4)
console.log(bagi1);

let bagi2 = bagi(20,0)
console.log(bagi2);

function kali(number1, number2) {
    
let result = number1 * number2
return result
}

let kali1 = kali(100,4)
console.log(kali1);

let kali2 =kali(10,2)
console.log(kali2);

function kurang(number1, number2) {
    
let result = number1 - number2
return result
}

let kurang1 = kurang(100,4)
console.log(kurang1);

let kurang2 =kurang(10,2)
console.log(kurang2);


function luassegitiga(alas1, tinggi2) {
    
    let result = 1 / 2 * alas1 * tinggi2
    return result
    }


let segitiga1 = luassegitiga(4,10)
console.log(segitiga1);

let segitiga2 = luassegitiga(12,4)
console.log(segitiga2);


