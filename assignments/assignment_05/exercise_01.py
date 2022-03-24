import pandas as pd 

url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=*&K%C3%98N=1%2C2&ALDER=*&CIVILSTAND=U%2CG&Tid=2020K4'
df = pd.read_csv(url, sep=';')

url1 = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=*&K%C3%98N=1%2C2&ALDER=*&CIVILSTAND=U%2CG&Tid=2008K4'
df1 = pd.read_csv(url1, sep=';')

# 2020 data
#test = df[(df['CIVILSTAND']=='Gift/separeret') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='Hele landet')  & (df['KØN']=='Mænd')]
#stats = test[['INDHOLD']].apply(pd.to_numeric)
#print(test)
#print(stats)

# 2008 data
#test1 = df1[(df1['CIVILSTAND']=='Gift/separeret') & (df1['ALDER']=='I alt') & (df1['OMRÅDE']=='Hele landet')  & (df1['KØN']=='Mænd')]
#stats1 = test1[['INDHOLD']].apply(pd.to_numeric)
#print(test1)
#print(stats1)

#print('The difference between divorced danes in 2008 to 2020 in percent ->')
#diff = stats-stats1
#print(str(round((diff/stats1) * 100, 2)) + '%')

#1072984 - 1096210 = -23226
#( -23226 / 1096210 ) · 100 = -2.12%



#København (Sjælland)
unmarried_københavn_men = df[(df['CIVILSTAND']=='Ugift') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='København')  & (df['KØN']=='Mænd')]
stats1 = unmarried_københavn_men[['INDHOLD']].apply(pd.to_numeric)
unmarried_københavn_women = df[(df['CIVILSTAND']=='Ugift') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='København')  & (df['KØN']=='Kvinder')]
stats2 = unmarried_københavn_women[['INDHOLD']].apply(pd.to_numeric)
#Aarhus (Jylland)
unmarried_Aarhus_men = df[(df['CIVILSTAND']=='Ugift') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='Aarhus')  & (df['KØN']=='Mænd')]
stats3 = unmarried_Aarhus_men[['INDHOLD']].apply(pd.to_numeric)
unmarried_Aarhus_women = df[(df['CIVILSTAND']=='Ugift') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='Aarhus')  & (df['KØN']=='Kvinder')]
stats4 = unmarried_Aarhus_women[['INDHOLD']].apply(pd.to_numeric)
#Odense (Fyn)
unmarried_Odense_men = df[(df['CIVILSTAND']=='Ugift') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='Odense')  & (df['KØN']=='Mænd')]
stats5 = unmarried_Odense_men[['INDHOLD']].apply(pd.to_numeric)
unmarried_Odense_women = df[(df['CIVILSTAND']=='Ugift') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='Odense')  & (df['KØN']=='Kvinder')]
stats6 = unmarried_Odense_women[['INDHOLD']].apply(pd.to_numeric)
#Aalborg (Jylland)
unmarried_Aalborg_men = df[(df['CIVILSTAND']=='Ugift') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='Aalborg')  & (df['KØN']=='Mænd')]
stats7 = unmarried_Aalborg_men[['INDHOLD']].apply(pd.to_numeric)
unmarried_Aalborg_women = df[(df['CIVILSTAND']=='Ugift') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='Aalborg')  & (df['KØN']=='Kvinder')]
stats8 = unmarried_Aalborg_women[['INDHOLD']].apply(pd.to_numeric)
#Esbjerg (Jylland)
unmarried_Esbjerg_men = df[(df['CIVILSTAND']=='Ugift') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='Esbjerg')  & (df['KØN']=='Mænd')]
stats9 = unmarried_Esbjerg_men[['INDHOLD']].apply(pd.to_numeric)
unmarried_Esbjerg_women = df[(df['CIVILSTAND']=='Ugift') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='Esbjerg')  & (df['KØN']=='Kvinder')]
stats10 = unmarried_Esbjerg_women[['INDHOLD']].apply(pd.to_numeric)

#Regne Fregne

københavn = stats1 + stats2
print(københavn[['INDHOLD']].apply(pd.to_numeric))
#pd.to_numeric(københavn, downcast="integer")
total = 65951 + 64776 + københavn

#print(total / københavn * 100)


#65951 m
#64776 k

aarhus = stats3 + stats4
#49714 m
#49812 k

odense = stats5 + stats6
#33731 m
#33878 k

aalborg = stats7 + stats8
#36427 m
#36549 k

esbjerg = stats9 + stats10
#23040 m
#23008 k



