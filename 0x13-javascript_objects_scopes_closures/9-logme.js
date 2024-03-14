#!/usr/bin/node

let init = 0;

exports.logMe = function(item) {
  console.log(`${init}: ${item}`);
  init++;
}
