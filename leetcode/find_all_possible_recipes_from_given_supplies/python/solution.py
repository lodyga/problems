class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients_per_recipe: list[list[str]], supplies: list[str]) -> list[str]:
        """
        Time complexity: O(V + E)
            V: supplies count + recipes count
            E: prequired suppries for a recipe
        Auxiliary space complexity: O(V + E)
        Tags: dfs, recursion, graph, topological sort
        """
        supplies = set(supplies)
        recipe_set = set(recipes)

        preqreqs = {}
        for recipe, ingredients in zip(recipes, ingredients_per_recipe):
            ingredients = set(ingredients)
            # Recepie require itself in ingredients
            if recipe in ingredients:
                recipe_set.remove(recipe)
            else:
                preqreqs[recipe] = ingredients

        visited = set()

        def dfs(recipe):
            if (
                recipe in supplies or
                recipe in possible_recipes
            ):
                return True
            # Recipe cannot be made, ingredient is not avaible.
            elif (
                recipe not in supplies and
                recipe not in preqreqs
            ):
                return False
            # cycle detection
            elif recipe in visited:
                return False

            visited.add(recipe)

            for ingredient in preqreqs[recipe]:
                if not dfs(ingredient):
                    return False

            visited.remove(recipe)

            return True

        possible_recipes = set()
        for recipe in recipe_set:
            if dfs(recipe):
                possible_recipes.add(recipe)

        return list(possible_recipes)


print(Solution().findAllRecipes(["bread"], [["yeast", "flour"]], ["yeast", "flour", "corn"]), ["bread"])
print(Solution().findAllRecipes(["bread", "sandwich"], [["yeast", "flour"], ["bread", "meat"]], ["yeast", "flour", "meat"]), ["bread", "sandwich"])
print(Solution().findAllRecipes(["bread", "sandwich", "burger"], [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]], ["yeast", "flour", "meat"]), ["bread", "sandwich", "burger"])
print(Solution().findAllRecipes(["bread"], [["yeast", "flour"]], ["yeast"]), [])
print(Solution().findAllRecipes(["ju", "fzjnm", "x", "e", "zpmcz", "h", "q"], [["d"], ["hveml", "f", "cpivl"], ["cpivl", "zpmcz", "h", "e", "fzjnm", "ju"], ["cpivl", "hveml", "zpmcz", "ju", "h"], ["h", "fzjnm", "e", "q", "x"], ["d", "hveml", "cpivl", "q", "zpmcz", "ju", "e", "x"], ["f", "hveml", "cpivl"]], ["f", "hveml", "cpivl", "d"]), ['ju', 'q', 'fzjnm'])