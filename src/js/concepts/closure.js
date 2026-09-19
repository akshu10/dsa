function outer() {
  var count = 0; // has block scope within {}

  function inner() {
    count++;
    console.log(count);
  }

  //count++;

  return inner;
}

const innerFunction = outer();
/**@abstract
 * InnerFuntion console.logs 1 because functions always remember their lexical scope, in other words CLOSURE
 */
innerFunction();
