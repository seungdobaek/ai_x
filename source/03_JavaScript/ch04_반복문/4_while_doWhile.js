// 1초동안 반복하는 while 구문 / do~while 구문
var cnt = 0; // 반복횟수
var endTime = new Date().getTime() + 1000;
// while(new Date().getTime() <= endTime){
//     cnt++; // cnt 1 증가
// }
do{
    cnt++;
} while(new Date().getTime() <= endTime)
console.log('1초 동안 while문 수행한 횟수 :', cnt);