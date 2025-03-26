class Circle {
    constructor(radius) {
        this._radius = radius;
    }
    get radius() {
        return this._radius;
    }
    set radius(value) {
        if (value > 0) {
            this._radius = value;
        }
        else {
            throw new Error("Radius must be possitive. ");
        }
    }
    area() {
        return Math.PI * this._radius ** 2;
    }
}
const circle = new Circle(5);
document.addEventListener("DOMContentLoaded",function() {
    document.getElementById("classGettersSettersOutput").innerHTML = `Radius: ${circle.radius} Area: ${circle.area()}`;
});