function greet() {
    console.log("Hello, apa kabar?");
}

greet() // memanggil function
greet()
greet()
greet()
greet()

// function dengan parameter atau argumen
function Hello(name,age,address) {
    console.log(`Hello, ${name}! ${age} years old, live in ${address}`);
}

Hello('Zahra','17','Bogor')
Hello('Aufa','16','Bekasi')

function add(number1, number2) {
    let result = number1 + number2
    return result
}

let add1 = add(13,30)
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

let kali1 = kali(15,2)
console.log(kali1)

function pengurangan(number1, number2) {
    let result = number1 - number2
    return result
}
    
    let pengurangan1 = pengurangan(50,10)
    console.log(pengurangan1)

    function luassegitiga(alas, tinggi) {
        let result = alas * tinggi * 1/2
        return result
    }
    
    let luassegitiga1 = luassegitiga (12, 5)
    console.log(luassegitiga1)