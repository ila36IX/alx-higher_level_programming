#!/usr/bin/node

exports.esrever = function (list) {
  const tsil = [];
  for (const el of list) {
    tsil.unshift(el);
  }
  return tsil;
};
