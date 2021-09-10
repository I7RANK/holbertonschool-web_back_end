export default function iterateThroughObject(reportWithIterator) {
  let new_str = "";
  let control = true;

  for (const employee of reportWithIterator) {
    if (control) {
      new_str += employee;
      control = false;
    }
    else {
      new_str += ` | ${employee}`;
    }
  }

  return new_str;
}
