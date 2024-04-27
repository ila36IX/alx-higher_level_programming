#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

const url = argv[2];

request(url, function (err, r, body) {
  const comTodoCount = {};

  if (!err && r.statusCode === 200) {
    const todos = JSON.parse(body);

    const compTodos = todos.filter(todo => todo.completed);
    compTodos.forEach(t => {
      comTodoCount[t.userId]
        ? comTodoCount[t.userId]++
        : comTodoCount[t.userId] = 1;
    });

    console.log(comTodoCount);
  }
});
