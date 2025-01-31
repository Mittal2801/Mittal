function modify() {
    let animals = ["Dog","Cat","Cow"]
    animals.push("Lion");
    animals[1] = "Tiger";
    animals.pop();

    document.write("Modified Array:" +animals.join(", ") + "<br>");
}
modify()