function outer() {
  var count = 0; // has block scope within {}

  function inner() {
    count++;
    console.log(count);
  }

  // Has a reference to var b due to hoisting
  function inner2() {
    console.log(b);
    console.log(c);
  }

  var b = 111111;
  // using a let/const will also work. Why? Because before the inner2() is executed the assignment to 'c' has happened in memory. (exists in scope)
  let c = 222222;
  //count++;

  return [inner, inner2];
}

const functions = outer();
/**@abstract
 * InnerFuntion console.logs 1 because functions always remember their lexical scope, in other words CLOSURE
 */
functions[0]();
functions[1]();
