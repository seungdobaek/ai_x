let num1 = 20;
let num2 = 20;
let difference = (num1>num2) ? num1-num2 : num2-num1;
// if (num1>num2){
//     difference = num1 - num2;
// } else {
//     difference = num2 - num1;
// }
console.log('두수의 차이는', difference);

// if (num1 > num2){
//     msg = '첫번째 수가 ' + difference + '만큼 더 크다';
// } else if (num2 > num1){
//     msg = '두번째 수가 ' + difference + '만큼 더 크다';
// } else{
//     msg = "두 수는 같다"
// }
msg = (num1>num2) ? '첫번째 수가 ' + (num1-num2) + '만큼 더 크다' : (num2 > num1) ? '두번째 수가 ' + (num2-num1) + '만큼 더 크다' : "두 수는 같다"
console.log(msg);