const list = [85,70,90,95,93]
const over90 = list.filter(checkMarks);

console.log("90 above marks:",over90);

function checkMarks(value,index,array){
    return value > 90;
}