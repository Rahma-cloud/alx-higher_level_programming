#!/usr/bin/node
module.exports = exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;i
    }
  }
  console.log(count);
};
