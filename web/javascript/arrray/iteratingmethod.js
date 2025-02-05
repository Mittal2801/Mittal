function iterating(){
    numbers = [1,2,3,4,5];

    //iterating method:
    //forEach,map,filter,reduce

    //foreach method
    document.write("ForEach method results: <br>");
    numbers.forEach(num => document.write(num + "<br>"));

    //map method
    let doubled = numbers.map(num => num * 2);
    document.write("Map method results: "+doubled.join(", ")+"<br>");

    //filter method
    let evens = numbers.filter(num => num % 2 == 0);
    document.write("Filter method results: "+evens.join(", ")+"<br>")

    //reduce method
    let sum = numbers.reduce((acc,num) => acc + num,0);
    document.write("Reduce method results: "+sum+"<br>")

}
iterating()