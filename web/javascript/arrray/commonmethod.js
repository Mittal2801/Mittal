function addRemoveElementsExample() {
    let colors = ["Red","Green","Blue"];

    // Add elements
    colors.push("Yellow");      //add last-yellow(red,green,blue,yellow)
    colors.unshift("Purple")    //add first-purple(purple,red,green,blue,yellow)
    
    // Remove elements
    colors.pop();               //remove last-yellow(purple,red,green,blue)
    colors.shift();             //remove first-purple(red,green,yellow)

    document.write("Updated colors array: "+colors.join(", ")+"<br>");
}
addRemoveElementsExample();