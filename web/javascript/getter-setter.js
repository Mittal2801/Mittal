const student = {
    firstName : "Prajapati",
    lastName : "Mittal",


    // Getter method for fullName
    get fullName() {
        return `${this.firstName} ${this.lastName}`;
    },


    // Setter method for fullName
    set fullName(name) {
        let parts = name.split(" ");
        if(parts.length === 2) {
            this.firstName = parts[0];
            this.lastName = parts[1];
        }
        else {
            console.log("Invalid full name format");
        }
    }
};

// Using getter
console.log(student.fullName);

// Using setter
student.fullName = "Nagar Vidhi";
console.log(student.fullName);