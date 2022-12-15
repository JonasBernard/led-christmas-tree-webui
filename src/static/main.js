document.getElementById("colorPicker").addEventListener("input", (e) => {
  setColor(e.target.value);
});

document.getElementById("brightness-range").addEventListener("input", (e) => {
  setBrightness(e.target.value);
});

function send(URL, data) {
  fetch("/tree/" + URL, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((response) => setMessage(response.message));
}

let currentColor = "#ffffff";

function setColor(color) {
  currentColor = color;
  send("color/", { color: color });
}
function setBrightness(brightness) {
  send("brightness/", { brightness: brightness });
}
function turnOn() {
  send("on/", null);
}
function turnOff() {
  send("off/", null);
}

let timer = null;

function closeMessage() {
  document.getElementById("message-container").innerHTML = "";
}

function setMessage(message) {
  document.getElementById(
    "message-container"
  ).innerHTML = `<div class="flex justify-center">
            <div class="flex gap-4 bg-green-300 rounded-xl px-4 py-2">
                ${message}
                <span><button onclick="closeMessage()">&#x2715</s></span>
            </div>
        </div>`;

  if (timer != null) {
    clearTimeout(timer);
  }
  timer = setTimeout(closeMessage, 2000);
}

let savedColors = [];

function saveColor() {
  if (currentColor == null) return;
  if (savedColors.includes(currentColor)) return;
  savedColors.push(currentColor);
  window.localStorage.setItem("savedColors", JSON.stringify(savedColors));

  loadSavedColors();
}

function loadSavedColors() {
  savedColors = JSON.parse(window.localStorage.getItem("savedColors"));

  let genHTML = "";
  for (let color of savedColors) {
    genHTML += `\n<button class="px-3 py-1 rounded-xl" style="height: 1.5em; background-color: ${color}" onclick="applyColor('${color}')"></button>`;
  }

  document.getElementById("savedColorHolder").innerHTML = genHTML;
}

function applyColor(color) {
    document.getElementById('colorPicker').value = color;
    setColor(color);
}

function removeColor() {
    if (currentColor == null) return;
    savedColors = savedColors.filter(c => c != currentColor);
    window.localStorage.setItem("savedColors", JSON.stringify(savedColors));
  
    loadSavedColors();
}

loadSavedColors();