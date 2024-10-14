num = [1,2,3,4,5,6,7,8,9]

num.forEach((v)=> {
    console.log("addition:",v+5)
});

num.forEach((val) => {
    console.log("multiplication:",val*val)
})

for(let p of num){
    console.log(p)
}

num.forEach((val)=>{
    console.log("division:",val/val)
})

num.forEach((no) => {
    console.log("subtraction:",no-no)
})

console.log(num.sort())
console.log(num.reverse())
console.log(num.toString())