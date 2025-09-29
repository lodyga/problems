class DetectSquares {
   /**
    * Time complexity: 
    *     add: O(1)
    *     count: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: hash map
    * @param {}
    * @return {}
    */
   constructor() {
      this.points = new Map();  // {(x, y): counter}
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
      let square_counter = 0;

      for (const point of this.points.keys()) {
         const [x, y] = point.split(',').map((value) => Number(value));
         if (
               x !== nx 
            && y !== ny 
            && Math.abs(x - nx) === Math.abs(y - ny)
            && this.points.has(`${x},${ny}`) 
            && this.points.has(`${nx},${y}`)
         )
            square_counter += (
               this.points.get(`${x},${y}`)
               * this.points.get(`${x},${ny}`)
               * this.points.get(`${nx},${y}`)
            );
      }
      return square_counter
   };
}


const detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
console.log(detectSquares.count([11, 10])); // return 1. You can choose:
//   - The first, second, and third points
console.log(detectSquares.count([14, 8]));  // return 0. The query point cannot form a square with any points in the data structure.
detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
console.log(detectSquares.count([11, 10])); // return 2. You can choose:
//   - The first, second, and third points
//   - The first, third, and fourth points