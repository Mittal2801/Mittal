function hello()
{
    console.log("hello")
}
hello()

function printMittal(y){
    for(let i=0;i<y;i++)
    {
        console.log("Mittal");
        console.log("hello");
    }
}
printMittal(100);

function sum(a,b)
{
    sum1 = a+b;
    console.log("sum of two value is ",sum1);
}
sum(101,112);
sum(101,12);

let mul=(a,b)=>{
    return a*b;
}

console.log(mul(2,3));

let multi = (a,bb) =>{
    return a *bb;
}

console.log(multi(2,55));