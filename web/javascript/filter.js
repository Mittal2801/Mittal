const numbers = [125,15,9,16,25]
const over18 = numbers.filter(checkData);

console.log(over18);

function checkData(value,index,array){
    return value > 18;
}

const num = [133,17,14,100,56]
const over19 = num.filter(check);

console.log(over19)


function check(value,index,array){
    return value > 19;
}