function all(){
    const allelement = document.querySelectorAll('.content');
    allelement.forEach((element,index) => {
        element.style.backgroundColor = '#ffc107';
        element.textContent = 'foreach!';
    });
}