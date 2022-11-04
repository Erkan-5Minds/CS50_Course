const button = document.getElementById('button');
document.addEventListener('mousemove', (e) => {
  const buttonLeft = button.offsetLeft;
  const buttonTop = button.offsetTop;
  let x = e.pageX;
  let y = e.pageY;

  let newbuttonLeft;
  let newbuttonTop;
  // console.log(y)

  mouseFromBottomLeft = ((x < buttonLeft && x > buttonLeft - 75) && (y < buttonTop && y > buttonTop - 75))
  mouseFromTopRight = (x > buttonLeft + 320)
  if(mouseFromBottomLeft) {
    newbuttonLeft = buttonLeft + 10 + "px";
    newbuttonTop = buttonTop + 10 + "px";
    button.style.left = newbuttonLeft;
    button.style.top = newbuttonTop;
  }else if(mouseFromTopRight) {
    
  }
})
