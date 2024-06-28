var fs = require('fs');
var N = fs.readFileSync('dev/stdin').toString().trim();
N = Number(N);
var sol = N.toString(2);
var res = 0;
for(let i in sol){
  if(sol[i] === "1") res += 1;
}
console.log(res)