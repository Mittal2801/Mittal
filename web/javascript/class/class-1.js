class result{
    constructor (name){
        this.fname = name; 
    }
    hello(p)
    {
        let v = p * 5;
        console.log("hello how are you?" +v);
    }
    print()
    {
        window.print();
        //console.log('print ' + this.fname);
    }
}
function hello123()
{
    console.log("hello");
}

x = new result("mittal");
console.log(x.hello(5))
//x.print();

y = new result("xyz");
//console.log(y.print());