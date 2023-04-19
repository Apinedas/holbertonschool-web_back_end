export default function cleanSet(set, startString) {
  let retString = '';
  if (typeof (startString) === 'undefined' || startString.length === 0) {
    return retString;
  }
  for (const element of set) {
    if (element && element.substring(0, startString.length) === startString) {
      if (retString.length > 0) {
        retString += '-';
      }
      retString += element.substring(startString.length);
    }
  }
  return retString;
}
