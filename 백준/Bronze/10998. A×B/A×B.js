// 입력 받기 (백준 Node.js 기본 템플릿)
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');

// 정수 A, B 파싱
const A = Number(input[0]);
const B = Number(input[1]);

// 결과 출력
console.log(A * B);