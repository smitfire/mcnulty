function plus_three(n){
  return n+3
}
function divide_three(n){
  return n/3
}

function lessThanFour(n){
  return n >=4
}

data = [1,2,3,4,5,6]
filtered = data.filter(lessThanFour)
console.log(filtered)
console.log(plus_three(3))
console.log(divide_three(3))
