# [Silver I] 곱셈 - 1629 

[문제 링크](https://www.acmicpc.net/problem/1629) 

### 성능 요약

메모리: 108080 KB, 시간: 116 ms

### 분류

분할 정복을 이용한 거듭제곱, 수학

### 제출 일자

2024년 6월 9일 23:04:36

### 문제 설명

<p>자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.</p>

### 출력 

 <p>첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.</p>



### 시간 초과 코드
```
 while B:
     if B % 2:
         res *= A
     A *= A
     B //= 2
```

```
 while B:
     if B & 1:
         res *= A
     A *= A
     B = B >> 1
```

### A = A%C 연산을 통해 시간을 대폭 줄일 수 있다.
### mod 연산의 거듭제곱 -> a, b가 p로 나눈 나머지가 서로 동일하다면, a^k, b^k를 p로 나눈 나머지도 서로 동일하다.
