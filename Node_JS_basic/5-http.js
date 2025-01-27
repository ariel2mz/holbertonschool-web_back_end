#!/usr/bin/env node

const http = require('http');
const fs = require('fs');
const path = require('path');

function countStudents(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        return reject(new Error('Cannot load the database'));
      }

      const lines = data.trim().split('\n').filter(Boolean);
      if (lines.length <= 1) {
        return reject(new Error('Cannot load the database'));
      }

      const fields = lines.slice(1).reduce((acc, line) => {
        const [firstname, , , field] = line.split(',');
        if (!acc[field]) {
          acc[field] = [];
        }
        acc[field].push(firstname);
        return acc; // Ensure the accumulator is returned
      }, {});

      const totalStudents = Object.values(fields).flat().length;
      const report = [`Number of students: ${totalStudents}`];

      for (const [field, names] of Object.entries(fields)) {
        report.push(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
      }

      resolve(report.join('\n'));
    });
  });
}

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    const databaseFile = process.argv[2];
    if (!databaseFile) {
      res.end('This is the list of our students\nCannot load the database');
      return;
    }

    try {
      const report = await countStudents(path.resolve(databaseFile));
      res.end(`This is the list of our students\n${report}`);
    } catch (error) {
      res.end(`This is the list of our students\n${error.message}`);
    }
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(1245, () => {
  console.log('Server running on port 1245');
});

module.exports = app;
