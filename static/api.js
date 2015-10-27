function submitForm() {
    var form = this;
    $.ajax({
        url: '/autos',
        type: 'POST',
        data: $("#mainForm").serialize(),
        success: function(response) {
            if (response.success) {
                form.reset();
                updateCollection();
            } else {
                alert(response.error);
            }
        }
    });
    return false
}

function promptDelete(entryId) {
    if (confirm("Are you sure you want to delete this entry?")) {
        $.ajax({
            url: '/autos/'+entryId,
            type: 'DELETE',
            success: updateCollection
        });
    }
}

function updateCollection() {
    collectionView.innerHTML = '';
    $.getJSON('/autos', null, function(response) {
        var i = 0; // add internal keys to avoid this mess
        response.data.forEach(function(entry){
            var copy = document.querySelector("#entryTemplate").cloneNode(true);
            copy.id = i++;
            for (key in entry) {
                copy.querySelector('.'+key).innerHTML = entry[key];
            }
            copy.querySelector(".buttonEdit").onclick = function() {
                console.log(copy);
            }
            copy.querySelector(".buttonDelete").onclick = function() {
                promptDelete(copy.id);
            };
            collectionView.appendChild(copy);
        });
    });
}

window.onload = function initialize() {
    mainForm.onsubmit = submitForm;
    updateCollection();
}
