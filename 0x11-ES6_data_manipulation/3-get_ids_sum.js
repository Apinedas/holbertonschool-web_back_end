export default function getStudentIdsSum(studentsArray) {
  const initialSum = 0;
  return studentsArray.reduce(
    (sumIds, currentStudent) => sumIds + currentStudent.id,
    initialSum,
  );
}
