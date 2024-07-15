var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().trim().split("\n")
var res = 0;
var N = parseInt(input[0])
var M = parseInt(input[1])

res = (N-1)*(M-1)*2
if (res < 0) res = 0
console.log(res)