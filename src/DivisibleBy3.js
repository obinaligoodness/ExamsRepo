function divisibleByThree(){
    let sum =0;
    for(let i =1; i<=30; i++){
        if(i%3==0){
            sum += i;
        }
    }
    console.log(sum)
}
console.log(divisibleByThree())