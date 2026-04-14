class Solution:
    def minimumTotalDistance(
        self,
        robot: List[int],
        factory: List[List[int]]
    ) -> int:

        robot.sort()
        factory.sort()
        INF = int(10**14)

        @cache
        def go(r, f, used):
            if r == len(robot):
                return 0

            if f == len(factory):
                return INF

            opts = [go(r, f + 1, 0)]

            if factory[f][1] > used:
                opts.append(
                    go(r + 1, f, used + 1) +
                    abs(robot[r] - factory[f][0])
                )

            return min(opts)

        return go(0, 0, 0)
        