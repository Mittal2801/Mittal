function transaction(){
    let balance = parseInt(document.getElementById('currentBalance').value);
    let amt = parseInt(document.getElementById('amount').value);

    let selectedoperation = document.querySelector('input[name="transaction"]:checked').value;
    d=0;
    if (selectedoperation === 'withdraw')
    {
        d = balance - amt;
        document.getElementById('result').value = d;
    }
    else if (selectedoperation === 'deposit')
    {
        d = balance + amt;
        document.getElementById('result').value = d;
    }

    document.getElementById('result').innerHTML = d;

}


function  showhide(grbHide){
    /*
    if (grbHide === 'withdraw')
        {
            withdraw.style.display = 'block';
            deposite.style.display = 'none';
            inquiry.style.display = 'none';
        }
        else if (grbHide === 'deposite')
        {        
            withdraw.style.display = 'none';
            deposite.style.display = 'block';
            inquiry.style.display = 'none';
        }
        else if (grbHide === 'inquiry')
        {
            withdraw.style.display = 'none';
            deposite.style.display = 'none';
            inquiry.style.display = 'block';
        }
            */
    
}