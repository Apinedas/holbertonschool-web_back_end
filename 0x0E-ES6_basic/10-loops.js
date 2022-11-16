export default function appendToEachArrayValue(array, appendString) {
  const new_array = [];
  for (let item of array) {
    new_array.push(appendString + item);
  }
  return new_array;
}
