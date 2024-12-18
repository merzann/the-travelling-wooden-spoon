// Ajax for thumbs-up and thumbs-down
document.getElementById('thumbs-up-btn').addEventListener('click', () => {
    updateThumbs('thumbs_up');
});

document.getElementById('thumbs-down-btn').addEventListener('click', () => {
    updateThumbs('thumbs_down');
});

function updateThumbs(action) {
    fetch(`/recipe/${recipeId}/thumbs/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken, // Django CSRF token
        },
        body: JSON.stringify({ action }),
    })
        .then(response => response.json())
        .then(data => {
            document.querySelector('#thumbs-up-btn + span').textContent = `${data.thumbs_up} Likes`;
            document.querySelector('#thumbs-down-btn + span').textContent = `${data.thumbs_down} Dislikes`;
        });
}
