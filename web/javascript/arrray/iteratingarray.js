function iterateArrayExample() {
    let fruits = ["Apple","Banana","Cherry"];

    //Using foreach method
    fruits.forEach(fruit =>{
        document.write(fruit + "<br>");
    });

    //Using for...of loop
    for (let fruit of fruits) {
        document.write(fruit +"<br>");
    }
}
iterateArrayExample()