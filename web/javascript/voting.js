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

let name = (document.getElementById('myTextBox1').value);
let password = (document.getElementById('myTextBox2').value);
let age = parseInt(document.getElementById('myTextBox3').value);
// alert(name)
// alert(password)
// alert(age)
if (document.getElementById('myTextBox1').value == ''){
    print2=("Please enter name!")
}
// document.getElementById('err').innerHTML = print2;

if (document.getElementById('myTextBox2').value < '6'){
    print3 = ("Please enter 6 digit password!")
}
// document.getElementById('err').innerHTML = print3;

if (document.getElementById('myTextBox3').value < '18'){
    print4 = ("Please enter above 18!")
}
document.getElementById('err').innerHTML = print2,print3,print4;


}
