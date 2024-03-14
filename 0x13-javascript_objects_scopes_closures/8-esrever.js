#!/usr/bin/node

exports.esrever = function(list) {
  const tsil = []; 
  for (let el of list) {
    tsil.unshift(el);  
  };
  return tsil;
};
