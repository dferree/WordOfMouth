// delete function button
function deleteActivity(activityId) {
    fetch('/delete-activity', {
        method: 'POST',
        body: JSON.stringify({activityId: activityId}),
    }).then((_res) => {
        window.location.href = "/activities";
    });
}

function confirmDelete(activityId) {
    if (confirm("Are you sure you want to delete this activity?")) {
        deleteActivity(activityId);
    }
}

// navbar dropdown
function toggleDropdown(category) {
    var dropdown = document.getElementById(category + "-dropdown");
    dropdown.classList.toggle("show");
}

function menuChange(x) {
    x.classList.toggle("change");
}

// expand category arrow.
// document.querySelectorAll('.display-acts').forEach(button => {
//     button.addEventListener('click', function() {
//         const category = this.getAttribute('data-category');
//         const dropdown = document.getElementById(`${category}-dropdown`);
//         if (dropdown) {
//             dropdown.classList.toggle('expanded');
//         }
//     });
// });

// $('.display-acts').click(function() {
//     const category = $(this).data('category');
//     const dropdown = $(`#${category}-dropdown`);
    
//     if (dropdown.length) {
//         dropdown.toggleClass('expanded');
//     }

//     const $icon = $(this).find('i');
//     if (dropdown.length && dropdown.hasClass('expanded')) {
//         $icon.removeClass('fa-solid fa-chevron-down').addClass('fa-solid fa-chevron-up');
//     } else {
//         $icon.removeClass('fa-solid fa-chevron-up').addClass('fa-solid fa-chevron-down');
//     }
// });

$('.display-acts').click(function() {
    const category = $(this).data('category');
    const dropdown = $(`#${category}-dropdown`);
    
    if (dropdown.length) {
        dropdown.toggleClass('expanded');
    }
    
    const $icon = $(this).find('i');
    if (dropdown.length && dropdown.hasClass('expanded')) {
        $icon.removeClass('fa-chevron-down fa-3x').addClass('fa-chevron-up fa-3x');
    } else {
        $icon.removeClass('fa-chevron-up fa-3x').addClass('fa-chevron-down fa-3x');
    }
});

// activity show more 
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


// scrolling functions
var lastScrollTop = 0;
var navbar = document.querySelector('.nav-wom');
var navbar_bottom = document.querySelector('.nav-wom-bottom');

window.addEventListener('scroll', function() {
    var currentScroll = window.pageYOffset || document.documentElement.scrollTop;
    
    if (currentScroll > lastScrollTop) {
        // Scrolling down
        navbar.style.transform = 'translateY(-100%)';
        navbar_bottom.style.transform = 'translateY(0)';
    } else {
        // Scrolling up
        navbar.style.transform = 'translateY(0)';
        navbar_bottom.style.transform = 'translateY(100%)';
    }

    lastScrollTop = currentScroll;
});


// hover tooltip functions
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