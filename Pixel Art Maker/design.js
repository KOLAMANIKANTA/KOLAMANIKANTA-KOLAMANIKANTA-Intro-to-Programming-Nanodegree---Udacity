// Grid mount function
function makeGridFun() {

  // Storing grid height value
  const gridHeightValue= document.getElementById('input_height').value;
  // Storing grid width value
  const gridWidthValue = document.getElementById('input_width').value;
  // Storing table canvas
  const tableCanvas = document.getElementById('pixel_canvas');

  // Delete rows to start
  tableCanvas.innerHTML = '';

  // Loop to insert the rows
  for (let i = 0; i < gridHeightValue; i++) {
    let row = tableCanvas.insertRow(i);

    // Loop to insert the cells
    for (let j = 0; j < gridWidthValue; j++) {
      let cell = row.insertCell(j);

      // Add click event to the cells
      cell.addEventListener('click', function(event) {
        // When the cell is clicked, the background color changes to the selected color
        event.target.style.backgroundColor = document.getElementById('colorPicker').value;
      });
    }
  }
}

// Add click event to the submit input
document.getElementById('sizePicker').addEventListener('submit', function(event) {
  event.preventDefault();
  // When the data is submitted the grid mount function is called
  makeGridFun();
});