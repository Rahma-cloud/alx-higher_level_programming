#!/usr/bin/node
const argv = process.argv;

if (!isNaN(argv[2])) {
  for (let i = 0; i < argv[2]; i++) {
    let temp = '';
    for (let j = 0; j < argv[2]; j++) {
      temp = temp + 'X';
    }
    console.log(temp);
  }
} else {
  console.log('Missing size');
}
