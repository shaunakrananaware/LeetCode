class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        out = set()

        for src, _ in paths:
            out.add(src)
        
        for _, dst in paths:
            if dst not in out: return dst