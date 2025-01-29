function modifyParagraph() {
    const paragraph = document.getElementById('uniqueParagraph');
    paragraph.textContent = 'This content was changed using getElementById()!';
    paragraph.style.backgroundColor = '#f8d7da';
    paragraph.style.fontWeight = 'bold';
}