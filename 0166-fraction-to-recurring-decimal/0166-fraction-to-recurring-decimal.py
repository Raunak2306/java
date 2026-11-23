class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"
        
        res = []
        
        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
        
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Integer part
        res.append(str(numerator // denominator))
        remainder = numerator % denominator
        
        if remainder == 0:
            return "".join(res)
        
        res.append(".")
        
        seen = {}  # remainder -> position in result
        
        while remainder != 0:
            if remainder in seen:
                res.insert(seen[remainder], "(")
                res.append(")")
                break
            
            seen[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator
        
        return "".join(res)

