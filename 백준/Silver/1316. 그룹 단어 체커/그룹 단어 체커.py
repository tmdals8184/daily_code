n = int(input())
count = 0
for _ in range(n):
    word = input() # aabbca
    list_uniq = list(set(word)) # c a b
    is_uniq = True
    for idx, uniq in enumerate(list_uniq):
        uniq_idxs = [i for i, w in enumerate(word) if w == uniq] # 0 1 
        # [0 + 1, 1 + 1, 2 + 1] == [1, 2, 3]
        comp_list1 = [v + 1 for v in uniq_idxs[:-1]]
        comp_list2 = uniq_idxs[1:]
        if comp_list1 != comp_list2:
            # 다르면 이 글자는 불연속적임 -> 조건 미충족            
            is_uniq = False
            break
    if is_uniq:
        count += 1
print(count)
            
    
    
    
    
    # 체크리스트: []
    # idx = 0
    # 현재글자(피벗): word[idx]
    # 다음글자: a <- 피벗 a와 같음
    #     다음으로 넘어가기
    # 다음글자: b <- 피벗 a와 다름
    #     체크리스트에 있는지(b가 나왔던적이 있는지) <- 없었음
    #     체크리스트: [a, b]
    #     현재 글자(피벗) :b
    #     다음글자: b <- 피벗 b와 같음
    #         다음으로 넘어가기
    #     다음글자: a <- 피벗 b와 다름
    #         체크리스트에 있는지(a가 나왔던적이 있는지) <- 있었음
    #         for문 중단, idx반환
    #