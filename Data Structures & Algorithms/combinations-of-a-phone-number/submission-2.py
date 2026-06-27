class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
            
        n=len(str(digits))
        if n==0:
            return []
        print(n)
        dictt={
            '1':(),
            '2':('a','b','c'),
            '3':('d','e','f'),
            '4':('g','h','i'),
            '5':('j','k','l'),
            '6':('m','n','o'),
            '7':('p','q','r','s'),
            '8':('t','u','v'),
            '9':('w','x','y','z')
        }
        res=[]
        sol=[]
        def backtrack(i):
            if i==n:
                res.append("".join(sol[:]))
                return
            for number in list(dictt[digits[i]]):
            
            
                sol.append(str(number))
                backtrack(i+1)
                sol.pop()
        backtrack(0)
        return res


        