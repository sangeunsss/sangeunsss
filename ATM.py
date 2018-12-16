def main():
   n = int(input()); # 사람 수 입력
   t = 0; # 총 소요시간
   p = list(map(int, input().split())); # 각 사람 당 소요시간 입력
   p.sort(); # 빨리 끝날 수 있는 사람 앞으로 정렬 (오름차순 정렬)
   for i in range(n): # 사람 수 만큼 반복
      t += p[i] * (n-i); # 해당 사람의 시간을 기다리는 사람 수 만큼 곱해서 계산
   print(t); # 총 소요시간 출력

main(); # 프로그램 실행