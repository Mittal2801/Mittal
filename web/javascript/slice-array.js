function sliceExample() {
    let numbers = [1,2,3,4,5];
    let sliced = numbers.slice(1,4);

    document.write("Sliced array: "+sliced.join(", ")+"<br>");
}
sliceExample()