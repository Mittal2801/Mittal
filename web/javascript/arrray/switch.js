function switchdefault() {
    let carname = "Dzire";
    let message;

    switch(carname) {
        case "Amaze" :
            message ="Not Amaze";
            break;
        case "Brezza":
            message ="Not Brezza";
            break;
        default:
            message = "Not"
    }
    document.write(message);
}
switchdefault();