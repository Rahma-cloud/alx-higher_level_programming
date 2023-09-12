#!/usr/bin/node
let argv = process.argv;
function compare (a, b) {
  return a - b;
}
argv = argv.slice(2);
argv = argv.sort(compare);
console.log(argv[argv.length - 2]);
