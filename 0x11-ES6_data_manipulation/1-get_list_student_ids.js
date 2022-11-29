export default function getListStudentIds(studentsArray) {
  if (Array.isArray(studentsArray)) {
    return studentsArray.map((student) => student.id);
  }
  return [];
}
