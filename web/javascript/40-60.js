const num = [30,23,90,80,70]
let between = num.some(myfunction);

console.log("Between 40 to 60=",between)


function myfunction(value,index,array){
    return value > 40 && value < 60;
}