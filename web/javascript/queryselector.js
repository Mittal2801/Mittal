function modifyFirstElement(){
    const firstContent = document.querySelector('.content');
    if(firstContent){
        firstContent.style.backgroundColor = '#b3e5fc';
        firstContent.style.fontWeight = 'bold';
        firstContent.textContent = 'This element was modified using querySelector()!';
    }
    else{
        console.log('No element found with the given selector. ');
    }
}