const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      try {
        const lines = data.trim().split('\n').filter((line) => line.trim() !== '');
        if (lines.length <= 1) {
          throw new Error('Cannot load the database');
        }

        const students = lines.slice(1);
        console.log(`Number of students: ${students.length}`);

        const fields = {};
        students.forEach((line) => {
          const [firstname, , , field] = line.split(',');
          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstname);
        });

        Object.entries(fields).forEach(([field, names]) => {
          console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
        });
        resolve();
      } catch (error) {
        reject(new Error('Cannot process the database'));
      }
    });
  });
}

module.exports = countStudents;

