
// delete function button
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


function menuChange(x) {
    x.classList.toggle("change");
  }

document.querySelectorAll('.expand-btn').forEach(button => {
    button.addEventListener('click', function() {
        const category = this.getAttribute('data-category');
        const dropdown = document.getElementById(`${category}-dropdown`);
        if (dropdown) {
            dropdown.classList.toggle('expanded');
        }
    });
});

function confirmDelete(activityId) {
    if (confirm("Are you sure you want to delete this activity?")) {
        deleteActivity(activityId);
    }
}

$(document).ready(function() {
    $('.show-more i').click(function() {
        var $description = $(this).closest('.activity-card').find('.activity-description');
        $description.toggleClass('expanded');
        if ($description.hasClass('expanded')) {
            $(this).removeClass('fa-circle-chevron-down fa-xl').addClass('fa-circle-chevron-up fa-xl'); // Change icon to "Show Less"
        } else {
            $(this).removeClass('fa-circle-chevron-up fa-xl').addClass('fa-circle-chevron-down fa-xl'); // Change icon to "Show More"
        }
    });
});

var lastScrollTop = 0;
window.addEventListener('scroll', function() {
    var currentScroll = window.pageYOffset || document.documentElement.scrollTop;
    var navbar = document.querySelector('.nav-wom');
    var navbar_bottom = document.querySelector('.nav-wom-bottom');
    if (currentScroll > lastScrollTop) {
        // Scrolling down
        navbar.style.transform = 'translateY(-100%)';
        navbar_bottom.style.transform = 'translateY(+100%)';
    } else {
        // Scrolling up
        navbar.style.transform = 'translateY(0)';
        navbar_bottom.style.transform = 'translateY(0)';
    }

    lastScrollTop = currentScroll;
});




$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip({ trigger: "hover" });
  });

  $(document).ready(function(){
    // Initialize Bootstrap tooltips
    $('[data-toggle="tooltip"]').tooltip();

    // Hide tooltip when dropdown is shown
    $('.cat-toggler').on('show.bs.dropdown', function () {
        $('[data-toggle="tooltip"]').tooltip('hide');
    });
});