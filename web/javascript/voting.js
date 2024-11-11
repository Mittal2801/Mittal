function vote()
{
var setdata = document.getElementById("ageSelect").value;
// alert(setdata);

if (document.getElementById('ageSelect').value == '0-10'){
    message = ('Not eligible for voting')
}

else if(document.getElementById('ageSelect').value == '11-18'){
    message = ('Not eligible for voting')
}

else if(document.getElementById('ageSelect').value == '19-30'){
    message = ('eligible for voting')
}

else if(document.getElementById('ageSelect').value == '31-40'){
    message = ('eligible for voting')

}

else if(document.getElementById('ageSelect').value == '41-50'){
    message = ('eligible for voting')
}
document.getElementById('msg').innerHTML = message;

let name = parseInt(document.getElementById('myTextBox1').value);
let password = parseFloat(document.getElementById('myTextBox2').value);
let age = parseInt(document.getElementById('myTextBox3').value);
alert(name)
alert(password)
alert(age)
if (document.getElementById('myTextBox1').value == ''){
    print2=("Please enter name")
}
else if (document.getElementById('myTextBox2').value == 'password < 6'){
    print2 = ("Please enter 6 digit password")
}
else if ( document.getElementById('myTextBox3').value == 'age<18'){
    print2 = ("Please enter above 18")
}
document.getElementById('err').innerHTML = print2;
}
