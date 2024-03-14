#!/usr/bin/node

const fs = require('fs');
const { argv } = require('node:process');

// fs.readFile(argv[2], (err, f) => {
//   if (err) throw err;
//   file1 = f.toString();
// });
//
// fs.readFile(argv[3], (err, f) => {
//   if (err) throw err;
//   file2 = f.toString();
// });
//
// setTimeout(() => {
//   fs.writeFile(argv[4], file1 + file2, (err) => {
//     if (err) throw err;
//   })
// }, 100);

const file1 = fs.readFileSync(argv[2]);
const file2 = fs.readFileSync(argv[3]);
fs.writeFile(argv[4], file1 + file2, (err) => {
  if (err) throw err;
});
