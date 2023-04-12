const chatForm = document.getElementById('chat-form');
const chatContainer = document.getElementById('chat-container');

chatForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const messageInput = document.getElementById('message');
    const messageText = messageInput.value.trim();
    if (!messageText) return;
    const message = document.createElement('div');
    message.classList.add('chat-message', 'sent');
    message.innerHTML = messageText;
    chatContainer.appendChild(message);
    messageInput.value = '';
    fetch('/api/message/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: messageText }),
    })
        .then((response) => response.json())
        .then((data) => {
            const reply = document.createElement('div');
            reply.classList.add('chat-message', 'received');
            reply.innerHTML = data.message;
            chatContainer.appendChild(reply);
        })
        .catch((error) => console.error(error));
});
