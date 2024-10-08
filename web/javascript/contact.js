const contact = {
    fname : 'Mittal',
    lname : 'Prajapati',
    email : 'mituprajapati2801@gmail.com',
    mobile : '9909608588',
    income : 50000
}

console.log(contact);
 
console.log("----------Objecct detail is below----------")
console.log(contact.fname)
console.log('fname of contact is ',contact['fname']);

console.log(contact.lname)
console.log('lname of contact is ',contact['lname']);
console.log(contact['mobile']);
console.log(contact.income)

contact['fname']='Vidhi';
contact['lname']='Nagar';
console.log(contact)

const marks = {
    java : 70,
    python : 66,
    php : 80,
    dbms : 77,
    html :60
}

console.log(marks);

console.log("detail of marks")
console.log(marks.java)
console.log("Python marks:-",marks['python']);
console.log("Dbms marks:-",marks.dbms);