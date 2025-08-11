# [Silver I] 예쁜 케이크 - 24040 

[문제 링크](https://www.acmicpc.net/problem/24040) 

### 성능 요약

메모리: 32412 KB, 시간: 96 ms

### 분류

수학, 정수론

### 제출 일자

2025년 8월 11일 16:54:04

### 문제 설명

<p><em><strong>Good Bye BOJ, 2021!</strong></em>이 열리는 오늘, 12월 31일은 종서의 생일이다. $N$ 명의 친구들은 종서에게 생일 선물로 예쁜 케이크를 만들어주려 한다.</p>

<p>여기에서, <strong>예쁜 케이크</strong>는 다음과 같은 조건을 만족하는 케이크를 의미한다.</p>

<ol>
	<li>케이크는 높이가 $1$이고, 부피가 $N$인 직육면체 모양이다.</li>
	<li>케이크를 적절히 칼질해서 한 변의 길이가 $1$인 정육면체 모양 조각 $N$ 개로 나눌 수 있어야 한다.</li>
	<li>케이크의 옆면에 가로 너비가 $1$인 직사각형을 이어 붙여 만든 띠를 딱 맞게 두를 수 있어야 한다.</li>
	<li>장식용 띠는 가로 폭이 $1$인 빨간색, 초록색, 하얀색 직사각형이 순서대로 번갈아 가면서 같은 개수만큼 나와야 한다.</li>
</ol>

<p>예를 들어, 아래 그림은 $N = 8$인 경우의 예쁜 케이크 중 하나와 그에 사용된 띠를 나타낸다.</p>

<p style="text-align: center;"><img alt="예쁜 케이크 그림" src="https://upload.acmicpc.net/d4956718-50bc-4fa5-b891-ea89b80bd31a/" style="width: 500px; height: 205px;"></p>

<p style="text-align: center;"><img alt="케이크 띠의 예시" src="https://upload.acmicpc.net/77d7dab9-b619-42b5-8b54-7ef3d67b72dd/" style="margin-top: 12px; margin-bottom: 12px; width: 500px; height: 38px;"></p>

<p>아쉽게도 $N$이 얼마인지에 따라 예쁜 케이크를 만들지 못 할 수도 있다. 종서의 친구들을 위해 부피가 $N$인 예쁜 케이크를 만들 수 있는지 알려주자.</p>

### 입력 

 <p>첫 번째 줄에 전체 테스트 케이스의 개수를 나타내는 정수 $T$가 주어진다.</p>

<p>이후 $T$ 개의 줄에 각각 문제에서 언급한 정수 $N$이 한 줄에 하나씩 주어진다.</p>

### 출력 

 <p>$T$ 개의 줄에 걸쳐 한 줄에 하나씩 문제의 답을 출력해야 한다.</p>

<p>부피가 $N$인 <strong>예쁜 케이크</strong>를 만들 수 있으면 <span style="color:#e74c3c;"><code>TAK</code></span>, 아니면 <span style="color:#e74c3c;"><code>NIE</code></span>를 출력한다.</p>

