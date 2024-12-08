# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:24:19 2024

@author: Sarah
"""

import pandas as pd


class DataFrameLoader():
    def __init__(self, path_raw_interaction: str, path_raw_recipes: str, pp_recipe: str):
        """
        Dataset Loader

        Args:
            path_raw_interaction (str): path to raw_interaction.csv.
            path_raw_recipes (str): path to raw_recipes.csv.
            pp_recipe (str): path to pp_recipe.csv.

        Returns:
            None.
        """
        self.path_raw_interaction = path_raw_interaction
        self.path_raw_recipes = path_raw_recipes
        self.path_pp_recipe = pp_recipe

    def load(self):
        try:
            # Load the raw data from CSV files
            self.raw_interaction = pd.read_csv(self.path_raw_interaction)
            self.raw_recipes = pd.read_csv(self.path_raw_recipes)
            self.pp_recipe = pd.read_csv(self.path_pp_recipe)


            # Here, instead of calling prepare_final_dataframe(), we could manually merge or process the data
            # For example, simply concatenating the datasets:
            self.df = pd.concat([self.raw_interaction, self.raw_recipes, self.pp_recipe], axis=1)
            
        except FileNotFoundError:
            print('--- FILE NOT FOUND --- check csv creation ')
        except Exception as e:
            print(' -- UNEXPECTED ERROR --- : ', e)

        return self.df
