import pandas as pd
import numpy as np
a_pd_df = pd.DataFrame(np.random.random((4,3)),
                       index = np.arange(4),
                       columns=["A","B","C"])
print(a_pd_df.index)
