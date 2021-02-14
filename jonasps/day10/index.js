const fs = require('fs').promises;

// Part 1
async function getInput() {
    try {
        const data = await fs.readFile('input.txt', 'utf-8');
        return data.toString().split(/\r?\n/)
    } catch (error) {
        console.log(error)
    }
}

async function getNumbersArray() {
    const data = await getInput().then(response => {
        numbers = [0]
        response.forEach(element => {
            numbers.push(parseInt(element));
        });
        return numbers.sort((a, b) => b - a);
    });
    return data;
}

getNumbersArray().then(res => {
    let one = 0;
    let two = 0;
    let three = 0;
    for (let i = 0; i < res.length;  i++) {
        const checkNum = res[i+1] - res[i];
        switch (checkNum) {
            case -1:
                one = one + 1;
                break;
            case -2:
                two = two + 1;
                break;
            case -3:
                three = three + 1;
                break;
            default:
                if (i, res.length) {
                    three = three + 1;
                }
                break;
        }
    }
    return({ one, two, three });
}).then(response => {
    // answer
    console.log(response, response.one * response.three);
})

// Part 2
// This can be solved with dynamic programming,
// All possible combinations are equal to the total sum of all previous combinations that can be reached
// from the current value.

// We start with the biggest value, add a new item, calculate 
// the possible combinations and save the value for that item, and continue down to value 0.
getNumbersArray().then(e => {
    const possibleMovesAtIndex = {};
    const all = [e[0] + 3, ...e]
    all.forEach((item, index) => {
        let value = 1;
        let isSet = false;
        if (all[index - 1] - item <= 3) {
            value = possibleMovesAtIndex[index - 1];
            isSet = true;
        }
        if (index >= 3 && all[index - 2] - item <= 3) {
            if (isSet) {
                value += possibleMovesAtIndex[index - 2];
            } else {
                value = possibleMovesAtIndex[index - 2];
            }
        }
        if (index >= 4 && all[index - 3] - item === 3) {
            if (isSet) {
                value += possibleMovesAtIndex[index - 3];
            } else {
                value = possibleMovesAtIndex[index - 3];
            }
        }
        possibleMovesAtIndex[`${index}`] = value;
    })
    console.log(possibleMovesAtIndex[all.length -1]);
});
