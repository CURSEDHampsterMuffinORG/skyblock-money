document.querySelector("#card1 button").onclick = () => {
  document.querySelector("#card1").classList.add("hidden-left");
  document.querySelector("#card2").classList.remove("hidden-right");
}
