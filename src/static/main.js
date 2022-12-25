document.getElementById("colorPicker").addEventListener("input", (e) => {
  setColor(e.target.value);
});

document.getElementById("brightness-range").addEventListener("input", (e) => {
  setBrightness(e.target.value);
});

for (let [effect, param] of [
  ["breathe", "min"],
  ["breathe", "max"],
  ["breathe", "frequency"],
  ["candle", "factor"],
  ["candle", "windiness"],
  ["party", "speed"]
]) {
  try {
    document.getElementById(`${effect}-${param}-range`).addEventListener("input", (e) => {
      setParameter(param, e.target.value);
    });
  } catch (e) {
    console.log("Could not add event listener for parameter:", effect, param);
  }
}

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
function setEffect(effect) {
  send("effect/", { "effect-name": effect });
  dispayHTML(effect);
}
function setParameter(key, value) {
  send("effect/parameter/", { "key": key, "value": value });
}

let timer = null;

function closeMessage() {
  document.getElementById("message-container").innerHTML = "";
}

function setMessage(message) {
  document.getElementById(
    "message-container"
  ).innerHTML = `<div class="flex justify-center">
            <div class="flex gap-4 bg-green-300 rounded-xl px-4 py-2 w-[350px] justify-between">
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

  if (!Array.isArray(savedColors)) savedColors = [];

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

function reapplyColor() {
  setColor(document.getElementById('colorPicker').value);
}

function removeColor() {
    if (currentColor == null) return;
    savedColors = savedColors.filter(c => c != currentColor);
    window.localStorage.setItem("savedColors", JSON.stringify(savedColors));
  
    loadSavedColors();
}

loadSavedColors();

const effects = ["none", "breathe", "candle", "party"];
function dispayHTML(name) {
  for (let effect of effects) {
    let id = `${effect}-parameters`;
    try {
      document.getElementById(id).style.display = "none";
    } catch (e) {}
  }
  try {
    document.getElementById(`${name}-parameters`).style.display = "flex";
  } catch (e) {}
}