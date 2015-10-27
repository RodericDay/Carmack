function submitForm() {
    $.post('/autos', $("#mainForm").serialize());
    updateCollection();
    this.reset();
    return false
}

function updateCollection() {
    $.getJSON('/autos', null, function(response) {
        collectionView.innerHTML = '';
        response.data.forEach(function(entry){
            collectionView.innerHTML += JSON.stringify(entry) + "<br>";
        });
    });
}

window.onload = function initialize() {
    mainForm.onsubmit = submitForm;
    updateCollection();
}
