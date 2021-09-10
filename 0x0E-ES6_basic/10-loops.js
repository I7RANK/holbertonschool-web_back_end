export default function appendToEachArrayValue(array, appendString) {
  let new_arr = []

  for (const idx of array) {
    new_arr.push(appendString + idx);
  }

  return new_arr;
}
