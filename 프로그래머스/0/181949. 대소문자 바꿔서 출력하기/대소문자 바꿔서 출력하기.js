// readline모듈 불러오기
// rl을 통해 표준 입출력 인터페이스
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// 입력값 받는 빈배열
let input = [];

// 이벤트리스너 line은 입력 후 Enter키를 통해 발생
rl.on('line', function (line) {
    input = [line];
    // 이벤트리스너 close rl.close() 호출 시 발생
}).on('close',function(){
    // str은 input의 첫요소
    // ans는 답을 저장
    str = input[0];
    let ans = ''
//     str의 길이만큼 반복
    for (let i = 0; i < str.length; i++) {
        let temp = str.charAt(i)
        if (temp === temp.toUpperCase()) {
            ans += temp.toLowerCase()
        } else {
            ans += temp.toUpperCase()
        }
    }
    console.log(ans)
});

