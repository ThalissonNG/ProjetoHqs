const searchInput = document.getElementById('search-here');

searchInput.addEventListener('input', (event) => {
    const value = formatString(event.target.value);
    
    const items = document.querySelectorAll('.list-hqs-completed .item')
    const noResults = document.getElementById('no-results');

    let hasResults = false;
    
    items.forEach(item =>{
        const itemTitle = item.querySelector('.tittle').textContent;
        if(formatString(itemTitle).indexOf(value) !== -1) {
            item.style.display = 'flex';
            hasResults = true;
        }
        else{
            item.style.display = 'none';
        }
    })
    if(hasResults){
        noResults.style.display = 'none';
    }
    else{
        noResults.style.display = 'block';
    }
});
function formatString(value){
    return value
        .toLowerCase()
        .trim();
}