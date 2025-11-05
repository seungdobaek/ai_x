//dateGetNumberOfDays.js
// now.getNumberOfDays(openday) => now는 this / openday는 that
Date.prototype.getNumberOfDays = function(that){
    let intervalMillisec = Math.abs(this.getTime() -that.getTime());
    let day = Math.floor(intervalMillisec/(1000*60*60*24)); //내림
    return day;
};
// let now = new Date();
// let limitday = new Date(2026,1,12,28,0,0);
// console.log(now.getNumberOfDays(limitday));
// console.log(limitday.getNumberOfDays(now));
// console.log(now.getNumberOfDays(now));