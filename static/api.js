function submitForm() {
    $.ajax({
        url: '/autos',
        type: 'POST',
        data: $(mainForm).serialize(),
        success: function(response) {
            if (response.success) {
                mainForm.reset();
                updateCollection();
            } else {
                alert(response.error);
            }
        }
    });
    return false
}

function populateForm(entryId) {
    $.getJSON('/autos/'+entryId, null, function(response) {
        if (response.success) {
            for (key in response.data) {
                if (key!=='photo') {
                    mainForm[key].value = response.data[key];
                }
            }
        }
    });
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
        response.data.forEach(function(entry){
            var copy = document.querySelector("#entryTemplate").cloneNode(true);
            copy.id = entry.id;
            for (key in entry) {
                if (key=='photo') {
                    copy.querySelector('.'+key).setAttribute("src", entry[key]);
                } else {
                    copy.querySelector('.'+key).innerHTML = entry[key];
                }
            }
            copy.querySelector(".buttonInfo").onclick = function() {
                populateForm(copy.id);
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
