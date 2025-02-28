class Vehicle {
    constructor (type) {
        this.type = type;
    }
    move() {
        return `${this.type} is moving.` ;
    }
}
class Car extends Vehicle {
    move() {
        return `${this.type} is faster.` ;
    }
}

const sportsCar = new Car("Sports Car");
document.addEventListener("DOMContentLoaded",function() {
    document.getElementById("inheritance").innerHTML = sportsCar.move();
});