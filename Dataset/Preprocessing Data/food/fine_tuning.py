import sys
import csv
import pandas as pd
import numpy as np
import io

#cd "BPHC Internships\3.University of Hamburg"

for i in range(1,4):
    df = pd.read_csv(f'List_{i}.csv')
    print(df)

    f= io.open(f'Fine_tuning/{i}.fine_tuning_data.txt', "w+", encoding="utf-8")

    for l in range(df.shape[0]):
        for m in range(df.shape[0]):    
            if(l != m):
                obj1 = df['itemLabel'][l]
                obj2 = df['itemLabel'][m]
                #print("Which is wider, and thus has more [MASK], ", obj1, " or ", obj2)
                f.write("Which is more [V nutritious], and thus more [A healthy], " + obj1 + " or " + obj2 + "\n")
                
    f.close()