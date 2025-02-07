function some() {
    let numbers = [1,3,5];     // in array if one even number it return output true otherwise false.

    let hasEven = numbers.some(num => num % 2 === 0);
    document.write("Has Even Numbers: "+hasEven+"<br>");
}
some()