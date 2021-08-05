document.querySelector("#card5 button.back").onclick = () => {
  var moneyCards = document.querySelectorAll(".money-card.hidden-left");
  if (moneyCards.length > 0) {
    document.querySelector("#card5").classList.add("hidden-right");
    moneyCards[moneyCards.length - 1].classList.remove("hidden-left");
  }
};

document.querySelector("#card5 button.reload").onclick = () => {
  window.location.reload();
};

document.querySelector("#card1 button").onclick = () => {
  document.querySelector("#card1").classList.add("hidden-left");
  document.querySelector("#card2").classList.remove("hidden-right");

  fetch(`/flips-for/${document.querySelector("#card1 input").value}`).then((resp) => {
    console.log(resp.status);
    if (resp.status == 200) {
      return resp.json();
    }/* else {
      document.querySelector("#card2").classList.add("hidden-left");
      document.querySelector("#card4").classList.remove("hidden-right");
    }*/
  }).then((resp) => {
    if (resp == undefined) return;
    window.flips = resp;
    setTimeout(() => {
      document.querySelector("#card2").classList.add("hidden-left");
      renderFlip(window.flips.shift());
    }, 1000); // If we don't delay the stuff, the users don't get to see my *wonderful* loading bar!
    // besides they'll think it's a crappy calculator that's just giving them false results
  })
}

function renderFlip(flip) {
  var clone = document.querySelector("template").content.cloneNode(true);
  // Process the flip data
  clone.querySelector(".item").innerHTML = flip["item"];
  clone.querySelector(".profit").innerHTML = `$${flip["profit"]}`;
  // Process the buying data
  clone.querySelector(".buyInfo .buySource").innerHTML = flip["buying"]["source"];
  clone.querySelector(".buyInfo .price").innerHTML = `$${flip["buying"]["cost"]}`;
  clone.querySelector(".buyInfo .buyDetails").innerHTML = flip["buying"]["details"];
  // Process the selling data
  clone.querySelector(".sellInfo .sellSource").innerHTML = flip["selling"]["source"];
  clone.querySelector(".sellInfo .price").innerHTML = `$${flip["selling"]["cost"]}`;
  clone.querySelector(".sellInfo .sellDetails").innerHTML = flip["selling"]["details"];
  // Finish rendering
  var renderedFlip = clone.children[0];
  clone.querySelector("button.next").onclick = () => {
    renderedFlip.classList.add("hidden-left");
    if (window.flips.length > 0) {
      renderFlip(window.flips.shift());
    } else if (document.querySelector(".money-card.hidden-right")) {
      document.querySelector(".money-card.hidden-right").classList.remove("hidden-right");
    } else {
      document.querySelector("#card5").classList.remove("hidden-right");
    }
  };
  clone.querySelector("button.back").onclick = () => {
    var moneyCards = document.querySelectorAll(".money-card.hidden-left");
    if (moneyCards.length > 0) {
      renderedFlip.classList.add("hidden-right");
      moneyCards[moneyCards.length - 1].classList.remove("hidden-left");
    }
  };
  document.body.appendChild(renderedFlip);
  setTimeout(() => {renderedFlip.classList.remove("hidden-right")}, 100);
}
