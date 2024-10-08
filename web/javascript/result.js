function hello()
{
    let a=parseInt(document.getElementById('txt1').value);
    let b=parseInt(document.getElementById('txt2').value);
    let c=parseInt(document.getElementById('txt3').value);
    let d=parseInt(document.getElementById('txt4').value);
    let e=parseInt(document.getElementById('txt5').value);
    total=a+b+c+d+e
    //document.getElementById('txt6').value = total;
    document.getElementById('total').innerHTML = total;

    avg = total / 5
    if(avg > 60)
    {
        grade=("A Grade")
    }

    else if(avg > 50)
    {
        grade=("B Grade")
    }

    else if(avg > 40)
    {
        grade=("C Grade")
    }
    
    else if(avg > 35)
    {
        grade=("D Grade")
    }

    else
    {
        grade=("Fail")
    }
    //document.getElementById('txt7').value = grade;
    document.getElementById('result').innerHTML = grade;


        



}