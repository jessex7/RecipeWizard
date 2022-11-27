document.querySelector('.ingredients').addEventListener('click', function(e) {
    if(e.target && e.target.className === 'plus-button') {
        addRow();
    } else if (e.target && e.target.className === 'delete-button') {
        removeRow(e);
    } else {
        
    }
});

function removeRow(e) {
    console.log(e)
    const parentRow = e.target.parentNode.parentNode;
    parentRow.remove()

}

function addRow() {
    // extract elements & values from DOM
    const nameElement = document.querySelector('.ingredient-name-input');
    const amountElement = document.querySelector('.ingredient-amount-input');
    const unitElement = document.querySelector('.ingredient-unit-input');
    const name = nameElement.value;
    const amount = amountElement.value;
    const unit = unitElement.value;

    // clean up view
    nameElement.value = '';
    amountElement.value = '';
    unitElement.value = '';

    // construct a new row
    const tbody = document.querySelector('tbody');
    const newTableRow = document.createElement('tr');
    newTableRow.className = 'standard-row';

    // construct the cells
    const nameCell = document.createElement('td');
    nameCell.className = 'ingredient-name';
    const nameInput = document.createElement('input');
    nameInput.name = 'ingredient-name[]';
    nameInput.type = 'text';
    nameCell.appendChild(nameInput);
    newTableRow.appendChild(nameCell);

    const amountCell = document.createElement('td');
    amountCell.className = 'ingredient-amount';
    const amountInput = document.createElement('input');
    amountInput.name = 'ingredient-amount[]';
    amountInput.type = 'number';
    amountCell.appendChild(amountInput);
    newTableRow.appendChild(amountCell);

    const unitCell = document.createElement('td');
    unitCell.className = 'ingredient-unit';
    const unitInput = document.createElement('input');
    unitInput.name = 'ingredient-unit[]';
    unitInput.type = 'text';
    unitCell.appendChild(unitInput);
    newTableRow.appendChild(unitCell);

    const buttonCell = document.createElement('td');
    buttonCell.className = 'button';
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'delete-button';
    button.textContent = 'x';
    buttonCell.appendChild(button);
    newTableRow.appendChild(buttonCell);

    // insert populated values into new row
    nameInput.value = name;
    amountInput.value = amount;
    unitInput.value = unit;
    tbody.appendChild(newTableRow);
    console.log("ITS WORKING");

    // const form = document.querySelector('recipe-form');
    // const buttonDiv = document.createElement('div');
    // buttonDiv.className = 'form-row';
    // const saveButton = document.createElement('button');
    // saveButton.id = 'save-button';
    // saveButton.formMethod = 'post';
    // saveButton.formAction = 

    // wish i had known this function existed before constructing an entire tr by hand
    //tbody.insertRow()

}
