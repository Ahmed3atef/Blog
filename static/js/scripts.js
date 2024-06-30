
document.addEventListener('DOMContentLoaded', function() {
    const commentSubmit = document.getElementById('comment-submit');
    const commentDelete = document.getElementById('comment-delete');
    const id = getIdFromUrl();


    const currentUserId = window.currentUser.user_id;
    
    commentSubmit.addEventListener('click', ()=>{
        sendComment(id,currentUserId)
    });
    commentDelete.addEventListener('click', ()=>{
        deleteComment()
    })
});

function getIdFromUrl() {
    const url = window.location.href;
    const urlParts = url.split('/');
    const id = urlParts[urlParts.length - 2];
    return id;
}

function sendComment(id, user_id) {
    const content = document.getElementById('inputContent').value;

    fetch(`/api/send-comment/${id}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            author: user_id, 
            post: id,
            comment: content,
        })
    })
    .then(response => response.json())
    .then(data => console.log('Success:', data))
    .then(
        () => location.reload()
    )
    .catch((error) => console.error('Error:', error));
}

function deleteComment(){
    const comment_id = document.getElementById('comment-delete').value;
    fetch(`/api/delete-comment/${comment_id}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
    })
    .then(data => console.log('Success:', data))
    .then(
        () => location.reload()
    )
    .catch((error) => console.error('Error:', error));
}



// Function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}