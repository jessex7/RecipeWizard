// applies to: create_or_edit macro
if (document.querySelector('.save-recipe-btn') != null) {
    document.querySelector('.save-recipe-btn').addEventListener('click', saveData);
};

// applies to: create_or_edit macro
if (document.querySelector('.add-row-btn') != null) {
    document.querySelector('.add-row-btn').addEventListener('click',addRowToBottom);
}

// applies to: create_or_edit macro
if (document.querySelectorAll('.delete-row-btn') != null) {
    let deleteRowBtns = document.querySelectorAll('.delete-row-btn');
    for (let index = 0; index < deleteRowBtns.length; index++) {
        deleteRowBtns[index].addEventListener('click', removeRow);
    };
};

// applies to: create_card macro
if (document.querySelector('.delete-recipe-btn') != null) {
    let deleteRecipeBtns = document.querySelectorAll('.delete-recipe-btn');
    for (let index = 0; index < deleteRecipeBtns.length; index++) {
        deleteRecipeBtns[index].addEventListener('click', deleteRecipe);
    };
};

// applies to: selections.html
if (document.querySelector('.add-to-list-btn') != null) {
    let addToListBtns = document.querySelectorAll('.add-to-list-btn');
    for (let index = 0; index < addToListBtns.length; index++) {
        addToListBtns[index].addEventListener('click', addRecipeToList);
    };
};

// applies to: selections.html
if (document.querySelector('#generate-list-btn') != null) {
    document.querySelector('#generate-list-btn').addEventListener('click', generateGroceryList);
};

// applies to grocery-list.html
if (document.querySelector('.delete-grocery-item-btn') != null) {
    const deleteGroceryItemBtns = document.querySelectorAll('.delete-grocery-item-btn');
    for (let index = 0; index < deleteGroceryItemBtns.length; index++) {
        deleteGroceryItemBtns[index].addEventListener('click', removeGroceryItem);
    }
}

// applies to: grocery-list.html
if (document.querySelector('.add-list-item-btn') != null) {
    document.querySelector('.add-list-item-btn').addEventListener('click', addGroceryListItemRow);
}

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
    const parentRow = e.target.parentNode.parentNode.parentNode;
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

        const svgIcon = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        svgIcon.setAttribute('width', '16');
        svgIcon.setAttribute('height', '16');
        svgIcon.setAttribute('fill', 'currentColor');
        svgIcon.classList.add('bi', 'bi-x-circle');
        svgIcon.setAttribute('viewbox', '0 0 16 16');

        const svgPathA = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        svgPathA.setAttribute('d',
        'M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z');
        const svgPathB = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        svgPathB.setAttribute('d',
        'M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z');
        svgIcon.appendChild(svgPathA);
        svgIcon.appendChild(svgPathB);
        button.appendChild(svgIcon);

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

function deleteGroceryList(e) {
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

function addRecipeToList(e) {
    const tgt = e.currentTarget;
    console.log(tgt);
    const parent = tgt.parentNode;
    console.log(parent);
    const recipeTitle = parent.children[0].firstChild.data;
    console.log(parent.parentNode);
    const recipeId = parent.parentNode.dataset.recipeId;
    console.log(recipeTitle);
    const listItem = document.createElement('li');
    listItem.dataset.recipe_id = recipeId;
    const selectedRecipesList = document.querySelector('#selected-recipe-list');
    const listItemParagraph = document.createElement('p');
    listItemParagraph.innerHTML = recipeTitle;
    listItem.appendChild(listItemParagraph);
    const deleteBtn = document.createElement('button');
    deleteBtn.type = 'button';
    deleteBtn.className = 'delete-list-item-btn';
    deleteBtn.addEventListener('click', removeListItem);
    deleteBtn.appendChild(createRedEncircledX())
    listItem.appendChild(deleteBtn);
    selectedRecipesList.appendChild(listItem);
}

function removeListItem(e) {
    const tgt = e.currentTarget;
    console.log(tgt);
    const parent = tgt.parentNode;
    console.log(parent);
    console.log("Parent node: ", parent);
    parent.remove();
}

function removeGroceryItem(e) {
    const tgt = e.currentTarget;
    const parent = tgt.parentNode;
    console.log(parent);
    parent.remove();
}

function addGroceryListItemRow() {
    const groceryList = document.querySelector('#grocery-list');
    const newListItem = document.createElement('li');
    const newInput = document.createElement('input');
    newInput.className = 'chill input';
    newInput.name = 'grocery-item';
    newInput.value = '';

    const newBtn = document.createElement('button');
    newBtn.className = 'delete-grocery-item svg-btn-wrapper';
    newBtn.type = 'button';
    newBtn.appendChild(createRedEncircledX());
    newBtn.addEventListener('click', removeGroceryItem)
    
    newListItem.appendChild(newInput);
    newListItem.appendChild(newBtn);
    groceryList.appendChild(newListItem);

}

function generateGroceryList() {
    const listOfRecipes = document.querySelectorAll('#selected-recipe-list>li');
    const listOfRecipeIds = [];
    for (let i = 0; i < (listOfRecipes.length) ;i++) {
        listOfRecipeIds.push(listOfRecipes[i].dataset.recipe_id);
    }
    const postEndpoint = document.querySelector('#generate-list-btn').dataset.postEndpoint;
    const payload = {
        recipe_ids: listOfRecipeIds
    };
    fetch(postEndpoint, {
        method: 'POST',
        body: JSON.stringify(payload),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(
        response => {
            if (response.status == 200) {
                window.location = response.url
            } else {
                alert(response.status)
            }
        }
    )
}

function createRedEncircledX() {
    const svgIcon = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svgIcon.setAttribute('width', '16');
    svgIcon.setAttribute('height', '16');
    svgIcon.setAttribute('fill', 'currentColor');
    svgIcon.classList.add('bi', 'bi-x-circle');
    svgIcon.setAttribute('viewbox', '0 0 16 16');

    const svgPathA = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    svgPathA.setAttribute('d',
    'M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z');
    const svgPathB = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    svgPathB.setAttribute('d',
    'M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z');
    svgIcon.appendChild(svgPathA);
    svgIcon.appendChild(svgPathB);
    return svgIcon;
}