function searchElementsExample() {
    let animals = ["Cat","Dog","Fish"]

    let indexOfDog = animals.indexOf("Dog");        //array element index found
    let includesFish = animals.includes("Fish");    //array element have or not(ans:true or false)
    let foundAnimal = animals.find(animal => animal.startsWith("C"));       //array element found by first latter like C for 'Cat'
    let indexOfFoundAnimal = animals.findIndex(animal => animal.startsWith("D"));   //array element index found by first latter like D for 'Dog'

    document.write("Index of 'Dog': "+indexOfDog+"<br>")
    document.write("Includes 'Fish': "+includesFish+"<br>")
    document.write("Found animal starting with 'C': "+foundAnimal+"<br>")
    document.write("Index of animal starting with 'D: "+indexOfFoundAnimal+"<br>")
    
}
searchElementsExample()