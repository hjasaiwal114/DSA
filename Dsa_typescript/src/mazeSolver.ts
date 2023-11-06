interface Point {
    x: number;
    y: number;
}

function walk(maze: string[], wall: string, curr: Point, end: Point): boolean {
    // base case
    // off the map or reached the end 
    if (curr.x< 0 || curr.x >= maze[0].length ||
        curr.y < 0 || curr.y >= maze.length ||
        curr.x === end.x && curr.y === end.y ) {
            return curr.x === end.x && curr.y === end.y;
        }
    // check if the current position is a wall or already visited
    if (maze[curr.y][curr.x] === wall) {
        return false;
    }

    maze[curr.y] = maze[curr.y].substring(0, curr.x) + 'V' + maze[curr.y].substring(curr.x + 1);

    const directions = [
        {x: 1, y: 0},
        {x: 0, y: 1},
        {x: -1, y:0},
        {x: 0, y: -1}
    ];

    for (const dir of directions) {
        const next = { x: curr.x + dir.x, y: curr.y + dir.y };
        if (walk(maze, wall, next, end)) {
            return true;
        }
    }

    return false;
}

export default function solve(maze: string[], wall: string, start, start: PointerEvent, end: Point): Point[] {
    const result = walk(maze, wall, start, end);

    return result? [start, end] : [];
}