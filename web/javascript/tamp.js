function tamp(selectedtamp) {
    let f = parseInt(document.getElementById('txt1').value);
    celsius = (f - 32) * 5 / 9;
    document.getElementById('txt2').value = celsius;
    
    let c = parseInt(document.getElementById('txt3').value);
    fahrenheit = (c * 9/5) + 32;
    document.getElementById('txt4').value = fahrenheit;
    
    if (selectedtamp === 'fc') {
        fc.style.display = 'block';
        cf.style.display = 'none';
    } else if (selectedtamp === 'cf') {
        fc.style.display = 'none';
        cf.style.display = 'block';
    }

tamp('fc');
tamp('cf');

}

