var fs = require('fs');
var N = fs.readFileSync('dev/stdin').toString().trim().split("\n");
var a;
var b;

function sol(left, right) {
  var res1 = 1;
  var res2 = 1;
  while(left >= 1){
    res1 = res1 * left;
    res2 = res2 * right;
    left = left - 1;
    right = right - 1;
  }
 
  return Math.round(res2/res1);
} 

for(let i = 1; i <= Number(N[0]); i++){
  let temp = N[i].split(" ")
  a = parseInt(temp[0])
  b = parseInt(temp[1])
  console.log(sol(a, b));
}