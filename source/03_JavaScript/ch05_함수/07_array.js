/* array 함수 : 가변인자함수 (파이썬 튜플매개변수로 구현)
* 매개변수가 0개 : length가 0ㅇ인 배열 return
* 매개변수가 1개 : length가 매개변수만큼의 크기인 매열 return
* 매개변수가 2개 이상 : 매개변수로 배열을 생성 return
*/
function array(){ // arguments(매개변수 배열) : 매개변수의 내용
    let result = []
    if(arguments.length==1){
        //result를 arguments[0]만큼의 크기인 배열로 : result의 length를 arugments[0]으로 변경
        // for (let i=0; i<arguments[0]; i++){
        //     result.push();
        // }
        result.length = arguments[0];
    } else if(arguments.length >= 2){
        // result를 arguments 내용의 배열로 : result.push(arguments[0~끝까지])
        for (let i of arguments){
            result.push(i);
        }

    }
    return result;
}

console.log(array(1, '이', 3, '사', '아무거나'));
console.log(array(3));
console.log(array());
console.log(array(3, 5));