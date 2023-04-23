// get all task elements
const taskElems = document.querySelectorAll('.task.id li');

// loop through task elements
taskElems.forEach((taskElem) => {
  // get title and description
  const title = taskElem.querySelector('a').textContent;
  const description = taskElem.querySelector('p').textContent;

  // create pop-up element
  const popup = document.createElement('div');
  popup.classList.add('popup');
  popup.innerHTML = `
    <h3>${title}</h3>
    <p>${description}</p>
  `;

  // show pop-up on hover
  taskElem.addEventListener('mouseover', () => {
    document.body.appendChild(popup);
  });

  // hide pop-up on mouse out
  taskElem.addEventListener('mouseout', () => {
    popup.remove();
  });
});
