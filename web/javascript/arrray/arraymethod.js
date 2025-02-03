function arrayMethodExample() {
    let numbers = [1,2,3,4,5];

    let squaredNumbers = numbers.map(num => num * num);     //Map modified
    let EvenNumbers = numbers.filter(num => num%2 === 0);   //Filter modified
    let sum = numbers.reduce((acc,num) => acc+num,0);       //Reduce modified

    document.write("Squared numbers: "+squaredNumbers.join(", ")+"<br>");
    document.write("Even numbers: "+EvenNumbers.join(", ")+"<br>");
    document.write("Sum of numbers: "+sum+"<br>");
}
arrayMethodExample()