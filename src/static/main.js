let disableTimeouts = [];

function disableForm() {
  disableTimeouts.push(setTimeout(() => 
    document.getElementById(`overlay`).style.display = "flex"
  , 400));
}

function enableForm() {
  disableTimeouts.forEach(t => clearTimeout(t));
  disableTimeouts = [];
  document.getElementById(`overlay`).style.display = "none";
}

document.getElementById("colorPicker").addEventListener("input", (e) => {
  setColor(e.target.value);
});

document.getElementById("brightness-float").addEventListener("input", (e) => {
  setBrightness(e.target.value);
});
setBrightness(0.05);

const effects = ["none", "breathe", "candle", "party", "spiral", "huerotate"];
for (let [effect, param, type] of [
  ["breathe", "min", "float"],
  ["breathe", "max", "float"],
  ["breathe", "frequency", "float"],
  ["candle", "factor", "float"],
  ["candle", "windiness", "float"],
  ["party", "speed", "float"],
  ["party", "saturation", "float"],
  ["party", "value", "float"],
  ["party", "per-pixel", "bool"],
  ["spiral", "length", "int"],
  ["huerotate", "speed", "float"],
]) {
  try {
    document.getElementById(`${effect}-${param}-${type}`).addEventListener("input", (e) => {
      let value = type=="bool" ? e.target.checked : e.target.value;
      setParameter(param, value, type);
    });
  } catch (e) {
    console.log("Could not add event listener for parameter:", effect, param);
  }
}

function send(URL, data) {
  disableForm();
  fetch("/tree/" + URL, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((response) => enableForm())
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
function setParameter(key, value, type) {
  send("effect/parameter/", { "key": key, "value": value, "type": type });
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
