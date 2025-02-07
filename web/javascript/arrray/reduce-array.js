function reduce() {
    let numbers = [1,2,3,4,5,6,7,8,9,10];

    let sum = numbers.reduce((acc,num) => acc + num ,0);
    document.write("Sum of numbers Array: "+sum)
}
reduce()