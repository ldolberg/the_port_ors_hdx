import urllib2
import urllib
import json
import pprint

districts = json.loads('''{"kavrepalanchok": ["27.58333", "85.66667"], "dolakha": ["27.68027", "86.0701"], 
"lalitpur": ["27.67658", "85.31417"], "dhading": ["27.86424", "84.9283"], 
"bhaktapur": ["27.67298", "85.43005"], "ramechhap": ["27.32207", "86.05913"], 
"makwanpur": ["27.41667", "85.25"], "kathmandu": ["27.70169", "85.3206"], 
"nuwakot": ["28", "83.83333"], "sindhuli": ["27.2799", "85.98421"], 
"rasuwa": ["27.08617", "86.42758"], "okhaldhunga": ["27.31032", "86.50502"], 
"gorkha": ["28.00242", "84.62009"], "sindhupalchowk": [0, 0],"kanchanpur": ["28.83333", "80.33333"], "palpa": ["27.75", "83.83333"], "sankhuwasabha": ["27.58333", "87.33333"], "rupandehi": ["27.66667", "83.41667"], "gulmi": ["28.06941", "83.24536"], "arghakhanchi": ["27.91667", "83.08333"], "bara": ["26.75", "81"], "morang": ["-37.65", "145.1"], "parsa": ["34.92466", "68.64761"], "sindhuli": ["27.2799", "85.98421"], "makawanpur": ["27.41429", "85.17962"], "dhankuta": ["26.98333", "87.33333"], "sarlahi": ["27", "85.58333"], "kaski": ["28.33333", "84"], "chitawan": ["27.68333", "84.43333"], "baglung": ["28.27189", "83.58976"], "panchthar": ["27.16667", "87.83333"], "kabhrepalanchok": [0, 0], "khotang": ["27.25", "86.83333"], "okhaldhunga": ["27.31032", "86.50502"], "gorkha": ["28.00242", "84.62009"], "baitadi": ["29.57113", "80.43722"], "taplejung": ["27.35", "87.66667"], "ilam": ["33.6374", "46.4227"], "mustang": ["29.18321", "83.95634"], "lalitpur": ["27.67658", "85.31417"], "rasuwa": ["27.08617", "86.42758"], "solukhumbu": ["27.75", "86.75"], "sunsari": ["26.66667", "87.16667"], "bhojpur": ["25.30886", "84.44504"], "dang": ["31.0699", "120.87635"], "parbat": ["35.23731", "74.58914"], "syangja": ["28.09596", "83.87243"], "lamjung": ["28.48914", "84.1884"], "nawalparasi": ["27.66667", "83.91667"], "tbd": ["33.22661", "69.77123"], "siraha": ["26.65411", "86.2087"], "dolakha": ["27.68027", "86.0701"], "dhading": ["27.86424", "84.9283"], "sindhupalchok": ["27.82936", "85.54504"], "bhaktapur": ["27.67298", "85.43005"], "ramechhap": ["27.32207", "86.05913"], "jhapa": ["22.57314", "89.39283"], "tanahu": ["27.91667", "84.25"], "nuwakot": ["28", "83.83333"], "udayapur": ["26.94167", "86.52031"], "kathmandu": ["27.70169", "85.3206"], "myagdi": ["28.58333", "83.33333"]}''')

if __name__ == '__main__':
	r = []
	for t in ["humanitarian","feedback"]:
		for d,coord in districts.iteritems():
			x = coord[0]
			y = coord[1]
		
			data_string = urllib.urlencode({'q': 'housing','x':x,'y':y,'type':t})


			# Make the HTTP request.
			url = 'http://localhost:5000/?'
			#print url+data_string
			#url = 'http://demo.ckan.org/api/3/action/group_list'
			response = urllib2.urlopen(url+data_string)
		
			#assert response.code == 200

			r.append( response.read())
	print ",".join(r)		