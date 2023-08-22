'''
두 딱지의 별의 개수가 다르다면, 별이 많은 쪽의 딱지가 이긴다.
별의 개수가 같고 동그라미의 개수가 다르다면, 동그라미가 많은 쪽의 딱지가 이긴다.
별, 동그라미의 개수가 각각 같고 네모의 개수가 다르다면, 네모가 많은 쪽의 딱지가 이긴다.
별, 동그라미, 네모의 개수가 각각 같고 세모의 개수가 다르다면, 세모가 많은 쪽의 딱지가 이긴다.
별, 동그라미, 네모, 세모의 개수가 각각 모두 같다면 무승부이다.
4, 3, 2, 1
'''
'''
첫 번째 줄에는 딱지놀이의 총 라운드 수를 나타내는 자연수 N이 주어진다.

다음 줄에는 A의 그림의 수와 그림의 모양이 있다.

다음 줄에는 B의 그림의 수와 그림의 모양이 있다.

N 라운드의 딱지 정보는 차례대로 총 2N 개의 줄에 주어진다.
'''

T = int(input())
for tc in range(T):
    A_lst = list(map(int, input().split()))
    B_lst = list(map(int, input().split()))
    A_size = A_lst.pop(0)
    A_lst.sort(reverse=True)
    B_size = B_lst.pop(0)
    B_lst.sort(reverse=True)

    if len(A_lst) > len(B_lst):
        for i in range(len(B_lst)):
            if i == len(B_lst) -1:
                if A_lst[i] < B_lst[i]:
                    print('B')
                else:
                    print('A')
                break
            if A_lst[i] < B_lst[i]:
                print('B')
                break
            elif A_lst[i] > B_lst[i]:
                print('A')
                break
            else:
                pass
            
    elif len(A_lst) < len(B_lst):
        for i in range(len(A_lst)):
            if i == len(A_lst) - 1:
                if A_lst[i] > B_lst[i]:
                    print('A')
                else:
                    print('B')
                break
            if A_lst[i] < B_lst[i]:
                print('B')
                break
            elif A_lst[i] > B_lst[i]:
                print('A')
                break
            else:
                pass
    else:
        for i in range(len(A_lst)):
            if i == len(A_lst) - 1:
                if A_lst[i] > B_lst[i]:
                    print('A')
                elif A_lst[i] < B_lst[i]:
                    print('B')
                else:
                    print('D')
                break
            if A_lst[i] < B_lst[i]:
                print('B')
                break
            elif A_lst[i] > B_lst[i]:
                print('A')
                break
            else:
                pass