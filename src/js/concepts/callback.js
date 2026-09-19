/**
 * Callback functions:
 * Are functions passed into other functions as arguments.
 * The function that it is passed to can call this passed in function at its own time.
 *
 */

// Below we pass in an anonymous function to the setTimeout function, that it calls after 1000ms thus making the anonymous a callback function.
setTimeout(function () {
  console.log("I am a message from the setTimeout Callback function");
}, 1000);

function x(y) {
  console.log("This is a message from function x");
  y();
}

x(function y() {
  console.log(
    "This is a message from a callback function y passed in as an [ARG]",
  );
});
