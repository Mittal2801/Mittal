function reduceright() {
    let numbers = [1,2,3,4,5];

    let reduceright = numbers.reduceRight((acc,num) => acc + num , '');
    document.write("Reduce Right Numbers: "+reduceright);
}
reduceright()