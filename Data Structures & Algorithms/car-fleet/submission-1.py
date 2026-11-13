class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = sorted(dict(zip(position,speed)).items())
        s = set()
        unique = 0
        last_car_time = 0
        for c in reversed(d):
            time = (target-c[0])/c[1]
            if time < last_car_time:
                continue
            else:
                s.add(time)
            last_car_time = time

        return len(s)