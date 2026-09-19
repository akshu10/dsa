// Shows a code example demonstrating the difference between function-scoped and block-scoped variables in JavaScript.

function demo() {
  if (true) {
    var a = 1; // function-scoped — leaks out of the if-block
    let b = 2; // block-scoped — trapped inside the if-block
  }
  console.log(a); // 1
  console.log(b); // ReferenceError: b is not defined
}

var a = 8;
var a = 9;

console.log(a);

age = 8;

console.log(age);
