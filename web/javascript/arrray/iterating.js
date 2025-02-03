function iterating() {
    let fruits = ["Apple","Banana","Cherry"]

    fruits.forEach(fruit => {
        document.write(fruit + "<br>");
    });
    for(let fruit of fruits){
        document.write(fruit + "<br>");
    }
}
iterating();