import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sbi_df=pd.read_csv('sbimf.csv',parse_dates=['Month'])
sbi_df=sbi_df.set_index(['Month'],drop=True)
sbi_df.sort_index(ascending=True,inplace=True)
sbi_df=sbi_df[['Close Price','Open Price']]

hdfc_df=pd.read_csv('hdfcmf.csv',parse_dates=['Month'])
hdfc_df=hdfc_df.set_index(['Month'],drop=True)
hdfc_df.sort_index(ascending=True,inplace=True)
hdfc_df=hdfc_df[['Close Price','Open Price']]

axis_df=pd.read_csv('axismf.csv',parse_dates=['Month'])
axis_df=axis_df.set_index(['Month'],drop=True)
axis_df.sort_index(ascending=True,inplace=True)
axis_df=axis_df[['Close Price','Open Price']]

dsp_df=pd.read_csv('dspmf.csv',parse_dates=['Month'])
dsp_df=dsp_df.set_index(['Month'],drop=True)
dsp_df.sort_index(ascending=True,inplace=True)
dsp_df=dsp_df[['Close Price','Open Price']]





sbi_df['Gain']=((sbi_df['Close Price']-sbi_df['Open Price'])*100/sbi_df['Open Price'])
print(sbi_df)
hdfc_df['Gain']=((hdfc_df['Close Price']-hdfc_df['Open Price'])*100/hdfc_df['Open Price'])
print(hdfc_df)

dsp_df['Gain']=((dsp_df['Close Price']-dsp_df['Open Price'])*100/dsp_df['Open Price'])
print(sbi_df)

axis_df['Gain']=((axis_df['Close Price']-axis_df['Open Price'])*100/axis_df['Open Price'])
print(sbi_df)



# plt.plot(sbi_df['Gain'])
# plt.show()
# plt.plot(hdfc_df['Gain'])
# plt.show()

# print(sbi_df.Gain.max())
# print(sbi_df.Gain.min())
# print(hdfc_df.Gain.max())
# print(hdfc_df.Gain.min())

# plt.hist(sbi_df['Gain'],bins=range(-4,4,1))
# plt.show()
# plt.hist(hdfc_df['Gain'],bins=range(-4,4,1))
# plt.show()

sns.kdeplot(sbi_df['Gain'],label='SBI')
sns.kdeplot(hdfc_df['Gain'],label='HDFC')
sns.kdeplot(dsp_df['Gain'],label='DSP')
sns.kdeplot(axis_df['Gain'],label='AXIS')
plt.legend()
plt.title('Volatality of Stocks')
plt.show()

print("STD",sbi_df.Gain.std())
print(sbi_df.Gain.mean())

from scipy import stats

sbi_stats=stats.norm.interval(0.9,loc=sbi_df.Gain.mean(),scale=sbi_df.Gain.std())
print(sbi_stats)
amt=100000
sbi_VAR=amt*sbi_stats[0]/100
print(sbi_VAR)


hdfc_stats=stats.norm.interval(0.9,loc=hdfc_df.Gain.mean(),scale=hdfc_df.Gain.std())
print(hdfc_stats)
amt=100000
hdfc_VAR=amt*hdfc_stats[0]/100
print(hdfc_VAR)


axis_stats=stats.norm.interval(0.9,loc=axis_df.Gain.mean(),scale=axis_df.Gain.std())
print(axis_stats)
amt=100000
axis_VAR=amt*axis_stats[0]/100
print(axis_VAR)


dsp_stats=stats.norm.interval(0.9,loc=dsp_df.Gain.mean(),scale=dsp_df.Gain.std())
print(dsp_stats)
amt=100000
dsp_VAR=amt*dsp_stats[0]/100
print(dsp_VAR)


# ic_cdf=stats.norm.cdf(-3.0,loc=sbi_df.Gain.mean(),scale=sbi_df.Gain.std())
# hdfc_cdf=stats.norm.cdf(-3.0,loc=hdfc_df.Gain.mean(),scale=hdfc_df.Gain.std())
# print('Loss')
# print(ic_cdf)
# print(hdfc_cdf)

print('Gain')
ic_cdf1=1-stats.norm.cdf(4.0,loc=sbi_df.Gain.mean(),scale=sbi_df.Gain.std())
hdfc_cdf1=1-stats.norm.cdf(4.0,loc=hdfc_df.Gain.mean(),scale=hdfc_df.Gain.std())
axis_cdf1=1-stats.norm.cdf(4.0,loc=axis_df.Gain.mean(),scale=axis_df.Gain.std())
dsp_cdf1=1-stats.norm.cdf(4.0,loc=dsp_df.Gain.mean(),scale=dsp_df.Gain.std())
print("Gain above 4%")
print("SBI Mutual Fund",ic_cdf1)
print("HDFC Mutual Fund",hdfc_cdf1)
print("AXIS Mutual Fund",axis_cdf1)
print("DSP Mutual Fund",dsp_cdf1)
