import pandas as pd

with open('Planning Parameters-Flattened-4.csv') as data_file:    
    df = pd.read_csv(data_file,index_col='SNo')

roadWidth = 30
plotExtent = 1500
plotWidth = 25
isCBA = 0
isMSBA = 1
privatePathLength = 0
privatePathWidth = 0

dfByUnits = df[(privatePathWidth>=df['Min Private Path Width']) & (privatePathLength<=df['Max Private Path Length'])& (roadWidth>=df['Min Road Width']) & (plotExtent>=df['Min Plot Extent']) & (plotWidth>=df['Min Plot Width/Frontage']) & (isCBA>=df['CBA Required?']) & (isMSBA>=df['MSB Required?'])].sort(columns=['Max FSI','Max Units','Max Height'], ascending=False).groupby('Type').head(1)
dfByHeight = df[(privatePathWidth>=df['Min Private Path Width']) & (privatePathLength<=df['Max Private Path Length']) & (roadWidth>=df['Min Road Width']) & (plotExtent>=df['Min Plot Extent']) & (plotWidth>=df['Min Plot Width/Frontage']) & (isCBA>=df['CBA Required?']) & (isMSBA>=df['MSB Required?'])].sort(columns=['Max FSI','Max Height','Max Units'], ascending=False).groupby('Type').head(1)
result = pd.concat([dfByUnits,dfByHeight],axis=0, join='outer').drop_duplicates().sort(columns=['Max FSI','Min Plot Extent'],ascending=False)[['Type','Max FSI','Max Units Desc','Max Height Desc','Blocks','Max Plot Coverage']]

print(result)
