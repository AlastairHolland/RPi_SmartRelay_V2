r = ""
for i in range(25, 1025, 50):
	r = r + '<form action="/relay/'+str(i/1000)+'"><button class="button" style ="height: 20px; float:left">'+str(i)+'ms</button></form>'
	r = r + '<form action="/relay/'+str((i+25)/1000)+'"><button class="button" style ="height: 20px; float:right">'+str(i+25)+'ms</button></form>'
print(r)
