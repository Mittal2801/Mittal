const contact = {
    fname : 'mittal',
    lname : 'prajapati',
    email : 'mituprajapati2801@gmail.com',
    phone : '9909608588',
    income : 50000
}


for(const i in contact)
{
    console.log(i);
}

for(const i in contact)
{
    console.log("key is ",i,"Value is ",contact[i])
}

a = "mittal"

for(let i of a)
{
    console.log(i)
}