const p =[5,4,1,5,12,16,6]

console.log(p)

let newArr = p.map((val) => {
    return val * val;
})
console.log(newArr);

let x1 = p.map((c) => {
    return c * 2;
})
console.log(x1);

let no = p.map((m) => {
    return m +5;
})
console.log(no);
