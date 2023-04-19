export default function getListStudents() {
  function createObject(id, firstName, location) {
    return {
      id,
      firstName,
      location,
    };
  }
  const guillaume = createObject(1, 'Guillaume', 'San Francisco');
  const james = createObject(2, 'James', 'Columbia');
  const serena = createObject(5, 'Serena', 'San Francisco');
  const objList = [guillaume, james, serena];
  return objList;
}
