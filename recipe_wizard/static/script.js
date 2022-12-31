

// create.html & edit.html functionality
if (document.querySelector('.save-btn') != null) {
    document.querySelector('.save-btn').addEventListener('click', saveData);
    document.querySelector('.add-row-btn').addEventListener('click',addRowToBottom);
    let deleteRowBtns = document.querySelectorAll('.delete-row-btn');
    for (let index = 0; index < deleteRowBtns.length; index++) {
        deleteRowBtns[index].addEventListener('click', removeRow);
    };
};

// index.html functionality
if (document.querySelector('.edit-link') != null) {
    let deleteRecipeBtns = document.querySelectorAll('.delete-recipe-btn');
    for (let index = 0; index < deleteRecipeBtns.length; index++) {
        deleteRecipeBtns[index].addEventListener('click', deleteRecipe);
    };
};

// selections.html functionality
if (document.querySelector('.add-to-list-btn') != null) {
    let addToListBtns = document.querySelectorAll('.add-to-list-btn');
    for (let index = 0; index < addToListBtns.length; index++) {
        addToListBtns[index].addEventListener('click', addRecipeToList);
    };
};

function saveData() {
    let recipe = {
        recipe_name: document.querySelector('.recipe-title').value,
        author: document.querySelector('.author-input').value,
        rating: document.querySelector('.rating-input').value,
        prep_time: document.querySelector('.prep-time-input').value,
        cook_time: document.querySelector('.cook-time-input').value,
        instructions: document.querySelector('.instructions-input').value,
    };

    const tbody = document.querySelector('tbody');
    const rows = tbody.children
    let ingredients = [];
    for (let i = 0; i < (rows.length) ;i++) {
        if(rows[i].className === 'input-row' || rows[i].className === 'standard-row') {
            let ingredientRow = {};
            let rowTableData = rows[i].children;
            for (let x = 0; x < (rowTableData.length-1); x++ ) {
                if (rowTableData[x].firstChild.className === 'ingredient-name-input') {
                    ingredientRow['ingredient_name'] = rowTableData[x].firstChild.value;
                } else if (rowTableData[x].firstChild.className === 'ingredient-amount-input') {
                    ingredientRow['amount'] = parseFloat(rowTableData[x].firstChild.value);
                } else if (rowTableData[x].firstChild.className === 'ingredient-unit-input') {
                    ingredientRow['unit'] = rowTableData[x].firstChild.value;
                }
            }
            ingredients.push(ingredientRow);
        }
    }
    recipe['ingredients'] = ingredients;
    console.log(recipe)
    const targetURL = document.URL
    fetch(targetURL, {
        method: 'POST',
        body: JSON.stringify(recipe),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(
        response => {
            if (response.redirected) {
                window.location = response.url
            } else {
                alert(response.status)
            }
        }
    )
}

function removeRow(e) {
    console.log(e)
    const parentRow = e.target.parentNode.parentNode;
    parentRow.remove()

}

function addRowToBottom() {
        // construct a new row
        const tbody = document.querySelector('tbody');
        const newTableRow = document.createElement('tr');
        newTableRow.className = 'standard-row';
    
        // construct the cells
        const nameCell = document.createElement('td');
        nameCell.className = 'row-ingredient';
        const nameInput = document.createElement('input');
        nameInput.name = 'ingredient-name';
        nameInput.type = 'text';
        nameInput.className = 'ingredient-name-input';
        nameCell.appendChild(nameInput);
        newTableRow.appendChild(nameCell);
    
        const amountCell = document.createElement('td');
        amountCell.className = 'row-amount';
        const amountInput = document.createElement('input');
        amountInput.name = 'ingredient-amount';
        amountInput.className = 'ingredient-amount-input';
        amountInput.type = 'number';
        amountCell.appendChild(amountInput);
        newTableRow.appendChild(amountCell);
    
        const unitCell = document.createElement('td');
        unitCell.className = 'row-unit';
        const unitInput = document.createElement('input');
        unitInput.name = 'ingredient-unit';
        unitInput.type = 'text';
        unitInput.className = 'ingredient-unit-input'
        unitCell.appendChild(unitInput);
        newTableRow.appendChild(unitCell);
    
        const buttonCell = document.createElement('td');
        buttonCell.className = 'button';
        const button = document.createElement('button');
        button.type = 'button';
        button.className = 'delete-row-btn';
        button.textContent = 'x';
        button.addEventListener('click', removeRow)
        buttonCell.appendChild(button);
        newTableRow.appendChild(buttonCell);
        tbody.appendChild(newTableRow);
}

function deleteRecipe(e) {
    const tgt = e.currentTarget
    const link = tgt.children[1];
    const deleteEndpoint = link.href;

    fetch(deleteEndpoint, {
        method: 'DELETE',
    })
    .then(
        response => {
            if (response.redirected) {
                window.location = response.url
            } else {
                alert(response.status)
            }
        }
    )
}



// selection.html functionality
function addRecipeToList(e) {
    const tgt = e.currentTarget;
    console.log(tgt);
    const parent = tgt.parentNode;
    console.log(parent);
    const recipeTitle = parent.children[0].firstChild.data;
    console.log(recipeTitle);

    const tbody = document.querySelector('.selection-tbody');
    console.log(tbody);
    const newTableRow = document.createElement('tr');
    newTableRow.className = 'selected-recipe-row';

    // construct the cells
    const nameCell = document.createElement('td');
    nameCell.className = 'recipe-title-cell';
    const namePara = document.createElement('p');
    namePara.innerHTML = recipeTitle;
    nameCell.appendChild(namePara);
    newTableRow.appendChild(nameCell);
    tbody.appendChild(newTableRow);

}