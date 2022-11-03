// Sort Array by Increasing Frequency
const frequencySort = (nums) => {
    const freq = {};
    for (const num of nums) {
      freq[num] = (freq[num] || 0) + 1;
    }
    return nums.sort((a, b) => freq[a] === freq[b] ? b - a : freq[a] - freq[b]);
  };