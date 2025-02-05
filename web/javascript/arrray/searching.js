function searching() {
    let fruits = ["Apple","Banana","Cherry"];
    
    let indexOf = fruits.indexOf("Apple");
    let findfruit = fruits.includes("Mango");
    let startlatter = fruits.find(fruit => fruit.startsWith("B"));
    let findindexwithstartlatter = fruits.findIndex(fruit => fruit.startsWith('C'));


    document.write("Fruits Array: "+fruits.join(", ")+"<br>")
    document.write("Index of Apple: "+indexOf+"<br>")
    document.write("Mango in array?true or false: "+findfruit+"<br>")
    document.write("In Array which fruit name start with 'B': "+startlatter+"<br>")
    document.write("In Array which index of fruit name start with 'C': "+findindexwithstartlatter+"<br>")
}
searching()