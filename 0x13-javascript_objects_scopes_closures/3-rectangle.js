#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (w, h) {
    for (let i = 0; i < w; i++) {
      let temp = '';
      for (let j = 0; j < h; j++) {
        temp = temp + 'X';
      }
      console.log(temp);
    }
  }
};
