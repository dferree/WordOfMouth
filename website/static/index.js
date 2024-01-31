function deleteActivity(activityId) {
    fetch('/delete-activity', {
        method: 'POST',
        body: JSON.stringify({activityId: activityId}),
    }).then((_res) => {
        window.location.href = "/";
    });
}

function toggleDropdown(category) {
    var dropdown = document.getElementById(category + "-dropdown");
    dropdown.classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.drop-arrow')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}