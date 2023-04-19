const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
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
    console.log(`Number of students: ${numberOfStudents}`);
    // eslint-disable-next-line guard-for-in
    for (const field in studentsByField) {
      let strList = '';
      for (const student of studentsByField[field]) {
        if (strList.length > 0) {
          strList += ', ';
        }
        strList += student;
      }
      console.log(`Number of students in ${field}: ${studentsByField[field].length}. List: ${strList}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
