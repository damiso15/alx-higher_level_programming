#!/usr/bin/node

const fs = require('fs');

const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

const file1Contents = fs.readFileSync(sourceFile1, 'utf8');
const file2Contents = fs.readFileSync(sourceFile2, 'utf8');
const concatenatedContents = `${file1Contents}${file2Contents}`;

fs.writeFileSync(destinationFile, concatenatedContents);
