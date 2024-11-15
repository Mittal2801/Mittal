function changeBackgroundColor() {
    const input = document.getElementById('no');
    const value = parseInt(input.value, 10);
    
    
        if (value >= 1 && value <= 10) {
            document.body.style.backgroundColor = 'pink';
        }
         else if (value >= 10 && value <= 20) {
            document.body.style.backgroundColor = 'yellow'; 
        } 
        else if(value >=21 && value <= 30){
            document.body.style.backgroundColor = 'blue'; 
        }
        else if(value >=31 && value <=40){
            document.body.style.backgroundColor = 'green';
        }

   
}

function onchangeColor()
{
var setdata = document.getElementById("drpcolor").value;
document.body.style.backgroundColor = setdata;

}