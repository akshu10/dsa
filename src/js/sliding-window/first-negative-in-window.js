/**
 *
 * @param {*} n - array of numbers
 * @param {*} k - window size
 *
 * --- SOLUTIONING ---
 * What state am I keeping? "indices of negatives, oldest first"
 * What are my phases? Almost every sliding window is: build first window → record answer → slide loop.
 * What happens on one slide step? Usually three things in order: something leaves, something enters, record the answer.
 */

/**
 * ([12, -1, -7, 8, -15, 30, 16, 28], 3) → [-1, -1, -7, -15, -15, 0]
 */
function firstNegativeInWindow(n, k) {
  const indices = [];
  const result = [];
  let head = 0; // front of `negatives`; entries before this are expired

  // build first window, we have already looked over 0 -> k - 1 elements
  for (let i = 0; i < k; i++) {
    if (n[i] < 0) indices.push(i);
  }

  // record the answer for window 0:
  // is there a live entry? (is head still within negatives?)
  //   yes -> push the VALUE at that index
  //   no  -> push 0

  result = n[indices[0]];
  head++;

  // Phase 2 — slide, one new element at a time

  for (let j = k; j < n.lenth; j++) {
    if (n[j] < 0) {
      indices.push(j);
    }
  }
}
