// function hello(){
//      let a = parseInt(document.getElementById('txt1').value);
//      let b = parseInt(document.getElementById("txt2").value);
//      c = a+b
//      alert("Addition of a & b=",c)
//  }


function hello()
{
    let a = parseInt(document.getElementById('txt1').value);
    let b = parseInt(document.getElementById('txt2').value);
    c=a+b
    document.getElementById('txt3').value = c;
}