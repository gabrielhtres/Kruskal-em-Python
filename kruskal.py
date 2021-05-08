arestas=[] #Lista de arestasn que será passada para o objeto como parâmetro
grafoComp=[] #Composição da MST
vertices=[] #Lista de vértices para controle
n=0
ver=1
flag=False
flag2=False

#---------------------------------------------INICIO DA CLASSE--------------------------------------------------
class Vertice: #Criação da classes e seus atributos
	arestasG=[]

#INICIO DOS MÉTODOS

	def __init__(self, arestas): #Método construtor da classe
		self.arestasG = arestas #Defino a lista de arestas como objeto

		for x in self.arestasG: #Adiciono o numero 0 a cada vértice da lista como verificador
			x.append(0)

		print(str(self.arestasG))

	def guardaAresta(self, arestaMenor, vertices): #Método para guardar as arestas e controlar os vértices
		
		for a in self.arestasG: #Percorre as arestas
			if a[0] == arestaMenor[0] and a[1] == arestaMenor[1] and a[2] == arestaMenor[2]:
				a[3]=1 #Encontra a aresta retornada no objeto e altera seu status para presente na MST
				break

		for x in vertices: #Percorre a lista de vértices e altera seus status para presente na MST
			if arestaMenor[0] == x[0]:
				x[1] = True
			if arestaMenor[1] == x[0]:
				x[1] = True

		return arestaMenor #Retorna a menor aresta possível encontrada para grafoComp(Lista com as arestas na MST)

	def busca_Menor_Aresta_Possivel(self): #Busca a menor aresta possível
		arestaMenor=[] #Define os valores default para iniciar o método
		menor=999
		i=0

		while i < len(self.arestasG):
			x=self.arestasG[i]
			if x[3] == 0: #Verifica se a aresta é possível ou se já está na MST
				for y in vertices: #Percorre os vértices para verificar os que já estão na MST
					if (x[0] == y[0] and y[1] == False) or (x[1] == y[0] and y[1] == False): #Testa se os vértices já estão ou não na MST
						if x[2] < menor: #Testes para definir a menor aresta possível
							menor=x[2]
							arestaMenor=x
							i=i+1
							flag2=True
							break
						else:
							i=i+1
				if flag2 == False: #Flag para controlar as iterações do while
					i=i+1
			else:
				i=i+1

			flag2=False #Define a flag para False novamente, para repetir os testes na próxima iteração

		return self.guardaAresta(arestaMenor, vertices) #Chama o método que guarda as arestas

	def mostraMST(self, MST): #Método para imprimir os vértices da MST
		for g in MST: #Percorre a MST para imprimir as arestas
			print("Aresta: " + str(g[0]) + " ----- " + str(g[1]) + " e Peso: " + str(g[2]))

#------------------------------------------FIM DA CLASSE-------------------------------------------------------

arestas.append([0, 1, 5]) #Defino as arestas e as guardo em uma lista
arestas.append([1, 2, 1])
arestas.append([2, 3, 6])
arestas.append([3, 0, 10])
arestas.append([0, 2, 8])
arestas.append([1, 4, 20])

vertices.append([0, False]) #Armamzeno os vértices para controle posterior
vertices.append([1, False])
vertices.append([2, False])
vertices.append([3, False])
vertices.append([4, False])

MST = Vertice(arestas) #Instancio o objeto Vertice passando a lista de arestas

while ver == 1: #Laço de repetição para continuar adicionando arestas na MST enquanto possível
	for t in vertices:
		if t[1] == False:
			flag=True				
		else:
			flag=False
	
	if flag == True:
		#print("Foi") #Teste
		grafoComp.append(MST.busca_Menor_Aresta_Possivel()) #Chamo o método que inicia os passos de inserção na MST e salvo o resultado em uma lista
	else:
		ver=0

MST.mostraMST(grafoComp) #Chamo o método para impressão da MST