let startX;
let startScrollLeft;
let isDragging = false;

function startDrag(event) {
  isDragging = true;
  startX = event.pageX - document.querySelector('.banner-container-g').offsetLeft;
  startScrollLeft = document.querySelector('.banner-container-g').scrollLeft;
  document.addEventListener('mousemove', drag);
  document.addEventListener('mouseup', stopDrag);
  document.querySelector('.banner-container-g').classList.add('draggable');
}

function drag(event) {
  if (!isDragging) return;
  const x = event.pageX - document.querySelector('.banner-container-g').offsetLeft;
  const walk = (x - startX) * 2;
  document.querySelector('.banner-container-g').scrollLeft = startScrollLeft - walk;
}

function stopDrag() {
  isDragging = false;
  document.removeEventListener('mousemove', drag);
  document.removeEventListener('mouseup', stopDrag);
  document.querySelector('.banner-container-g').classList.remove('draggable');
}

let startX_P;
let startScrollLeft_P;
let isDragging_P = false;

function startDragP(event) {
  isDragging_P = true;
  startX_P = event.pageX - document.querySelector('.banner-container-p').offsetLeft;
  startScrollLeft_P = document.querySelector('.banner-container-p').scrollLeft;
  document.addEventListener('mousemove', dragP);
  document.addEventListener('mouseup', stopDragP);
  document.querySelector('.banner-container-p').classList.add('draggable');
}

function dragP(event) {
  if (!isDragging_P) return;
  const x_P = event.pageX - document.querySelector('.banner-container-p').offsetLeft;
  const walk_P = (x_P - startX_P) * 2;
  document.querySelector('.banner-container-p').scrollLeft = startScrollLeft_P - walk_P;
}

function stopDragP() {
  isDragging_P = false;
  document.removeEventListener('mousemove', dragP);
  document.removeEventListener('mouseup', stopDragP);
  document.querySelector('.banner-container-p').classList.remove('draggable');
}
