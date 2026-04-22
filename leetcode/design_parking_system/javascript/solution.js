/**
 * Time complexity: O(1)
 * Auxiliary space complexity: O(1)
 * Tags:
 *     DS: array
 *     A: iteration
 */
class ParkingSystem {
   constructor(big, medium, small) {
      this.parkingSlot = [big, medium, small];
   };

   addCar(carType) {
      if (this.parkingSlot[carType - 1] === 0) {
         return false
      } else {
         this.parkingSlot[carType - 1] -= 1;
         return true
      }
   };
};


const parkingSystem = new ParkingSystem(1, 1, 0);
console.log(parkingSystem.addCar(1) === true)
console.log(parkingSystem.addCar(2) === true)
console.log(parkingSystem.addCar(3) === false)
console.log(parkingSystem.addCar(1) === false)
