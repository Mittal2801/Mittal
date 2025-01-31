function modifyArrayExample() {
    let animals = ["Cat","Dog","Fish"];
    animals.push("Bird");       //Add element to the end
    animals[1] = "Lizard";      //Change an existing element
    animals.pop();              //Remove the last element

    document.write("Modified animals array: "+animals.join(", ")+"<br>");
}
modifyArrayExample()