function findindex() {
    let numbers = [1,2,3,4,5];

    let findindex = numbers.findIndex(num => num > 3);
    document.write("Find Index: "+findindex+"<br>");
}
