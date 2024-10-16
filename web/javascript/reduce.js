const p1 = [5,4,1,5,12,16,6]

console.log(p1);

let x1 = p1.reduce((res,rep) => {
    return res + rep;
})
console.log(x1);

let x2 = p1.reduce((res,rep) =>{
    return res * rep;
})
console.log(x2);

let x3 = p1.reduce((res,rep) =>{
    return res > rep ? res : rep;
})
console.log(x3);

let x4 = p1.reduce((res,rep) =>{
    return res < rep ? res : rep; 
})
console.log(x4);

let x5 = p1.reduce((res,rep) =>{
    return res * rep ? res : rep;
})
console.log(x5);