class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        r=[False]*len(rooms)

        def dfs(l):
            if r[l]==True:
                return
            r[l]=True
            for i in rooms[l]:
                dfs(i)
        dfs(0)
        for i in r:
            if i==False:
                return False
        return True
            

        