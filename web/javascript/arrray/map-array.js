function map() {
    let numbers = [1,2,3,4,5];

    let squared = numbers.map(num => num * num);
    document.write("Squared numbers: "+squared.join(", ")+"<br>");
}
map()