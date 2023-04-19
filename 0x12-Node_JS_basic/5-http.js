const http = require('http');
const fs = require('fs');

const hostname = '127.0.0.1';
const port = 1245;

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  if (req.url === '/') {
    res.write('Hello Holberton School!');
  }
  if (req.url === '/students') {
    res.write('This is the list of our students\n');
    try {
      const data = fs.readFileSync(process.argv[2], 'utf8');
      const linesArray = data.split('\n');
      let numberOfStudents = 0;
      const studentsByField = {};
      linesArray.shift();
      for (const line of linesArray) {
        const splittedLine = line.split(',');
        if (splittedLine.length === 4) {
          numberOfStudents += 1;
          if (splittedLine[3] in studentsByField) {
            studentsByField[splittedLine[3]].push(splittedLine[0]);
          } else {
            studentsByField[splittedLine[3]] = [splittedLine[0]];
          }
        }
      }
      res.write(`Number of students: ${numberOfStudents}\n`);
      let strStudents = '';
      // eslint-disable-next-line guard-for-in
      for (const field in studentsByField) {
        let strList = '';
        for (const student of studentsByField[field]) {
          if (strList.length > 0) {
            strList += ', ';
          }
          strList += student;
        }
        strStudents += `Number of students in ${field}: ${studentsByField[field].length}. List: ${strList}\n`;
      }
      res.write(strStudents.slice(0, -1));
    } catch (err) {
      res.write('Cannot load the database');
    }
  }
  res.end();
});

app.listen(port, hostname);

module.exports = app;
