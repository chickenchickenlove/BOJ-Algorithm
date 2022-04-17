"""
고객수 : 25명
카페수 : 6,000개

우선순위 : 고객별로 달라짐
1. 고객 + 친구의 주문횟수 : 이 값은 바뀐다.
2. 거리 : 고정
3. cafe ID : 고정

2,3번은 바뀌지 않음.

우선순위
1. RECOMMEND 시에 올 때 마다, 검색
2. 우선순위 큐로 관리해주는 방법이 존재함.

출제자 의도를 생각해보자.
recommand() 10,000회다. -->많은 횟수다. 좀 더 효율적으로 처리해야한다는 의도가 판단된다.
1. recommend()시에 검색
2. heapq로 관리
-> recommnd : O(10 * log6,000)
-> Lazy 업데이트를 생각한 경우 불필요한 노드가 더 많아질 수 있음. --> 그래서 log쪽 노드는 크게 문제가 없다고 볼 수 있다.
-> 그런데 유효ㅕ하지 않은 값들이 계속 들어가 있을 수 있으니 10이 아니라 더 많이 할 수도 있다.
-> 내 친구와 나의 우선순위가 모두 바뀐다. order : push 횟수 = 친구수 + 1 (본인) 만큼 push를 한다.

update
 order : push 횟수 = 1 + 친구수
 beBuddy : push 횟수 = 두명의 주문 카페한 적 있는 카페 개수


1. recommend() 시에, 검색하면..
nlargest를 하면 된다.
nlargetst : 0 (카페수 + 10log(카페수))


heapq로 관리
update
 order : push 횟수 = 1 + 친구수
 beBuddy : push 횟수 = 두 명의 주문한 적 있는 카페 개수
 reconmend : O (10 * log 6,000)


우선순위를 하나의 정수값으로 합쳐서 관리하는 편도 있다.
*10 뭐 이런 식으로 처리 하면 될 듯.


께산기..

카페 총 10000개 등록 가능. 이름은 5자. ->
베스트 스코어 총 150000번 요청한다.





"""