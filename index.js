document.querySelector("#card1 button").onclick = () => {
  document.querySelector("#card1").classList.add("hidden-left");
  document.querySelector("#card2").classList.remove("hidden-right");
  fetch(`/flips-for/${document.querySelector("#card1 input").value}`).then((resp) => {
    console.log(resp.status);
    if (resp.status == 200) {
      return resp.json();
    } else {
      document.querySelector("#card2").classList.add("hidden-left");
      document.querySelector("#card4").classList.remove("hidden-right");
    }
  }).then((resp) => {
    console.log(resp);
  })
}
