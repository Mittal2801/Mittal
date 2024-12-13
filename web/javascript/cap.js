function cap(){
    let name = (document.getElementById('myTextBox1').value);
    // alert(name);
    // alert(name.toUpperCase());
    document.getElementById('capital').innerHTML = name.toUpperCase()
}