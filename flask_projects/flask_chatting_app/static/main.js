document.addEventListener('DOMContentLoaded', () => {
    const socket = io();

    const sendBtn = document.getElementById('sendBtn');
    const messageInput = document.getElementById('message');
    const messagesDiv = document.getElementById('messages');

    sendBtn.addEventListener('click', () => {
        const message = messageInput.value;
        socket.send(message);
        messageInput.value = '';
    });

    socket.on('message', (msg) => {
        const p = document.createElement('p');
        p.textContent = msg;
        messagesDiv.appendChild(p);
    });
});
