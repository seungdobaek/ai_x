function sumAll(){
    let sum = 0;
    if (arguments.length==0){
        sum = -999;
    } else {
        for (let data of arguments){
            sum += data;
        }
    }
    return sum;
}