class Operation:
    def __init__(self):
        pass
    
    @staticmethod
    def combinations_backtracking(self, target, numbers):
        tables = [[number] for number in numbers]
        new_tables = []
        result = []

        while tables:
            for table in tables:
                s = sum(table)
                for number in numbers:
                    if number >= table[-1]:
                        if s + number < target:
                            new_tables.append(table + [number])
                        elif s + number == target:
                            result.append(table + [number])
            tables = new_tables
            new_tables = []
        return result

    @staticmethod
    def combinationDP_count(self, S, n):
        m = len(S) 
        # bottom up table using the base case 0 value 
        # case (n = 0) 
        table = [[0 for x in range(m)] for x in range(n+1)] 
  
        # Fill the entries for 0 value case (n = 0) 
        for i in range(m): 
            table[0][i] = 1
    
        # Fill table entries in bottom up manner 
        for i in range(1, n+1): 
            for j in range(m):  
                # Count of solutions including S[j] 
                x = table[i - S[j]][j] if i-S[j] >= 0 else 0
                # Count of solutions excluding S[j] 
                y = table[i][j-1] if j >= 1 else 0
  
                # total count 
                table[i][j] = x + y 
        
        return table[n][m-1] 
    