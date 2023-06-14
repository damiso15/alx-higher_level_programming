#!/usr/bin/node

const { dict } = require('./101-data');

const sortedDict = {};

for (const [userId, occurrences] of Object.entries(dict)) {
  if (sortedDict[occurrences]) {
    sortedDict[occurrences].push(userId);
  } else {
    sortedDict[occurrences] = [userId];
  }
}

console.log(sortedDict);
