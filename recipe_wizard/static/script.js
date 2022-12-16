

// create.html & edit.html functionality
if (document.querySelector('.save-btn') != null) {
    document.querySelector('.save-btn').addEventListener('click', saveData);
    document.querySelector('.add-row-btn').addEventListener('click',addRowToBottom);
    let deleteRowBtns = document.querySelectorAll('.delete-row-btn');
    for (let index = 0; index < deleteRowBtns.length; index++) {
        deleteRowBtns[index].addEventListener('click', removeRow);
    };
    document.querySelector('.delete-recipe-btn').addEventListener('click',deleteRecipe);
};

// index.html functionality
if (document.querySelector('.edit-link') != null) {
    let deleteRecipeBtns = document.querySelectorAll('.delete-recipe-btn');
    for (let index = 0; index < deleteRecipeBtns.length; index++) {
        deleteRecipeBtns[index].addEventListener('click', deleteRecipe);
    };
};

function saveData() {
    let recipe = {
        recipe_name: document.querySelector('#recipe_name').value,
        author: document.querySelector('#author').value,
        rating: document.querySelector('#rating').value,
        prep_time: document.querySelector('#prep_time').value,
        cook_time: document.querySelector('#cook_time').value,
        instructions: document.querySelector('#instructions').value,
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
        buttonCell.appendChild(button);
        newTableRow.appendChild(buttonCell);
        tbody.appendChild(newTableRow);
}

function deleteRecipe(e) {
    //const deleteEndpoint = document.URL.slice(0,-5)
    const tgt = e.currentTarget
    const paths = tgt.children[0];
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





// if (document.querySelector('.delete-recipe-btn') != null) {
//     document.querySelector('.delete-recipe-button').addEventListener('click', deleteItem);
// }

// function deleteItem(e) {
//     const recipeElement = e.target.parentNode.parentNode.parentNode;
//     const deleteEndpoint = recipeElement.lastElementChild.href;
//     fetch(deleteEndpoint, {
//         method: 'DELETE',
//     })
//     .then(
//         response => {
//             if (response.redirected) {
//                 window.location = response.url
//             } else {
//                 alert(response.status)
//             }
//         }
//     )
// }


// document.querySelector('.ingredients').addEventListener('click', function(e) {
//     if(e.target && e.target.className === 'plus-button') {
//         addRow();
//     } else if (e.target && e.target.className === 'delete-row-btn') {
//         removeRow(e);
//     } else {
        
//     }
// });

// index.html functionality

// if (document.querySelector('.edit-recipe-button') != null) {
//     document.querySelector('.edit-recipe-button').addEventListener('click', editItem);
// }


// function editItem(e) {
//     const recipeElement = e.target.parentNode.parentNode.parentNode;
//     const editEndpoint = recipeElement.lastElementChild.href;
//     location.href = editEndpoint;
//     // fetch(editEndpoint, {
//     //     method: 'GET'
//     // })
//     // .then(function(response) {
//     //     return response.text();
//     // })
//     // .then(function(html) {
//     //     document.body.innerHTML = html;
//     // });
// }