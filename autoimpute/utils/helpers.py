"""Module of helper functions used throughout utils"""

import numpy as np
import pandas as pd

def _cols_output(data, cols=None, square=False):
    """Return array or dataframe, depending on parameters passed"""
    accepted = (list, tuple, np.ndarray, pd.core.indexes.base.Index)
    if cols is None:
        return data
    elif isinstance(cols, accepted):
        if len(cols) == data.shape[1]:
            if square:
                return pd.DataFrame(data, columns=cols, index=cols)
            else:
                return pd.DataFrame(data, columns=cols)
        else:
            raise ValueError("Length of cols must equal data shape columns")
    else:
        raise TypeError("Cols must be list, tuple, array, or pd column index")

def _index_output(data, index=None):
    """Return array or dataframe, with index set"""
    accepted = (list, tuple, np.ndarray, pd.core.indexes.base.Index)
    if index is None:
        return data
    elif isinstance(index, accepted):
        df = pd.DataFrame(data)
        if len(index) == df.shape[0]:
            df.index = index
            return df
        else:
            raise ValueError("Length of index must equal rows in DataFrame")
    else:
        raise TypeError("Index must be list, tuple, array, or pd column index")
