var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().trim().split(" ")
var res = 0;
var top_16 = parseInt(input[0]);

for(let i = 1; i <= 4; i++){
  var tmp = parseInt(input[i]);
  if(top_16 - tmp <= 1000) res += 1;
  else break;
}

console.log(res)