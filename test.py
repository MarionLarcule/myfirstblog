print('Hello, Django girls!')
if 3 < 2 : 
	print ('it\'s work') # Un commentaire commence par '#' C GENIAL !!
else : 
	print ('New')

# Fonction def name():
def marion(name):
	print ('Salut')
	if name == 'Marion':
		print ('Salut Mama') 
	else : 
		print('Salut Mac')
marion('Marion')
# Les boucles for = pour / in = dans
girls = ['Charlotte', 'Marion', 'Francesca', 'Marion']
for name in girls : 
	print('Hello' + ' ' + name + ' ' + '!')