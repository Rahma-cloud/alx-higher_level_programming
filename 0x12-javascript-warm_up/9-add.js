#!/usr/bin/node
const argv = process.argv;

function add (a, b) {
  console.log(a + b);
}
add(argv[2], argv[3]);
