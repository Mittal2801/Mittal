class Animal {
    constructor(name) {
        this.name = name;
    }
    speak() {
        return `${this.name} makes a noise.`;
    }
}

class Dog extends Animal {
    speak() {
        return `${this.name} barks.`;
    }
}
const dog = new Dog("Buddy");
document.addEventListener("DOMContentLoaded",function() {
    document.getElementById("classInheritanceOutput").innerHTML = dog.speak();
});