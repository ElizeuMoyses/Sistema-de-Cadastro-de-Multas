import tkinter as tk
from tkinter import ttk
import datetime as dt

# Criar uma janela/abrir
janela = tk.Tk()

# Titulo da janela
janela.title('Cadastro de Multas')

# Icone da Janela
janela.wm_iconbitmap('logo.ico')

#FUNÇÕES




#LISTAS

lista_status = ["Multa","Notificação"]
lista_sim_nao = ["Sim","Não"]
lista_tipo_infracao = ["Lista de infração"] #FALTA - Puxar as infrações do bando de dados
lista_empresa = ["Atlantis Saneamento",
                 "Águas de Jaguaruna",
                 "Gaivota Saneamento",
                 "Gravatal Saneamento",
                 "Guabituba Saneamento",
                 "Jaguaruna Saneamento",
                 "Sanitary",
                 "Sombrio Saneamento",] #FALTA - Puxar as empresas do bando de dados
lista_unidades = ["Lista de unidades"] #FALTA - Puxar as unidades do bando de dados
lista_CC = ["Lista de Centro de Custos"] #FALTA - Puxar os Centro de custo do bando de dados
#_______________________________________________________________________________________

#Texto do STATUS DA INFRAÇÃO
label_status = tk.Label(text="Status da Infração")
label_status.grid(row=1,column=0,padx= 10,pady=10,sticky='nswe',columnspan=1)
#Combobox do STATUS DA INFRAÇÃO
combbox_status = ttk.Combobox(values=lista_status)
combbox_status.grid(row=1,column=4,padx= 10,pady=10,sticky='nswe',columnspan=1)

#_______________________________________________________________________________________

#Texto do Nº DO CHAMADO DA NOTIFICAÇÃO
label_n_chamado_notificacao = tk.Label(text="Nº do Chamado da Notificação")
label_n_chamado_notificacao.grid(row=2,column=0,padx= 10,pady=10,sticky='nswe',columnspan=1)
#Box do NUMERO DA NOTIFICAÇÃO
entry_n_chamado_notificacao = tk.Entry()
entry_n_chamado_notificacao.grid(row=2,column=4,padx= 10,pady=10,sticky='nswe',columnspan=1)

#_______________________________________________________________________________________

#Texto do Nº DO CHAMADO DA MULTA
label_n_chamado_multa = tk.Label(text="Nº do Chamado da Multa")
label_n_chamado_multa.grid(row=3,column=0,padx= 10,pady=10,sticky='nswe',columnspan=1)

#Box do Nº DO CHAMADO DA MULTA
entry_n_chamado_multa = tk.Entry()
entry_n_chamado_multa.grid(row=3,column=4,padx= 10,pady=10,sticky='nswe',columnspan=1)

#________________________________________________________________________________________

#Texto do Nº DA NOTIFICAÇÃO
label_n_notificacao = tk.Label(text="Nº da Notificação")
label_n_notificacao.grid(row=4,column=0,padx= 10,pady=10,sticky='nswe',columnspan=1)

#Box do Nº DA NOTIFICAÇÃO
entry_n_notificacao = tk.Entry()
entry_n_notificacao.grid(row=4,column=4,padx= 10,pady=10,sticky='nswe',columnspan=1)

#_______________________________________________________________________________________

#Texto da DATA DA INFRAÇÃO
label_data_da_infracao = tk.Label(text="Data da Infração")
label_data_da_infracao.grid(row=5,column=0,padx= 10,pady=10,sticky='nswe',columnspan=1)

#Box da DATA DA INFRAÇÃO
entry_data_da_infracao = tk.Entry()
entry_data_da_infracao.grid(row=5,column=4,padx= 10,pady=10,sticky='nswe',columnspan=1)

#_______________________________________________________________________________________

#Texto da HORA DA INFRAÇÃO
label_hora_da_infracao = tk.Label(text="Hora da Infração")
label_hora_da_infracao.grid(row=5,column=0,padx= 10,pady=10,sticky='nswe',columnspan=1)

#Box da HORA DA INFRAÇÃO
entry_hora_da_infracao = tk.Entry()
entry_hora_da_infracao.grid(row=5,column=4,padx= 10,pady=10,sticky='nswe',columnspan=1)

#_______________________________________________________________________________________

# FALTA - Pesquisar as placas no bando de dados dos veículos

#Texto da PLACA DO VEÍCULO
label_placa_do_veiculo = tk.Label(text="Placa do Veículo")
label_placa_do_veiculo.grid(row=6,column=0,padx= 10,pady=10,sticky='nswe',columnspan=1)

#Box da PLACA DO VEÍCULO
entry_placa_do_veiculo = tk.Entry()
entry_placa_do_veiculo.grid(row=6,column=4,padx= 10,pady=10,sticky='nswe',columnspan=1)

#_______________________________________________________________________________________

#Texto da INDICAÇÃO DA NOTIF. AO ÓRGÃO
label_identificacao_da_notif_ao_orgao = tk.Label(text="Identificação da Notif. ao Órgão")
label_identificacao_da_notif_ao_orgao.grid(row=7,column=0,padx= 10,pady=10,sticky='nswe',columnspan=1)

#Box da INDICAÇÃO DA NOTIF. AO ÓRGÃO
combbox_identificacao_da_notif_ao_orgao = ttk.Combobox(values=lista_sim_nao)
combbox_identificacao_da_notif_ao_orgao.grid(row=7,column=4,padx= 10,pady=10,sticky='nswe',columnspan=1)

#_______________________________________________________________________________________

#Texto da TIPO DE INFRAÇÃO
label_tipo_infracao= tk.Label(text="Tipo de Infração")
label_tipo_infracao.grid(row=8,column=0,padx= 10,pady=10,sticky='nswe',columnspan=1)

#Box da TIPO DE INFRAÇÃO
combbox_tipo_infracao = ttk.Combobox(values=lista_tipo_infracao)
combbox_tipo_infracao.grid(row=8,column=1,padx= 10,pady=10,sticky='nswe',columnspan=39)

#_______________________________________________________________________________________

#Texto da PONTOS
label_pontos= tk.Label(text="Pontos")
label_pontos.grid(row=1,column=10,padx= 10,pady=10,sticky='nswe',columnspan=10)

#Box da PONTOS
entry_pontos = tk.Entry()
entry_pontos.grid(row=1,column=20,padx= 10,pady=10,sticky='nswe',columnspan=20)

#_______________________________________________________________________________________

#Texto da VALOR TOTAL DA MULTA R$
label_valor_total_multa = tk.Label(text="Valor Total da Multa R$")
label_valor_total_multa.grid(row=2,column=10,padx= 10,pady=10,sticky='nswe',columnspan=10)

#Box da PONTOS
entry_valor_total_multa = tk.Entry()
entry_valor_total_multa.grid(row=2,column=20,padx= 10,pady=10,sticky='nswe',columnspan=20)

#_______________________________________________________________________________________

#Texto da VALOR COM DESCONTO R$
label_valor_desconto = tk.Label(text="Valor com Desconto R$")
label_valor_desconto.grid(row=3,column=10,padx= 10,pady=10,sticky='nswe',columnspan=10)

#Box da PONTOS
entry_valor_desconto = tk.Entry()
entry_valor_desconto.grid(row=3,column=20,padx= 10,pady=10,sticky='nswe',columnspan=20)

#_______________________________________________________________________________________

#Texto da EMPRESA
label_empresa= tk.Label(text="Empresa")
label_empresa.grid(row=4,column=10,padx= 10,pady=10,sticky='nswe',columnspan=10)

#Box da EMPRESA
combbox_empresa = ttk.Combobox(values=lista_empresa)
combbox_empresa.grid(row=4,column=20,padx= 10,pady=10,sticky='nswe',columnspan=20)

#_______________________________________________________________________________________

#Texto da UNIDADE
label_unidade= tk.Label(text="Unidades")
label_unidade.grid(row=5,column=10,padx= 10,pady=10,sticky='nswe',columnspan=10)

#Box da UNIDADE
combbox_unidade = ttk.Combobox(values=lista_unidades)
combbox_unidade.grid(row=5,column=20,padx= 10,pady=10,sticky='nswe',columnspan=20)

#_______________________________________________________________________________________

#Texto da CENTRO DE CUSTO
label_CC= tk.Label(text="Centro de Custo")
label_CC.grid(row=6,column=10,padx= 10,pady=10,sticky='nswe',columnspan=10)

#Box da CENTRO DE CUSTO
combbox_CC = ttk.Combobox(values=lista_CC)
combbox_CC.grid(row=6,column=20,padx= 10,pady=10,sticky='nswe',columnspan=20)

#_______________________________________________________________________________________

#Texto da MOTORISTAS
label_motorista= tk.Label(text="Motorista")
label_motorista.grid(row=6,column=10,padx= 10,pady=10,sticky='nswe',columnspan=10)

#Box da MOTORISTAS
combbox_motorista = ttk.Combobox(values=lista_CC)
combbox_motorista.grid(row=6,column=20,padx= 10,pady=10,sticky='nswe',columnspan=20)

#_______________________________________________________________________________________

#Texto da ENVIADO PARA DESCONTO
label_enviado_desconto= tk.Label(text="Enviado para Desconto")
label_enviado_desconto.grid(row=7,column=10,padx= 10,pady=10,sticky='nswe',columnspan=10)

#Box da ENVIADO PARA DESCONTO
combbox_enviado_desconto = ttk.Combobox(values=lista_sim_nao)
combbox_enviado_desconto.grid(row=7,column=20,padx= 10,pady=10,sticky='nswe',columnspan=20)

#_______________________________________________________________________________________

#Texto da RESPONSÁVEL QUE LANÇOU
label_responsavel_lancou= tk.Label(text="Responsável que Lançou")
label_responsavel_lancou.grid(row=1,column=40,padx= 10,pady=10,sticky='nswe',columnspan=10)

#Box da RESPONSÁVEL QUE LANÇOU
entry_responsavel_lancou = tk.Entry()
entry_responsavel_lancou.grid(row=1,column=50,padx= 10,pady=10,sticky='nswe',columnspan=20)

#_______________________________________________________________________________________

#Texto da OBSERVAÇÃO
label_observacao= tk.Label(text="Observação")
label_observacao.grid(row=2,column=40,padx= 10,pady=10,sticky='nswe',columnspan=5)

#Box da OBSERVAÇÃO
entry_observacao = tk.Entry()
entry_observacao.grid(row=2,column=45,padx= 10,pady=10,sticky='nswe',columnspan=30)

#_______________________________________________________________________________________

#Botão SALVAR MULTA

botao_salvar_multa = tk.Button(text="Salvar Multa")
botao_salvar_multa.grid(row=4,column=40,padx= 10,pady=10,sticky='nswe',columnspan=30)

#_______________________________________________________________________________________

#Botão CANCELAR MULTA

botao_cancelar_multa = tk.Button(text="Cancelar Multa")
botao_cancelar_multa.grid(row=5,column=40,padx= 10,pady=10,sticky='nswe',columnspan=30)

#_______________________________________________________________________________________

#Botão IMPORTAR

botao_abrir_bc = tk.Button(text="Abrir Banco de Dados")
botao_abrir_bc.grid(row=6,column=40,padx= 10,pady=10,sticky='nswe',columnspan=30)


#_______________________________________________________________________________________

#Botão IMPORTAR

botao_abrir_relatorio = tk.Button(text="Abrir Relatório")
botao_abrir_relatorio.grid(row=7,column=40,padx= 10,pady=10,sticky='nswe',columnspan=30)










janela.mainloop()