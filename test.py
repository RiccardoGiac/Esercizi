def reverse(x: int) -> int:
        sxs: str = str(x)
        sx : list = list(sxs)
        if sx[0] == "-":
            sx.remove(sx[0])
        for n in sx:
            sx.append(sx.pop(0))
        
        sx = str(sx)
        print(sx)
        
        if x < 0:
            sx = int(sx)
            sx = -(sx)
            return sx
        else:
            return int(sx)
        
print(reverse(-2))