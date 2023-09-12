#!/usr/bin/node
let argv = process.argv;
if (!argv[2] || !argv[3]) {
  console.log(0);
} else {
  function compare (a, b) {
    return a - b;
  }
  argv = argv.slice(2);
  argv = argv.sort(compare);
  console.log(argv[argv.length - 2]);
}
