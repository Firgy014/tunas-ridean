def max_skill_level(N, M, A, B):
    opponents = sorted(zip(A, B), key=lambda x: x[0])
    
    current_skill = M
    total_skill = current_skill

    for skill, boost in opponents:
        if current_skill >= skill:  
            current_skill += boost  
            total_skill = current_skill
    return total_skill

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = max_skill_level(N, M, A, B)


print(result)