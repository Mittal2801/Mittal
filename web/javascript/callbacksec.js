function showMessage(callback) {
    console.log("This message appers after 2seconds.please wait for data");
    setTimeout(() => {
        callback();
    },2000);
}
function done() {
    console.log("Operation completed!");
}
showMessage(done)