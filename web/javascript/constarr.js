const arr = [1,2,3,4,5,6,7,8,9]

for(let i =0;i<arr.length;i++)
{
    console.log("index " + i + "  = "+ arr[i])
}

const courses = ["CCC","PYTHON","WEB DEVELOPMENT","WEB DESIGN","C/C++"]

console.log("***** for in loop *****")
for(i in courses){
    console.log(i);
    console.log(courses[i]);
}

console.log("***** for of loop *****")
for(i of courses){
    console.log(i);
}

let total=0
let add=0
let count=0

const marks = [75,59,66,53,60,55]

for(i of marks){
    total+=(i);
    if(i>50 && i<60){
        add+=(i);
        count+=1;
    }
}
console.log("total=",total)
console.log("marks between 50 to 60=",add)
console.log("count=",count)
