const form = document.getElementById("chat-form");
const input = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const message = input.value;
  appendMessage("You", message, "user");
  input.value = "";

  try {
    const res = await fetch("http://127.0.0.1:5000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message }),
    });

    const data = await res.json();
    appendMessage("CryptoBuddy", data.response, "bot");
  } catch (error) {
    appendMessage("CryptoBuddy", "Sorry, there was an error connecting to the server.", "bot");
  }
});

function appendMessage(sender, text, type) {
  const div = document.createElement("div");
  div.classList.add("message", type);
  div.innerHTML = `<strong>${sender}:</strong> ${text}`;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
}