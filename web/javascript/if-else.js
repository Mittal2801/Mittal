a=30
b=40

function hello(){
    //alert("mittal gandi");
    let a = parseInt(document.getElementById('txt1').value);
    let b = parseInt(document.getElementById("txt2").value);
    let c = a+b;
    alert("Addition of a & b="+ c)
}


if(a>b)
{
    console.log("a is greater than b")
}
else
{
    console.log("b is greater than a")
}