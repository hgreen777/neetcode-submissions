class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort cars into the order they are, they cannot overtake.
        d = sorted(dict(zip(position,speed)).items())
        s = set()
        # Keep track of last fleet time to see if the car should be in the fleet or new one.
        last_car_time = 0
        # Start with closest car and work out time till target.
        for c in reversed(d):
            time = (target-c[0])/c[1]
            if time < last_car_time:
                # If quicker then the car infront it will only catch up.
                # Therefore not a unique fleet.
                continue
            else:
                s.add(time)
            last_car_time = time

        return len(s)