document.getElementById('send-button').addEventListener('click', function () {
    var query = document.getElementById('user-query').value;
    fetch('/chat/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ 'query': query })
    })
        .then(response => response.json())
        .then(data => {
            // Update chat history with the new data
            var chatHistoryDiv = document.getElementById('chat-history');
            chatHistoryDiv.innerHTML = '';
            data.chat_history.forEach(message => {
                chatHistoryDiv.innerHTML += `<div>${message.query}: ${message.response}</div>`;
            });
        });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
