console.log('helloo from ts');


let myString: string;
let myNum: number
let myBool: boolean;
let strArr: string[];
let myVoid: void;

myVoid = undefined;
myString = 'hellooo world my string'.slice(0, 15);
myNum = 7;
myBool = true;

interface numberZ{
    num1: any;
    num2: number;
}

function getsum(nums: numberZ):number{
    if( typeof nums.num1 == 'string' ){
        nums.num1 = parseInt(nums.num1);
        console.log(nums.num1);
    }
    return nums.num1+nums.num2;
}


let numsz = {num1:'3',num2:7}


console.log(myString, myNum, myBool, myVoid, getsum( numsz ) );
