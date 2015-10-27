function submitForm() {
    $.post('/autos', $("#mainForm").serialize());
    updateCollection();
    this.reset();
    return false
}

function updateCollection() {
    $.getJSON('/autos', null, function(response) {
        response.data.forEach(function(entry){
            var copy = document.querySelector("#entryTemplate").cloneNode(true);
            for (key in entry) {
                document.querySelector('.'+key).innerHTML = entry[key];
            }
            collectionView.appendChild(copy);
        });
    });
}

window.onload = function initialize() {
    mainForm.onsubmit = submitForm;
    updateCollection();
}
