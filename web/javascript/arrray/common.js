function method() {
    let colors = ["Red","Green","Blue"]

    colors.push("Pink");         //add last
    colors.unshift("Purple");    //add first
    
    colors.pop();               //remove last
    colors.shift();            //remove first

    document.write("Colors Name: "+colors.join(", ")+"<br>")
}
method()