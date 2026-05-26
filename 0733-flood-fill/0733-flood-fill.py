class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        starting_pixel = image[sr][sc]

        self.dfs(image, sr, sc, newColor, starting_pixel)

        return image


    def dfs(self, image, sr, sc, newColor, starting_pixel):

        if sr < 0 or sr > len(image)-1 or sc < 0 or sc > len(image[0])-1 or image[sr][sc] == newColor or image[sr][sc] != starting_pixel:
            return

        image[sr][sc] = newColor

        self.dfs(image, sr+1, sc, newColor, starting_pixel)
        self.dfs(image, sr-1, sc, newColor, starting_pixel)
        self.dfs(image, sr, sc+1, newColor, starting_pixel)
        self.dfs(image, sr, sc-1, newColor, starting_pixel)