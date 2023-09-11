#!/usr/bin/node
const argv = process.argv;

if (argv.length === 3) {
  console.log(argv[2] + 'is' + argv[3]);
} else if (argv.length <= 2) {
  console.log('c is undefined');
} else {
  console.log('undefined is undefined');
}
