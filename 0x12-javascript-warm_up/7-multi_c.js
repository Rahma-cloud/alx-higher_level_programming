#!/usr/bin/node
const argv = process.argv;

if (!isNaN(argv[2])) {
  for (let i = 0; i < argv[2]; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
