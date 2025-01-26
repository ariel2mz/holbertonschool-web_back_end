#!/usr/bin/node

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Welcome to Holberton School, what is your name?\n', (name) => {
  process.stdout.write('Your name is: ' + name + '\r'); // Ensure carriage return
  rl.close();
});

rl.on('close', () => {
  process.stdout.write('\nThis important software is now closing\n'); // Ensure carriage return
});
