#!/usr/bin/node
exports.converter = function (base) {
  return function (me) {
    return me.toString(base);
  };
};
