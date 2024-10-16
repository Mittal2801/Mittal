const numEvery = [8,34,5,11];
let allOver18 = numEvery.some(myfunction);

console.log("All above 18 is ",allOver18)

function myfunction(value,index,array){
    console.log(index);
    return value > 18;
}

const no = [75,83,56,42,55];
let over50 = no.some(newData);

console.log("All above 90 is ",over50);

function newData(value,index,array){
    console.log(index);
    return value > 90;
}