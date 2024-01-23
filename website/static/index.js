function deleteActivity(activityId) {
    fetch('/delete-activity', {
        method: 'POST',
        body: JSON.stringify({activityId: activityId}),
    }).then((_res) => {
        window.location.href = "/";
    });
}

function menuChange(x) {
    x.classList.toggle("change");
  }