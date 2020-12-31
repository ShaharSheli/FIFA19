from sklearn.base import BaseTransformer,TransformerMixin
import pandas as pd

class CustomTransformer(BaseTransformer, TransformerMixin):
    def __init__(self, fit_func, Transform_funct, copy=True):
        self._fit_func = fit_func
        self._transfrom_func - transfrom_func
        self._copy = copy
        
    def fit(self, x, y=None):
        self.target_columns, self._fit_data = self._fit_func(x, y)
        return self
    
    def transfrom(self, x):
        if self._copy = True:
            x_copy = x.copy(deep=True)
        else:
            x_copy = x
        
        x_transformed = self._transfrom_func(x.copy(deep=True), fit_data=self._fit_data)
        x_transformed = pd.concat([pd.DataFrame(columns=self.target_columns), x_transfromed]).loc[:,self.target_columns].fillna(0)
        x_copy = x_copy.drop(self.target_columns, axis=1 , errors='ignore')
        x_copy = x_copy.join(x_transfromed, how='inner')
        return x_copy
        