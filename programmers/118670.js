//푸는중  rotate 고쳐야함..
function solution(rc, operations) {
    let rotateNumber = 0;
    let shiftRowNumber = 0;

    operations.map((element)=>{
        if (element === "Rotate") {
            rotateNumber ++;
            if (shiftRowNumber > 0) {
                rc = shiftRow(rc, shiftRowNumber);
                shiftRowNumber = 0;
            }
        }
        else {
            shiftRowNumber ++;
            if(rotateNumber>0){
                rc = rotate(rc, rotateNumber);
                rotateNumber = 0;
            }

        }
    })
    rc = shiftRowNumber > 0 ? shiftRow(rc, shiftRowNumber) : rotate(rc, rotateNumber);

    return rc;
}

function shiftRow(rc, n) {
    const result = [];
    n = n % rc.length;
    if (n !==0 ) {
        for (let i = rc.length-n; i< rc.length; i++){
            result.push(rc[i]);
        }
        for (let i = 0; i<rc.length-n; i++) {
            result.push(rc[i])
        }
    }
    return result;
}

function rotate(rc, n) {
    let = borderSize = (rc[0].length * 2) + ((rc.length -2) * 2);
    n = n % borderSize;
    if (n === 0) {
        return rc;
    }

    const border = [];
    let columnSize = rc[0].length;
    for (let i = 0; i < columnSize; i++) {
        border.push(rc[0][i]);
    }
    for (let i = 1; i < rc.length-1; i++) {
        border.push(rc[i][columnSize-1]);
    }
    for (let i = columnSize-1; i >= 0; i--) {
        border.push(rc[rc.length-1][i]);
    }
    for (let i = rc.length-2; i > 0; i --) {
        border.push(rc[i][0]);
    }

    let borderResult = border.slice(borderSize-n);
    borderResult.push(...border.slice(0,borderSize-n));

    let borderCnt = 0;
    for (let i =0; i< columnSize; i++) {
        rc[0][i] = borderResult[borderCnt];
        borderCnt++;
    }
    for (let i = 1; i < rc.length-1; i++) {
        rc[i][columnSize-1] = borderResult[borderCnt];
        borderCnt++;
    }
    for (let i = columnSize-1; i>=0; i--) {
        rc[rc.length-1][i] = borderResult[borderCnt];
        borderCnt++;
    }
    for (let i = rc.length-2; i > 0; i --) {
        rc[i][0] = borderResult[borderCnt];
        borderCnt ++;
    }
    return rc;
}
//38637948

// console.log(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]));
console.log(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]));
