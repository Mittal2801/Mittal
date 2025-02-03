function method() {
    let numbers = [1,2,3,4,5];

    let square = numbers.map(num => num * num);
    let even = numbers.filter(num => num % 2 == 0);
    let sum = numbers.reduce((acc,num) => acc + num,0)

    document.write("Square="+square.join(", ")+"<br>")
    document.write("Even="+even.join(", ")+"<br>")
    document.write("Sum="+sum+"<br>")
}
method()