let num1 = parseFloat(prompt("birinchi son kiritin"))
let amal = prompt("+,-,*,/")
let num2 = parseFloat(prompt("ikkinchi son kiritin"))
let natija;
switch(amal){
    case "+":
    natija = num1+num2
    break;
    case "-":
    natija = num1-num2
    break;
    case "*":
    natija = num1*num2
    break;
    case "/":
        if (num2 === 0) {
            alert("hato")
        }
    natija = num1/num2
    break;
    default:
        alert("hato yoq")
    }
console.log(natija)
alert(`${num1}${amal}${num2} = ${natija}`);