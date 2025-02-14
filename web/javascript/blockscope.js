function checkBlockScope() {
    if(true) {
        let blockVar = "I am a block-scoped variable";
        document.getElementById('blockOutput').innerHTML = blockVar;
        document.getElementById('outsideOutput').innerHTML = blockVar;
    }
    document.getElementById('outsideOutput').innerHTML = blockVar;
}