/*

Merge Intervals.
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

eg. arr = [[1,3],[2,6],[8,10],[15,18]]

output:- [[1,6], [8,10], [15,18]]

*/

const mergeInterval = (intervals) => {
  intervals.sort((a, b) => {
    return a[0] - b[0];
  });

  let res = [];
  for (let interval of intervals) {
    // let n = res.length - 1;
    if (res.length === 0 || interval[0] > res[res.length - 1][1]) {
      res.push(interval);
    } else {
      res[res.length - 1][1] = Math.max(interval[1], res[res.length - 1][1]);
    }
  }
  return res;
};
