import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    new_products = products[(products['low_fats' ] == 'Y') & (products['recyclable' ] == 'Y') ]
    return new_products[['product_id']]
    
