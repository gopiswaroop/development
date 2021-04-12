var hot=false
var temp=31
if (temp>80) {
   console.log("hot outside");
}else if (temp <= 80 && temp >= 50){
    console.log("avg hot today")
}else if (temp < 50 && temp >= 32){
    console.log("cold out")
}else{
    console.log("very cold")
}
