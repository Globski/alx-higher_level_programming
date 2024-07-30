#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const taskCount = {};
    data.forEach((task) => {
      if (task.completed) {
        if (taskCount[task.userId]) {
          taskCount[task.userId] += 1;
        } else {
          taskCount[task.userId] = 1;
        }
      }
    });
    console.log(taskCount);
  }
});
