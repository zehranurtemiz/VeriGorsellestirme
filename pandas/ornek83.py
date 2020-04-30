import pandas as pd
import numpy as np
veri_pd = pd.DataFrame(np.random.random((500,5)),columns=["A","B","C","D","E"])
print(veri_pd.idxmax())
