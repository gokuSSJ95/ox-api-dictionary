import requests,json,sys
p = input("Enter word to be searched.")
url = "https://od-api.oxforddictionaries.com:443/api/v1/entries/en/"
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
print ('Word is: '+d['results'][0]['id'])

#Phonetic Spelling
print("Pronounciation: "+d['results'][0]['lexicalEntries'][0]['pronunciations'][0]['phoneticSpelling'])
cnt1=1
for ia in range(0,len(d['results'][0]['lexicalEntries'])):
    if('entries' in d['results'][0]['lexicalEntries'][ia]):
        for ib in range(0,len(d['results'][0]['lexicalEntries'][ia]['entries'])):
            if('senses' in d['results'][0]['lexicalEntries'][ia]['entries'][ib]):
                for ic in range(0,len(d['results'][0]['lexicalEntries'][ia]['entries'][ib]['senses'])):
                    print()
                    if('definitions' in d['results'][0]['lexicalEntries'][ia]['entries'][ib]['senses'][ic]):
                        for idd in range(0,len(d['results'][0]['lexicalEntries'][ia]['entries'][ib]['senses'][ic]['definitions'])):
                            print("Definition "+str(cnt1))
                            print(d['results'][0]['lexicalEntries'][ia]['entries'][ib]['senses'][ic]['definitions'][idd])
                            cnt1+=1
                    if('examples' in d['results'][0]['lexicalEntries'][ia]['entries'][ib]['senses'][ic]):
                        for idd in range(0,len(d['results'][0]['lexicalEntries'][ia]['entries'][ib]['senses'][ic]['examples'])):
                            print("Example")
                            print(d['results'][0]['lexicalEntries'][ia]['entries'][ib]['senses'][ic]['examples'][idd]['text'])
                    if('subsenses' in d['results'][0]['lexicalEntries'][ia]['entries'][ib]['senses'][ic]):
                        for idd in range(0,len(d['results'][0]['lexicalEntries'][ia]['entries'][ib]['senses'][ic]['subsenses'])):
                            if('definitions' in d['results'][0]['lexicalEntries'][ia]['entries'][ib]['senses'][ic]['subsenses'][idd]):
                                for ie in range(0,len(d['results'][0]['lexicalEntries'][ia]['entries'][ib]['senses'][ic]['subsenses'][idd]['definitions'])):
                                    print()
                                    print("Sub-definition")
                                    print(d['results'][0]['lexicalEntries'][ia]['entries'][ib]['senses'][ic]['subsenses'][idd]['definitions'][ie])
                            if('examples' in d['results'][0]['lexicalEntries'][ia]['entries'][ib]['senses'][ic]['subsenses'][idd]):
                                for ie in range(0,len(d['results'][0]['lexicalEntries'][ia]['entries'][ib]['senses'][ic]['subsenses'][idd]['examples'])):
                                    print("Example")
                                    print(d['results'][0]['lexicalEntries'][ia]['entries'][ib]['senses'][ic]['subsenses'][idd]['examples'][ie]['text'])
