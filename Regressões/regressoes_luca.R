# analises.R

# Esse script:
# > 

###########################################################################

# Passo 0: Definir diretório e carregar bibliotecas

#rm(list = ls())

#setwd("C:/Users/lucam/OneDrive/Área de Trabalho/Economia/R/GEPE")

library(dplyr)
library(tidyr)
library(readr)
library(ggplot2)
library(stargazer)

options(scipen = 999) # disable scientific notation

###########################################################################
data = read.csv("Apoio_p_18_COVID19_/dataset_final.csv")
# Passo 1: 


###############################
#Regressões boas
data = data %>% mutate(populacao_50 =    populacao_2017_total_20_29_anos +
                         populacao_2017_total_30_39_anos +
                         populacao_2017_total_40_49_anos)

data = data %>% mutate(populacao_50criancas =  
                         populacao_50 + 
                         populacao_2017_total_10_19_anos+
                         populacao_2017_total_00_09_anos)

data = data %>% mutate(populacao_60 = populacao_50 +
                         populacao_2017_total_50_59_anos)

data = data %>% mutate(populacao_60criancas = 
                         populacao_50criancas+
                         populacao_2017_total_50_59_anos)


data = data %>% mutate(mortes_21covid_50 = obitos_2021_COVID_30_39 +
                                               obitos_2021_COVID_40_49 +
                                               obitos_2021_COVID_20_29)
                                              


data = data %>% mutate(mortes_21covid_50_cap = mortes_21covid_50 / 
                                                   populacao_50 * 100000)

data = data %>% mutate(mortes_21covid_60 = mortes_21covid_50 +
                                               obitos_2021_COVID_50_59)

data = data %>% mutate(mortes_21covid_60_cap = mortes_21covid_60 / 
                         populacao_60 * 100000)


data = data %>% mutate(mortes_21covid_50_cri = mortes_21covid_50 +
                         obitos_2021_COVID_10_19+
                         obitos_2021_COVID_0_9)

data = data %>% mutate(mortes_21covid_60_cri = mortes_21covid_50_cri+
                         obitos_2020_COVID_50_59)

data = data %>% mutate(mortes_21covid_60_cap_cri = mortes_21covid_60_cri / 
                         populacao_60criancas * 100000)

data = data %>% mutate(mortes_21covid_50_cap_cri = mortes_21covid_50_cri/ 
                         populacao_50criancas * 100000)

df_ricos <- data %>%
  filter(log_renda >= 8.305727)
df_ricos_ig <- df_ricos %>%
  filter(ipvs <= 14.5)
df_2 <- data %>%
  filter(log_renda < 8.305727)
df_main <- rbind(df_2,df_ricos_ig)

model1 = lm(mortes_21covid_50_cap ~ votos_2018_Bolsonaro_1_percentual, data = df_main)
model2 = lm(mortes_21covid_50_cap ~ votos_2018_Bolsonaro_1_percentual + log_renda, data = df_main)
#model3 = lm(mortes_21covid_50_cap ~ votos_2018_Bolsonaro_1_percentual + ipvs, data = data)
model4 = lm(mortes_21covid_50_cap ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df_main)

stargazer(model1,model2,model4,
          dep.var.caption = "Variável dependente",
          dep.var.labels = "Mortes de COVID (per capita) em 2021",
          covariate.labels = c("Votos no Bolsonaro no 1º Turno (em %)","Log da Renda","IPVS","Constante"),
          notes.label = "Níveis de significância",
          title = 'Regressão 12',out = "Apoio_p_18_COVID19_/regressoes_12.tex")

model1 = lm(mortes_21covid_60_cap ~ votos_2018_Bolsonaro_1_percentual, data = df_main)
model2 = lm(mortes_21covid_60_cap ~ votos_2018_Bolsonaro_1_percentual + log_renda, data = df_main)
#model3 = lm(mortes_21covid_60_cap ~ votos_2018_Bolsonaro_1_percentual + ipvs, data = data)
model4 = lm(mortes_21covid_60_cap ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df_main)

stargazer(model1,model2,model4,
          dep.var.caption = "Variável dependente",
          dep.var.labels = "Mortes de COVID (per capita) em 2021",
          covariate.labels = c("Votos no Bolsonaro no 1º Turno (em %)","Log da Renda","IPVS","Constante"),
          notes.label = "Níveis de significância",
          title = 'Regressão 13',out = "Apoio_p_18_COVID19_/regressoes_13.tex")

model1 = lm(mortes_21covid_50_cap_cri ~ votos_2018_Bolsonaro_1_percentual, data = df_main)
model2 = lm(mortes_21covid_50_cap_cri ~ votos_2018_Bolsonaro_1_percentual + log_renda, data = df_main)
#model3 = lm(mortes_21covid_50_cap_cri ~ votos_2018_Bolsonaro_1_percentual + ipvs, data = data)
model4 = lm(mortes_21covid_50_cap_cri ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df_main)

stargazer(model1,model2,model4,
          dep.var.caption = "Variável dependente",
          dep.var.labels = "Mortes de COVID (per capita) em 2021",
          covariate.labels = c("Votos no Bolsonaro no 1º Turno (em %)","Log da Renda","IPVS","Constante"),
          notes.label = "Níveis de significância",
          title = 'Regressão 14',out = "Apoio_p_18_COVID19_/regressoes_14.tex")

model1 = lm(mortes_21covid_60_cap_cri ~ votos_2018_Bolsonaro_1_percentual, data = df_main)
model2 = lm(mortes_21covid_60_cap_cri ~ votos_2018_Bolsonaro_1_percentual + log_renda, data = df_main)
#model3 = lm(mortes_21covid_60_cap_cri ~ votos_2018_Bolsonaro_1_percentual + ipvs, data = data)
model4 = lm(mortes_21covid_60_cap_cri ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df_main)

stargazer(model1,model2,model4,
          dep.var.caption = "Variável dependente",
          dep.var.labels = "Mortes de COVID (per capita) em 2021",
          covariate.labels = c("Votos no Bolsonaro no 1º Turno (em %)","Log da Renda","IPVS","Constante"),
          notes.label = "Níveis de significância",
          title = 'Regressão 15',out = "Apoio_p_18_COVID19_/regressoes_15.tex")

model1 = lm(mortes_21covid_50_cap_cri ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = data)
model2 = lm(mortes_21covid_60_cap_cri ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = data)
model3 = lm(mortes_21covid_50_cap ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = data)
model4 = lm(mortes_21covid_60_cap ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = data)

stargazer(model1, model2, model3,model4,
          dep.var.caption = "Mortes de COVID (per capita) em 2021",
          dep.var.labels = c('0-50 anos','0-60 anos','20-50 anos','20-60 anos'),
          covariate.labels = c("Votos no Bolsonaro no 1º Turno (em %)","Log da Renda","IPVS","Constante"),
          notes.label = "Níveis de significância",
          title = 'Regressão 19',out = "Apoio_p_18_COVID19_/regressoes_19.tex")

model1 = lm(mortes_21covid_50_cap_cri ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df_main)
model2 = lm(mortes_21covid_60_cap_cri ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df_main)
model3 = lm(mortes_21covid_50_cap ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df_main)
model4 = lm(mortes_21covid_60_cap ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df_main)

stargazer(model1, model2, model3,model4,
          dep.var.caption = "Mortes de COVID (per capita) em 2021",
          dep.var.labels = c('0-50 anos','0-60 anos','20-50 anos','20-60 anos'),
          covariate.labels = c("Votos no Bolsonaro no 1º Turno (em %)","Log da Renda","IPVS","Constante"),
          notes.label = "Níveis de significância",
          title = 'Regressão 20',out = "Apoio_p_18_COVID19_/regressoes_20.tex")


data = data %>% mutate(excedente_50 = excedente_mortes_20_29+
                                      excedente_mortes_30_39+
                                      excedente_mortes_40_49)


data = data %>% mutate(excedente_50_cri = excedente_50+
                         excedente_mortes_10_19+
                         excedente_mortes_0_9)
                         
data = data %>% mutate(excedente_50cap = excedente_50 /populacao_50
                       * 100000)

data = data %>% mutate(excedente_50cap_cri = excedente_50_cri /populacao_50criancas
                       * 100000)

model1 = lm(excedente_50cap ~ votos_2018_Bolsonaro_1_percentual, data = data)
model2 = lm(excedente_50cap ~ votos_2018_Bolsonaro_1_percentual + log_renda, data = data)
model3 = lm(excedente_50cap ~ votos_2018_Bolsonaro_1_percentual + ipvs, data = data)
model4 = lm(excedente_50cap~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = data)

stargazer(model1, model2, model3, model4, type = "text")

model1 = lm(excedente_50cap_cri ~ votos_2018_Bolsonaro_1_percentual, data = data)
model2 = lm(excedente_50cap_cri ~ votos_2018_Bolsonaro_1_percentual + log_renda, data = data)
model3 = lm(excedente_50cap_cri ~ votos_2018_Bolsonaro_1_percentual + ipvs, data = data)
model4 = lm(excedente_50cap_cri~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = data)

stargazer(model1, model2, model3, model4, type = "text")




data = data %>% mutate(excedente_50_cri = excedente_50+
                         excedente_mortes_10_19+
                         excedente_mortes_0_9)



data = data %>% mutate(excedente_60_cri = excedente_50_cri +
                         excedente_mortes_50_59)

data = data %>% mutate(excedente_60 = excedente_50 +
                         excedente_mortes_50_59)

data = data %>% mutate(excedente_60cap_cri = excedente_60_cri /populacao_60criancas
                       * 100000)

data = data %>% mutate(excedente_60cap= excedente_60 /populacao_60
                       * 100000)


model1 = lm(excedente_60cap ~ votos_2018_Bolsonaro_1_percentual, data = data)
model2 = lm(excedente_60cap ~ votos_2018_Bolsonaro_1_percentual + log_renda, data = data)
model3 = lm(excedente_60cap ~ votos_2018_Bolsonaro_1_percentual + ipvs, data = data)
model4 = lm(excedente_60cap~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = data)

stargazer(model1, model2, model3, model4, type = "text")

model1 = lm(excedente_60cap_cri ~ votos_2018_Bolsonaro_1_percentual, data = data)
model2 = lm(excedente_60cap_cri ~ votos_2018_Bolsonaro_1_percentual + log_renda, data = data)
model3 = lm(excedente_60cap_cri ~ votos_2018_Bolsonaro_1_percentual + ipvs, data = data)
model4 = lm(excedente_60cap_cri~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = data)

stargazer(model1, model2, model3, model4, type = "text")
##
data = data %>% mutate(obitos2020 = obitos_2020_COVID_0_9+
                         obitos_2020_COVID_10_19+
                         obitos_2020_COVID_20_29+
                         obitos_2020_COVID_30_39+
                         obitos_2020_COVID_40_49+
                         obitos_2020_COVID_50_59+
                         obitos_2020_COVID_60_69+
                         obitos_2020_COVID_70_inf) 


data = data %>% mutate(obitos2021 = obitos_2021_COVID_0_9+
                         obitos_2021_COVID_10_19+
                         obitos_2021_COVID_20_29+
                         obitos_2021_COVID_30_39+
                         obitos_2021_COVID_40_49+
                         obitos_2021_COVID_50_59+
                         obitos_2021_COVID_60_69+
                         obitos_2021_COVID_70_inf) 

data = data %>% mutate(segunda_onda = obitos2021/obitos2020)

df_ricos <- data %>%
  filter(log_renda >= 8.305727)
df_ricos_ig <- df_ricos %>%
  filter(ipvs <= 14.5)
df_2 <- data %>%
  filter(log_renda < 8.305727)
df_main <- rbind(df_2,df_ricos_ig)

model1 = lm(segunda_onda ~ votos_2018_Bolsonaro_1_percentual, data = df_main)
model2 = lm(segunda_onda ~ votos_2018_Bolsonaro_1_percentual + log_renda, data = df_main)
#model3 = lm(segunda_onda ~ votos_2018_Bolsonaro_1_percentual + ipvs, data = data)
model4 = lm(segunda_onda~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df_main)

stargazer(model1,model2,model4,
          dep.var.caption = "Variável dependente",
          dep.var.labels = "Segunda onda (2021)",
          covariate.labels = c("Votos no Bolsonaro no 1º Turno (em %)","Log da Renda","IPVS","Constante"),
          notes.label = "Níveis de significância",
          title = 'Regressão 16',out = "Apoio_p_18_COVID19_/regressoes_16.tex")
