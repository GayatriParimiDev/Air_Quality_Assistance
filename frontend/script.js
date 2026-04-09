// frontend/script.js
const API_BASE = "http://127.0.0.1:5000";

const chatEl = document.getElementById("chat");
const inputEl = document.getElementById("msgInput");

function appendMessage(text, who="bot"){
  const div = document.createElement("div");
  div.className = "message " + (who === "user" ? "user" : "bot");
  // allow newlines
  div.innerHTML = text.replace(/\n/g, "<br/>");
  chatEl.appendChild(div);
  chatEl.scrollTop = chatEl.scrollHeight;
}

async function sendMessage(){
  const text = inputEl.value.trim();
  if(!text) return false;
  appendMessage(text, "user");
  inputEl.value = "";
  appendMessage("… thinking", "bot"); // temporary message
  // remove the placeholder after fetch
  try {
    const res = await fetch(API_BASE + "/api/chat", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({message: text})
    });
    const json = await res.json();
    // remove last "thinking"
    const nodes = chatEl.querySelectorAll(".message.bot");
    if(nodes.length) nodes[nodes.length-1].remove();
    appendMessage(json.reply || "No response from server.");
  } catch (err) {
    const nodes = chatEl.querySelectorAll(".message.bot");
    if(nodes.length) nodes[nodes.length-1].remove();
    appendMessage("Could not reach server. Make sure backend is running at http://127.0.0.1:5000");
    console.error(err);
  }

  return false; // prevent form submit
}

function fillExample(txt){
  inputEl.value = txt;
  inputEl.focus();
}
