#!/usr/bin/node

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Welcome to Holberton School, what is your name?\n', (name) => {
  process.stdout.write('Your name is: ' + name + '\n'); // Fix: Ensure newline
  rl.close();
});

rl.on('close', () => {
  process.stdout.write('This important software is now closing\n'); // Fix: Ensure newline
});
