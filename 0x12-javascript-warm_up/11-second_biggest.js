#!/usr/bin/node
const len = process.argv.length;
if (len <= 3) {
  console.log(0);
} else {
  const sorted = process.argv.slice(2).sort((a, b) => a - b);
  console.log(sorted[len - 4]);
}
