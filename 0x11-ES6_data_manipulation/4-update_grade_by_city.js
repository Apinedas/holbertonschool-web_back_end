export default function updateStudentGradeByCity(studentsArray, city, newGrades) {
  const studentsFromCity = studentsArray.filter((student) => student.location === city);
  const newStudentsArray = studentsFromCity.map((student) => {
    const studentCopy = student;
    const newGrade = newGrades.filter((grade) => grade.studentId === student.id);
    if (newGrade[0]) {
      studentCopy.grade = newGrade[0].grade;
    } else {
      studentCopy.grade = 'N/A';
    }
    return studentCopy;
  });
  return newStudentsArray;
}
