class Solution {
   /**
    * Time complexity: O(E2)
    * Auxiliary space complexity: O(E)
    * Tags: dfs, recursion, graph
    * @param {string[][]} tickets
    * @return {string[]}
    */
   findItinerary(tickets) {
      tickets.sort();
      const adjs = new Map();

      for (const [source, destination] of tickets) {
         if (!adjs.has(source))
            adjs.set(source, []);
         adjs.get(source).push(destination)
      }

      const flightPath = ['JFK'];

      const dfs = (city) => {
         if (flightPath.length === tickets.length + 1)
            return true
         else if (adjs.get(city).length === 0)
            return false

         const prunedAdjs = adjs.get(city).slice();
         for (let index = 0; index < prunedAdjs.length; index++) {
            const adjCity = prunedAdjs[index];
            adjs.get(city).splice(index, 1);
            flightPath.push(adjCity);
            if (dfs(adjCity))
               return true
            flightPath.pop();
            adjs.get(city).splice(index, 0, adjCity);
         }
         return false
      }
      dfs('JFK');
      return flightPath
   };
}


const findItinerary = new Solution().findItinerary;
console.log(new Solution().findItinerary([['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']]), ['JFK', 'MUC', 'LHR', 'SFO', 'SJC'])
console.log(new Solution().findItinerary([['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]), ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO'])
console.log(new Solution().findItinerary([['JFK', 'SFO'], ['SFO', 'JFK'], ['JFK', 'ATL'], ['Y2K', 'ATL'], ['ATL', 'Y2K']]), ['JFK', 'SFO', 'JFK', 'ATL', 'Y2K', 'ATL'])
console.log(new Solution().findItinerary([['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'JFK'], ['ATL', 'AAA'], ['AAA', 'ATL'], ['ATL', 'BBB'], ['BBB', 'ATL'], ['ATL', 'CCC'], ['CCC', 'ATL'], ['ATL', 'DDD'], ['DDD', 'ATL'], ['ATL', 'EEE'], ['EEE', 'ATL'], ['ATL', 'FFF'], ['FFF', 'ATL'], ['ATL', 'GGG'], ['GGG', 'ATL'], ['ATL', 'HHH'], ['HHH', 'ATL'], ['ATL', 'III'], ['III', 'ATL'], ['ATL', 'JJJ'], ['JJJ', 'ATL'], ['ATL', 'KKK'], ['KKK', 'ATL'], ['ATL', 'LLL'], ['LLL', 'ATL'], ['ATL', 'MMM'], ['MMM', 'ATL'], ['ATL', 'NNN'], ['NNN', 'ATL']]), ['JFK', 'SFO', 'JFK', 'ATL', 'AAA', 'ATL', 'BBB', 'ATL', 'CCC', 'ATL', 'DDD', 'ATL', 'EEE', 'ATL', 'FFF', 'ATL', 'GGG', 'ATL', 'HHH', 'ATL', 'III', 'ATL', 'JJJ', 'ATL', 'KKK', 'ATL', 'LLL', 'ATL', 'MMM', 'ATL', 'NNN', 'ATL'])