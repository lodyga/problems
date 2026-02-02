class Solution {
   /**
    * Time complexity: O(V*E)
    * Auxiliary space complexity: O(V*E)
    * Tags:
    *     DS: hash map, list
    *     A: backtracking, sorting
    *     Model: graph
    * @param {string[][]} tickets
    * @return {string[]}
    */
   findItinerary(tickets) {
      tickets.sort();
      const nextCities = new Map();

      for (const [src, dst] of tickets) {
         if (!nextCities.has(src))
            nextCities.set(src, []);
         nextCities.get(src).push(dst)
      }

      const flightPath = ['JFK'];

      const backtrack = (city) => {
         if (flightPath.length === tickets.length + 1) {
            return true
         } else if (nextCities.get(city).length === 0) {
            return false
         }

         const nextCitiesCopy = nextCities.get(city).slice();
         for (let index = 0; index < nextCitiesCopy.length; index++) {
            const adjCity = nextCitiesCopy[index];
            nextCities.get(city).splice(index, 1);
            flightPath.push(adjCity);

            if (backtrack(adjCity))
               return true

            flightPath.pop();
            nextCities.get(city).splice(index, 0, adjCity);
         }
         return false
      }

      backtrack('JFK');
      return flightPath
   };

   /**
    * Time complexity: O(ElogE)
    * Auxiliary space complexity: O(E)
    * Tags:
    *     DS: hash map, list
    *     A: post-order dfs on edges, Hierholzer
    *     Model: graph
    * @param {string[][]} tickets
    * @return {string[]}
    */
   findItinerary(tickets) {
      // Sort only by destination.
      tickets.sort((a, b) => b[1].localeCompare(a[1]));
      const nextCities = new Map();

      for (const [src, dst] of tickets) {
         if (!nextCities.has(src))
            nextCities.set(src, []);
         nextCities.get(src).push(dst)
      }

      const flightPath = [];

      const dfs = (city) => {
         while (nextCities.get(city)?.length > 0) {
            const nextCity = nextCities.get(city).pop();
            dfs(nextCity);
         }

         flightPath.push(city);
      };

      dfs("JFK")
      flightPath.reverse()
      return flightPath
   };
}


const findItinerary = new Solution().findItinerary;
console.log(new Solution().findItinerary([['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']]).toString() === ['JFK', 'MUC', 'LHR', 'SFO', 'SJC'].toString())
console.log(new Solution().findItinerary([['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]).toString() === ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO'].toString())
console.log(new Solution().findItinerary([['JFK', 'SFO'], ['SFO', 'JFK'], ['JFK', 'ATL'], ['Y2K', 'ATL'], ['ATL', 'Y2K']]).toString() === ['JFK', 'SFO', 'JFK', 'ATL', 'Y2K', 'ATL'].toString())
console.log(new Solution().findItinerary([['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'JFK'], ['ATL', 'AAA'], ['AAA', 'ATL'], ['ATL', 'BBB'], ['BBB', 'ATL'], ['ATL', 'CCC'], ['CCC', 'ATL'], ['ATL', 'DDD'], ['DDD', 'ATL'], ['ATL', 'EEE'], ['EEE', 'ATL'], ['ATL', 'FFF'], ['FFF', 'ATL'], ['ATL', 'GGG'], ['GGG', 'ATL'], ['ATL', 'HHH'], ['HHH', 'ATL'], ['ATL', 'III'], ['III', 'ATL'], ['ATL', 'JJJ'], ['JJJ', 'ATL'], ['ATL', 'KKK'], ['KKK', 'ATL'], ['ATL', 'LLL'], ['LLL', 'ATL'], ['ATL', 'MMM'], ['MMM', 'ATL'], ['ATL', 'NNN'], ['NNN', 'ATL']]).toString() === ['JFK', 'SFO', 'JFK', 'ATL', 'AAA', 'ATL', 'BBB', 'ATL', 'CCC', 'ATL', 'DDD', 'ATL', 'EEE', 'ATL', 'FFF', 'ATL', 'GGG', 'ATL', 'HHH', 'ATL', 'III', 'ATL', 'JJJ', 'ATL', 'KKK', 'ATL', 'LLL', 'ATL', 'MMM', 'ATL', 'NNN', 'ATL'].toString())
