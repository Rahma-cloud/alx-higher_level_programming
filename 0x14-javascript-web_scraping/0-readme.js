#!/usr/bin/node
const fs = require('fs');

fs.readFile('/Users/Rahmah/ALX/alx-higher_level_programming/0x14-javascript-web_scraping/cisfun', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
