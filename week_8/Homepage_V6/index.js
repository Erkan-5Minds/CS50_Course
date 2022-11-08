menu1IsOpen  = false;
menu2IsOpen  = false;
menu3IsOpen  = false;

function openOnClick(number) {
  num = number;
  const arrow1 = document.getElementById("projekt_one_arrow");
  const projektOneContainer = document.getElementById("projekt_one_container");
  if (menu1IsOpen) {
    if (number == 1) {
      arrow1.src = "img/Arrow_Right.png"
      projektOneContainer.style.display = "none";
      menu1IsOpen  = false;
    }
  } else {
    if (number == 1) {
      arrow1.src = "img/Arrow_Down.png"
      projektOneContainer.style.display = "block";
      menu1IsOpen = true;
    }
  }

  const arrow2 = document.getElementById("projekt_two_arrow");
  const projektTwoContainer = document.getElementById("projekt_two_container");
  if (menu2IsOpen) {
    if (number == 2) {
      arrow2.src = "img/Arrow_Right.png";
      projektTwoContainer.style.display = "none";
      menu2IsOpen = false;
    }
  } else {
    if (number == 2) {
      arrow2.src = "img/Arrow_Down.png";
      projektTwoContainer.style.display = "block";
      menu2IsOpen = true;
    }
  }

  const arrow3 = document.getElementById("projekt_three_arrow");
  const projektThreeContainer = document.getElementById("projekt_three_container");
  if (menu3IsOpen) {
    if (number == 3) {
      arrow3.src = "img/Arrow_Right.png";
      projektThreeContainer.style.display = "none";
      menu3IsOpen = false;
    }
  } else {
    if (number == 3) {
      arrow3.src = "img/Arrow_Down.png";;
      projektThreeContainer.style.display = "block";
      menu3IsOpen = true;
    }
  }
}
