function find() {
    let numbers = [1,2,3,4,5];

    let findnum = numbers.find(num => num > 3);
    document.write("Find Example: "+findnum+"<br>");
}
find()