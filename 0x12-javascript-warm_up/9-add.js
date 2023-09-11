#!/usr/bin/node
const argv = process.argv;

function add (a, b) {
  if (a && b) {
    console.log(a + b);
  } else {
    console.log('NaN');
  }
}
add(argv[2], argv[3]);
