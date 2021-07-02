#!/usr/bin/env python
# coding: utf-8

# In[73]:


import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/bulbasaur')
data.status_code


# In[74]:


if data.status_code == 200:
    bulbasaur_data = data.json()


# In[76]:


bulbasaur = {
    'name' : bulbasaur_data['species']['name'],
    'abilities': [bulbasaur_data['abilities'][0]['ability']['name'],bulbasaur_data['abilities'][1]['ability']['name']],
    'weight' : bulbasaur_data['weight'], 
    'types' : [bulbasaur_data['types'][0]['type']['name'],bulbasaur_data['types'][1]['type']['name']]
}
print(bulbasaur)


# In[38]:


data = r.get('https://pokeapi.co/api/v2/pokemon/ivysaur')
data.status_code


# In[39]:


if data.status_code == 200:
    ivysaur_data = data.json()


# In[78]:


ivysaur = {
    'name' : ivysaur_data['species']['name'],
    'abilities': [ivysaur_data['abilities'][0]['ability']['name'],ivysaur_data['abilities'][1]['ability']['name']],
    'weight' : ivysaur_data['weight'], 
    'types' : [ivysaur_data['types'][0]['type']['name'],ivysaur_data['types'][1]['type']['name']]
}
print(ivysaur)


# In[40]:


data = r.get('https://pokeapi.co/api/v2/pokemon/venusaur')
data.status_code


# In[41]:


if data.status_code == 200:
    venusaur_data = data.json()


# In[80]:


venusaur = {
    'name' : venusaur_data['species']['name'],
    'abilities': [venusaur_data['abilities'][0]['ability']['name'],venusaur_data['abilities'][1]['ability']['name']],
    'weight' : venusaur_data['weight'], 
    'types' : [venusaur_data['types'][0]['type']['name'],venusaur_data['types'][1]['type']['name']]
}
print(venusaur)


# In[42]:


data = r.get('https://pokeapi.co/api/v2/pokemon/charmander')
data.status_code


# In[43]:


if data.status_code == 200:
    charmander_data = data.json()


# In[83]:


charmander = {
    'name' : charmander_data['species']['name'],
    'abilities': [charmander_data['abilities'][0]['ability']['name'],charmander_data['abilities'][1]['ability']['name']],
    'weight' : charmander_data['weight'], 
    'types' : [charmander_data['types'][0]['type']['name']]
}
print(charmander)


# In[44]:


data = r.get('https://pokeapi.co/api/v2/pokemon/charmeleon')
data.status_code


# In[45]:


if data.status_code == 200:
    charmeleon_data = data.json()


# In[85]:


charmeleon = {
    'name' : charmeleon_data['species']['name'],
    'abilities': [charmeleon_data['abilities'][0]['ability']['name'],charmeleon_data['abilities'][1]['ability']['name']],
    'weight' : charmeleon_data['weight'], 
    'types' : [charmeleon_data['types'][0]['type']['name']]
}
print(charmeleon)


# In[46]:


data = r.get('https://pokeapi.co/api/v2/pokemon/charizard')
data.status_code


# In[47]:


if data.status_code == 200:
    charizard_data = data.json()


# In[86]:


charizard= {
    'name' : charizard_data['species']['name'],
    'abilities': [charizard_data['abilities'][0]['ability']['name'],charizard_data['abilities'][1]['ability']['name']],
    'weight' : charizard_data['weight'], 
    'types' : [charizard_data['types'][0]['type']['name'],charizard_data['types'][1]['type']['name']]
}
print(charizard)


# In[71]:


Charizard = {
    'name' : charizard_data['species']['name'],
    'abilities': [charizard_data['abilities'][0]['ability']['name'],charizard_data['abilities'][1]['ability']['name']],
    'weight' : charizard_data['weight'], 
    'types' : [charizard_data['types'][0]['type']['name'],charizard_data['types'][1]['type']['name']]
}
print(Charizard)


# In[48]:


data = r.get('https://pokeapi.co/api/v2/pokemon/squirtle')
data.status_code


# In[49]:


if data.status_code == 200:
    squirtle_data = data.json()


# In[88]:


squirtle = {
    'name' : squirtle_data['species']['name'],
    'abilities': [squirtle_data['abilities'][0]['ability']['name'],squirtle_data['abilities'][1]['ability']['name']],
    'weight' : squirtle_data['weight'], 
    'types' : [squirtle_data['types'][0]['type']['name']]
}
print(squirtle)


# In[50]:


data = r.get('https://pokeapi.co/api/v2/pokemon/wartortle')
data.status_code


# In[51]:


if data.status_code == 200:
    wartortle_data = data.json()


# In[91]:


wartortle = {
    'name' : wartortle_data['species']['name'],
    'abilities': [wartortle_data['abilities'][0]['ability']['name'],wartortle_data['abilities'][1]['ability']['name']],
    'weight' : wartortle_data['weight'], 
    'types' : [wartortle_data['types'][0]['type']['name']]
}
print(wartortle)


# In[68]:


data = r.get('https://pokeapi.co/api/v2/pokemon/blastoise')
data.status_code


# In[53]:


if data.status_code == 200:
    blastoise_data = data.json()


# In[93]:


blastoise = {
    'name' : blastoise_data['species']['name'],
    'abilities': [blastoise_data['abilities'][0]['ability']['name'],blastoise_data['abilities'][1]['ability']['name']],
    'weight' : blastoise_data['weight'], 
    'types' : [blastoise_data['types'][0]['type']['name']]
}
print(blastoise)


# In[54]:


data = r.get('https://pokeapi.co/api/v2/pokemon/caterpie')
data.status_code


# In[55]:


if data.status_code == 200:
    caterpie_data = data.json()


# In[95]:


caterpie = {
    'name' : caterpie_data['species']['name'],
    'abilities': [caterpie_data['abilities'][0]['ability']['name'],caterpie_data['abilities'][1]['ability']['name']],
    'weight' : caterpie_data['weight'], 
    'types' : [caterpie_data['types'][0]['type']['name']]
}
print(caterpie)


# In[56]:


data = r.get('https://pokeapi.co/api/v2/pokemon/metapod')
data.status_code


# In[57]:


if data.status_code == 200:
    metapod_data = data.json()


# In[100]:


metapod = {
    'name' : metapod_data['species']['name'],
    'abilities': [metapod_data['abilities'][0]['ability']['name']],
    'weight' : metapod_data['weight'], 
    'types' : [metapod_data['types'][0]['type']['name']]
}
print(metapod)


# In[105]:


data = r.get('https://pokeapi.co/api/v2/pokemon/butterfree')
data.status_code


# In[106]:


if data.status_code == 200:
    butterfree_data = data.json()


# In[107]:


butterfree = {
    'name' : butterfree_data['species']['name'],
    'abilities': [butterfree_data['abilities'][0]['ability']['name'],butterfree_data['abilities'][1]['ability']['name']],
    'weight' : butterfree_data['weight'], 
    'types' : [butterfree_data['types'][0]['type']['name'],butterfree_data['types'][1]['type']['name']]
}
print(butterfree)


# In[110]:


data = r.get('https://pokeapi.co/api/v2/pokemon/weedle')
data.status_code


# In[111]:


if data.status_code == 200:
    weedle_data = data.json()


# In[112]:


weedle = {
    'name' : weedle_data['species']['name'],
    'abilities': [weedle_data['abilities'][0]['ability']['name'],weedle_data['abilities'][1]['ability']['name']],
    'weight' : weedle_data['weight'], 
    'types' : [weedle_data['types'][0]['type']['name']]
}
print(weedle)


# In[116]:


data = r.get('https://pokeapi.co/api/v2/pokemon/kakuna')
data.status_code


# In[117]:


if data.status_code == 200:
    kakuna_data = data.json()


# In[119]:


kakuna = {
    'name' : kakuna_data['species']['name'],
    'abilities': [kakuna_data['abilities'][0]['ability']['name']],
    'weight' : kakuna_data['weight'], 
    'types' : [kakuna_data['types'][0]['type']['name'],kakuna_data['types'][1]['type']['name']]
}
print(kakuna)


# In[120]:


data = r.get('https://pokeapi.co/api/v2/pokemon/beedrill')
data.status_code


# In[121]:


if data.status_code == 200:
    beedrill_data = data.json()


# In[122]:


beedrill = {
    'name' : beedrill_data['species']['name'],
    'abilities': [beedrill_data['abilities'][0]['ability']['name'],beedrill_data['abilities'][1]['ability']['name']],
    'weight' : beedrill_data['weight'], 
    'types' : [beedrill_data['types'][0]['type']['name'],beedrill_data['types'][1]['type']['name']]
}
print(beedrill)


# In[123]:


data = r.get('https://pokeapi.co/api/v2/pokemon/pidgey')
data.status_code


# In[124]:


if data.status_code == 200:
    pidgey_data = data.json()


# In[125]:


pidgey = {
    'name' : pidgey_data['species']['name'],
    'abilities': [pidgey_data['abilities'][0]['ability']['name'],pidgey_data['abilities'][1]['ability']['name']],
    'weight' : pidgey_data['weight'], 
    'types' : [pidgey_data['types'][0]['type']['name'],pidgey_data['types'][1]['type']['name']]
}
print(pidgey)


# In[126]:


data = r.get('https://pokeapi.co/api/v2/pokemon/pidgeotto')
data.status_code


# In[127]:


if data.status_code == 200:
    pidgeotto_data = data.json()


# In[130]:


pidgeotto = {
    'name' : pidgeotto_data['species']['name'],
    'abilities': [pidgeotto_data['abilities'][0]['ability']['name'],pidgeotto_data['abilities'][1]['ability']['name']],
    'weight' : pidgeotto_data['weight'], 
    'types' : [pidgeotto_data['types'][0]['type']['name'],pidgeotto_data['types'][1]['type']['name']]
}
print(pidgeotto)


# In[133]:


data = r.get('https://pokeapi.co/api/v2/pokemon/rattata')
data.status_code


# In[134]:


if data.status_code == 200:
    rattata_data = data.json()


# In[136]:


rattata = {
    'name' : rattata_data['species']['name'],
    'abilities': [rattata_data['abilities'][0]['ability']['name'],rattata_data['abilities'][1]['ability']['name']],
    'weight' : rattata_data['weight'], 
    'types' : [rattata_data['types'][0]['type']['name']]
}
print(rattata)


# In[137]:


data = r.get('https://pokeapi.co/api/v2/pokemon/pidgeot')
data.status_code


# In[138]:


if data.status_code == 200:
    pidgeot_data = data.json()


# In[139]:


pidgeot = {
    'name' : pidgeot_data['species']['name'],
    'abilities': [pidgeot_data['abilities'][0]['ability']['name'],pidgeot_data['abilities'][1]['ability']['name']],
    'weight' : pidgeot_data['weight'], 
    'types' : [pidgeot_data['types'][0]['type']['name'],pidgeot_data['types'][1]['type']['name']]
}
print(pidgeot)


# In[140]:


data = r.get('https://pokeapi.co/api/v2/pokemon/raticate')
data.status_code


# In[141]:


if data.status_code == 200:
    raticate_data = data.json()


# In[143]:


raticate = {
    'name' : raticate_data['species']['name'],
    'abilities': [raticate_data['abilities'][0]['ability']['name'],raticate_data['abilities'][1]['ability']['name']],
    'weight' : raticate_data['weight'], 
    'types' : [raticate_data['types'][0]['type']['name']]
}
print(raticate)


# In[ ]:


names = ['bulbasaur', 'ivysaur', 'venusaur','charmander','charmeleon', 'charizard', 'squirtle', 'wartortle','blastoise','caterpie', 'metapod', 'butterfree','weedle','kakuna','beedrill','pidgey','pidgeotto','pidgeot','rattata','raticate']

for name in names:
    data = r.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
    print(f'{name} | {data.status_code}')


# In[ ]:




