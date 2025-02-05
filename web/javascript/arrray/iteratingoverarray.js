function iteratingMethodsExample() {
    let numbers = [1,2,3,4,5];

    //foreach method
    document.write("foreach method results: <br>");
    numbers.forEach(num => document.write(num + "<br>"));

    //map method
    let doubled = numbers.map(num => num * 2);
    document.write("map results: "+doubled.join(", ")+"<br>");

    //filter method
    let evens = numbers.filter(num => num % 2 == 0);
    document.write("Filter results: "+evens.join(", ")+"<br>")

    //reduce method
    let sum = numbers.reduce((acc,num) => acc + num, 0);
    document.write("Reduce results: "+sum+"<br>");
}
iteratingMethodsExample()