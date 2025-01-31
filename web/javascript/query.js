function firstchange(){
    const felement = document.querySelector('.content');
    if (felement) {
        felement.style.backgroundColor = '#dadcfc';
        felement.style.fontWidth = '10px';
        felement.textContent = 'This is changed content!'
    }
    else{
        console.log('No element found');
    }
    
}