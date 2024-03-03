def main():
    N, X = map(int, input().split())
    
    ans = -1
    alcohol = 0
    for i, _ in enumerate(range(N)):
        v, p = map(int, input().split())
        alcohol += v * (p / 100)
        
        if ans != -1:
            continue
        
        if  alcohol > X:
            ans = i + 1
        
    print(ans)
    
    
if __name__ == '__main__':
    main()