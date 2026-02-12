class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients_list: list[list[str]], supplies: list[str]) -> list[str]:
        """
        Time complexity: O(V + E)
            V: supplies count + recipes count
            E: prequired supplies for a recipe
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: hash map, hash set, list
            A: DFS with memoization (DP on DAG), topological sort with cycle detection
            Model: graph
        """
        supplies_set = set(supplies)
        recipe_ingredients = {
            recipe: ingredients for recipe, ingredients in zip(recipes, ingredients_list)
        }
        bad_recipes = set()
        path = set()

        def dfs(product: str) -> bool:
            if product in supplies_set:
                return True
            elif (
                product not in recipe_ingredients or
                product in path or
                product in bad_recipes
            ):
                return False
            
            path.add(product)
            
            for ingredient in recipe_ingredients[product]:
                if not dfs(ingredient):
                    path.discard(product)
                    bad_recipes.add(product)
                    return False

            path.discard(product)
            supplies_set.add(product)
            return True

        return [recipe for recipe in recipe_ingredients if dfs(recipe)]


print(sorted(Solution().findAllRecipes(["bread"], [["yeast", "flour"]], ["yeast", "flour", "corn"])) == sorted(["bread"]))
print(sorted(Solution().findAllRecipes(["bread", "sandwich"], [["yeast", "flour"], ["bread", "meat"]], ["yeast", "flour", "meat"])) == sorted(["bread", "sandwich"]))
print(sorted(Solution().findAllRecipes(["bread", "sandwich", "burger"], [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]], ["yeast", "flour", "meat"])) == sorted(["bread", "sandwich", "burger"]))
print(sorted(Solution().findAllRecipes(["bread"], [["yeast", "flour"]], (["yeast"]))) == sorted([]))
print(sorted(Solution().findAllRecipes(["ju", "fzjnm", "x", "e", "zpmcz", "h", "q"], [["d"], ["hveml", "f", "cpivl"], ["cpivl", "zpmcz", "h", "e", "fzjnm", "ju"], ["cpivl", "hveml", "zpmcz", "ju", "h"], ["h", "fzjnm", "e", "q", "x"], ["d", "hveml", "cpivl", "q", "zpmcz", "ju", "e", "x"], ["f", "hveml", "cpivl"]], ["f", "hveml", "cpivl", "d"])) == sorted(['ju', 'q', 'fzjnm']))
