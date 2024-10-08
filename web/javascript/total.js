const data = {
    fname : 'mittal',
    lname : 'prajapati',
    email :'mituprajapati2801@gmail.com',
    phone : '9909608588',
    income : 50000,
    python : 66,
    php : 60,
    html : 65,
    dbms : 59,
    java : 62
}
total=0
for(const i in data)
{
    if(i=='python' || i=='php' || i=='html' || i=='dbms' || i=='java')
    {
        total+=data[i];
    }
}
console.log("all subject total:",total);