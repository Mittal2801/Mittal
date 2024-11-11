function cal()
{
let amt = parseInt(document.getElementById('myTextBox1').value);
let rate = parseFloat(document.getElementById('myTextBox2').value);
let time = parseInt(document.getElementById('myTextBox3').value);

if (document.getElementById('myTextBox1').value == ''){
    print=("Please enter amount")
}
else if (document.getElementById('myTextBox2').value == ''){
    print = ("Please enter rate")
}
else if ( document.getElementById('myTextBox3').value == ''){
    print = ("Please enter time")
}
document.getElementById('message').innerHTML = print;


for(let i=0; i<time; i++){
    si = amt * rate * time/100
    cal = amt * rate/100
    add = amt +cal
    amt += cal
}
document.getElementById('amount').innerHTML = amt;
document.getElementById('total').innerHTML = si;
document.getElementById('interest').innerHTML = add;
}



