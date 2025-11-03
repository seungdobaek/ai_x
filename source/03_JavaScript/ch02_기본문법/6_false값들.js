//false로 해석되는 값 : 0, '', NaN, null, undefined
var i;
console.log(Boolean(i));
console.log(Boolean(0));
console.log(Boolean(NaN));
console.log(Boolean(Number("a")));
console.log(Boolean(''));
console.log(Boolean(null));
console.log();
console.log("0==false의결과 :", 0==false);
console.log("0===false의결과 :", 0===false);