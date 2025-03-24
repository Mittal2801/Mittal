class Temp {
    constructor(celsius) {
        this._celsius = celsius;
    }
    get celsius() {
        return this._celsius;
    }
    set celsius(value) {
        this._celsius = value;
    }
   
    get fahrenheit() {
        return (this._celsius * 9/5) + 32;
    }
    set fahrenheit(value) {
        this._celsius = (value - 32) *5/9;
    }
}

const tempr = new Temp();

tempr.celsius = 25;
console.log(tempr._celsius)
console.log(tempr.fahrenheit)

tempr.fahrenheit = 100;
console.log("Celcius:",tempr.celsius)
console.log("Fahrenheit:",tempr.fahrenheit)