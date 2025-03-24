class Person {
    constructor(firstName,lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    // Getter for fullName
    get fullName() {
        return `${this.firstName} ${this.lastName}`
    }

    // Setter for fullName
    set fullName(name) {
        let parts = name.split(" ");
        if (parts.length === 2) {
            this.firstName = parts[0];
            this.lastName = parts[1];
        }
        else{
            console.log("Invalid name format")
        }
    }
}

Person.fullName = "NAGAR VIDHI";
console.log(Person.fullName);