class Solution:

    def encode(self, strs: List[str]) -> str:
        fs = ""
        lengths = []

        for s in strs:
            lengths.append(str(len(s)))
            fs += s

        fs = ','.join(lengths) + ';' + fs
        return fs

    def decode(self, s: str) -> List[str]:
        if s == ";":
            return []
        sl = []
        # Absorb till ;, split on ','
        splits = s.split(';')
        lens = splits[0].split(',')
        st = ''.join(splits[1:])
        # Absorb till ;, split on ','
        splits = s.split(';')
        lens = splits[0].split(',')
        st = ';'.join(splits[1:])

        cur = 0
        for l in lens:
            l = int(l)
            sl.append(
                st[cur:cur+l]
            )
            cur += l
        return sl

        cur = 0
        for l in lens:
            l = int(l)
            sl.append(
                st[cur:cur+l]
            )
            cur += l
        return sl


