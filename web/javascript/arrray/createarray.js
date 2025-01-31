function createArrayExample() {
    // Using array literal 
    let fruits = ["Apple","Banana","Cherry"];
    // USing Array constuctor
    let numbers = new Array(1,2,3,4,5);
    
    document.write("Fruits array: "+fruits.join(", ")+"<br>");
    document.write("Numbers array: "+numbers.join(", ")+"<br>");
}
createArrayExample();