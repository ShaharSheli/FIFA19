import seaborn as sns
import pandas as pd

def heatmap(df,f1,f2,measure,threshhold,figsize=(25,10),font_scale=1.2):
    
    sns.set(rc={'figure.figsize':figsize})
    
    heat_precent = pd.DataFrame(df.groupby([f1,f2]).mean()[measure]).reset_index()
    #heat_precent[measure]*=100
    heat_count = pd.DataFrame(df.groupby([f1,f2]).count()[measure]).reset_index()
    index_to_drop = heat_count[heat_count[measure]<=threshhold].index
    heat_precent = heat_precent.drop(index=index_to_drop).reset_index()
    heat_count = heat_count.drop(index=index_to_drop).reset_index()
    heat_precent = heat_precent.pivot(index=f1,columns=f2,values=measure)
    heat_count = heat_count.pivot(index=f1,columns=f2,values=measure)
    
    index = heat_count.index
    cols = heat_count.columns
    
    comb = []
    for i in index:
        for col in cols:
            comb.append((heat_precent.loc[i][col],heat_count.loc[i][col]))
            
    c = pd.DataFrame(comb)
    c = c.fillna(0)
    
    c[1] = c[1].astype(int)
    c[0] = c[0].map('{:,.2f}'.format)
    
    labels = np.array(list(zip(c[0],c[1])))
    label_format = [str(l[0] + "\n" + str(l[1])) for l in labels]
    labels = np.array(label_format).reshape(heat_count.shape)
    sns.heatmap(heat_precent,annot=labels,fmt='s')
    
        