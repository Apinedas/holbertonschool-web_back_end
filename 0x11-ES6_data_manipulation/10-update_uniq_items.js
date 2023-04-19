export default function updateUniqueItems(toChangeMap) {
  if (toChangeMap instanceof Map) {
    for (const dataMap of toChangeMap) {
      if (dataMap[1] === 1) {
        toChangeMap.set(dataMap[0], 100);
      }
    }
    return toChangeMap;
  }
  throw new Error('Cannot process');
}
