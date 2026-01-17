/**
 * Time complexity: 
 *     add: O(1)
 *     count: O(n)
 * Auxiliary space complexity: O(n)
 * Tags:
 *     DS: hash map
 *     A: iteration
 */
class DetectSquares {
   constructor() {
      // {(x, y): counter}
      this.points = new Map();
   };
   /**
    * @param {number[]} point 
    * @returns {number}
    */
   add(point) {
      const [x, y] = point;
      this.points.set(`${x},${y}`, (this.points.get(`${x},${y}`) || 0) + 1);
   };

   /**
    * @param {number[]} point 
    * @returns {number}
    */
   count(newPoint) {
      const [nx, ny] = newPoint;
      let counter = 0;

      for (const point of this.points.keys()) {
         const [x, y] = point.split(',').map((value) => Number(value));
         if (
            x !== nx &&
            y !== ny &&
            Math.abs(x - nx) === Math.abs(y - ny) &&
            this.points.has(`${x},${ny}`) &&
            this.points.has(`${nx},${y}`)
         )
            counter += (
               this.points.get(`${x},${y}`) *
               this.points.get(`${nx},${y}`) *
               this.points.get(`${x},${ny}`)
            );
      }
      return counter
   };
}


const detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
console.log(detectSquares.count([11, 10]) === 1);
console.log(detectSquares.count([14, 8]) === 0);
detectSquares.add([11, 2]);
console.log(detectSquares.count([11, 10]) === 2);
