class Solution {
   /**
    * Time complexity: O(V + E)
    *     V: supplies count + recipes count
    *     E: prequired supplies for a recipe
    * Auxiliary space complexity: O(V + E)
    * Tags:
    *     DS: hash map, hash set, list
    *     A: DFS with memoization (DP on DAG), topological sort with cycle detection
    *     Model: graph
    * @param {string[]} recipes
    * @param {string[][]} ingredientsList
    * @param {string[]} supplies
    * @return {string[]}
    */
   findAllRecipes(recipes, ingredientsList, supplies) {
      const suppliesSet = new Set(supplies);
      const recipeIngredients = new Map(recipes.map((recipe, index) => [recipe, ingredientsList[index]]));
      const badRecipes = new Set();
      const path = new Set();

      const dfs = (product) => {
         if (suppliesSet.has(product)) {
            return true
         } else if (
            !recipeIngredients.has(product) ||
            path.has(product) ||
            badRecipes.has(product)
         ) {
            return false
         }

         path.add(product);

         for (const ingredient of recipeIngredients.get(product)) {
            if (!dfs(ingredient)) {
               path.delete(product)
               badRecipes.add(product)
               return false
            }
         }

         path.delete(product);
         suppliesSet.add(product);
         return true
      };
      
      return [...recipeIngredients.keys()].filter(recipe => dfs(recipe))
      
      const res = [];
      for (const recipe of recipeIngredients.keys()) {
         if (dfs(recipe)) {
            res.push(recipe);
         }
      }
      return res
   };
}


const findAllRecipes = new Solution().findAllRecipes;
console.log(new Solution().findAllRecipes(["bread"], [["yeast", "flour"]], ["yeast", "flour", "corn"]).sort().toString() === ["bread"].sort().toString())
console.log(new Solution().findAllRecipes(["bread", "sandwich"], [["yeast", "flour"], ["bread", "meat"]], ["yeast", "flour", "meat"]).sort().toString() === ["bread", "sandwich"].sort().toString())
console.log(new Solution().findAllRecipes(["bread", "sandwich", "burger"], [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]], ["yeast", "flour", "meat"]).sort().toString() === ["bread", "sandwich", "burger"].sort().toString())
console.log(new Solution().findAllRecipes(["bread"], [["yeast", "flour"]], (["yeast"])).sort().toString() === [].sort().toString())
console.log(new Solution().findAllRecipes(["ju", "fzjnm", "x", "e", "zpmcz", "h", "q"], [["d"], ["hveml", "f", "cpivl"], ["cpivl", "zpmcz", "h", "e", "fzjnm", "ju"], ["cpivl", "hveml", "zpmcz", "ju", "h"], ["h", "fzjnm", "e", "q", "x"], ["d", "hveml", "cpivl", "q", "zpmcz", "ju", "e", "x"], ["f", "hveml", "cpivl"]], ["f", "hveml", "cpivl", "d"]).sort().toString() === ['ju', 'q', 'fzjnm'].sort().toString())
