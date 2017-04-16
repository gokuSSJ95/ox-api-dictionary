import requests,json,sys
p = input("Enter word to be searched.")
url = "https://od-api.oxforddictionaries.com:443/api/v1/entries/en/" #APIs provided by oxford
url+=p

headers = {
    'app_id': "b956e709",
    'app_key': "0ce6c2189141e92eb0137260dbf8c80f",
    'cache-control': "no-cache",
    'postman-token': "0a192645-af1c-6525-ff59-fabe8fbe7e2e"
    }

response = requests.request("GET", url, headers=headers)
if  response.headers['Content-Type'] == 'text/html':
    print ('Entered word is wrong.')
    sys.exit()


    

d = json.loads(response.text)
tvara = 'Word is: '+d['results'][0]['id']
print (tvara)
tvara = "Pronounciation: "+d["results"][0]['lexicalEntries'][0]['pronunciations'][0]['phoneticSpelling']

#Phonetic Spelling
print(tvara)
cnt1=1
for ia in range(0,len(d['results'][0]['lexicalEntries'])):
    for ib in range(0,len(d['results'][0]['lexicalEntries'][ia]['entries'])):
        for ic in range(0,len(d['results'][0]['lexicalEntries'][ia]['entries'][ib]['senses'])):
            for idd in range(0,len(d['results'][0]['lexicalEntries'][ia]['entries'][ib]['senses'][ic]['definitions'])):
                tvara = "Definition "+str(cnt1)
                print(tvara)
                tvara = d['results'][0]['lexicalEntries'][ia]['entries'][ib]['senses'][ic]['definitions'][idd] 
                print(tvara)
                cnt1+=1

                
