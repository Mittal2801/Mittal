function funchange(){
    const elements = document.getElementsByClassName('modifyclass');
    for(let i=0;i<elements.length;i++)
    {
        elements[i].style.backgroundColor = '#ccc';
        elements[i].style.fontWeight = 'bold';
        elements[i].textContent = 'This element was modified using getElementsByClassName!';
    }
}