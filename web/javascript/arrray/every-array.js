function every() {
    let numbers = [12,2,32,44,58];

    let everyEven = numbers.every(num => num % 2 === 0);
    document.write("Every Even Numbers: "+everyEven+"<br>");
}
every()