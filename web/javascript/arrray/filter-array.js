function filterexample() {
    let numbers = [1,2,3,4,5,6];

    let evens = numbers.filter(num => num % 2 === 0);
    document.write("Evens Numbers: "+evens.join(", ")+"<br>");
}
filterexample()