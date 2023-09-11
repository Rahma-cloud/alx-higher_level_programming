#!/usr/bin/node
const argv = process.argv;

function add (a, b) {
  if (isNaN(a || b)) {
    console.log('NaN');
  }
  console.log(a + b);
}
add(argv[2], argv[3]);
