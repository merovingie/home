console.log('helloo from ts');
var myString;
var myNum;
var myBool;
var strArr;
var myVoid;
myVoid = undefined;
myString = 'hellooo world my string'.slice(0, 15);
myNum = 7;
myBool = true;
function getsum(nums) {
    if (typeof nums.num1 == 'string') {
        nums.num1 = parseInt(nums.num1);
        console.log(nums.num1);
    }
    return nums.num1 + nums.num2;
}
var numsz = { num1: '3', num2: 7 };
console.log(myString, myNum, myBool, myVoid, getsum(numsz));
