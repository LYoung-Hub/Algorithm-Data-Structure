from collections import deque


class SnakeGame(object):

    class Position(object):

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def isEqual(self, p):
            return self.x == p.x and self.y == p.y

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.rows = height
        self.cols = width
        self.food = food

        initial = self.Position(0, 0)
        self.snake = deque([initial])
        self.length = 0

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        curr = self.Position(self.snake[0].x, self.snake[0].y)

        if direction == 'U':
            curr.x -= 1
        if direction == 'D':
            curr.x += 1
        if direction == 'L':
            curr.y -= 1
        if direction == 'R':
            curr.y += 1

        if curr.x >= self.rows or curr.x < 0 or curr.y >= self.cols or curr.y < 0:
            return -1

        for i in range(1, len(self.snake) - 1):
            if self.snake[i].isEqual(curr):
                return -1

        self.snake.appendleft(curr)

        if self.length < len(self.food):
            p = self.Position(self.food[self.length][0], self.food[self.length][1])
            if p.isEqual(curr):
                self.length += 1

        while len(self.snake) > self.length + 1:
            self.snake.pop()

        return self.length

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)


if __name__ == '__main__':
    obj = SnakeGame(3,2,[[1,2],[0,1]])
    obj.move('R')
    obj.move('D')
    obj.move('R')
