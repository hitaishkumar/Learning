console.log("Running");

//  Exercise 1:
// Write a JavaScript program to check two
// numbers and return true if one of the number
// is 100 or if the sum of the two numbers is
// 100

const program = (a,b) => a === 100 || b === 100 || a == 100 - b

console.log(program(90,180))
console.log(program(90,10))
console.log(program(90,100))
console.log(program(90,80))
console.log(program(90,90))