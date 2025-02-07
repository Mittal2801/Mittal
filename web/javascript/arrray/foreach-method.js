function foreach() {
    let numbers = [1,2,3,4,5,6,7];

    numbers.forEach((num, index) => document.write(`Index ${index}:${num}<br>`))
}
foreach()