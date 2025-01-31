function modifyAllElements(){
    const allContentElements = document.querySelectorAll('.content');
    allContentElements.forEach((element,index) =>{
        element.style.backgroundColor = '#ffcl07';
        element.textContent = 'This is element ${index + 1},modified using querySelectorAll!';
    });
}