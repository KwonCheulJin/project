let nums = [];
for (let i = 1; i < 46; i++) {
    nums.push(i)
}

let myNum = [];
for (let j = 1; j < 999; j++) {
    let randomNum = Math.floor(Math.random() * nums.length) + 1;
    if (myNum.indexOf(randomNum) == -1) {
        myNum.push(randomNum);
        if (myNum.length == 6) {
            break;
        }
    }
}

function sortNum(a,b){
    return a-b;
}
myNum.sort(sortNum);
console.log(myNum)