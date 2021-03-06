library(tidyverse)
library(stargazer)

df <- read_csv("Apoio_p_18_COVID19_/dataset_final.csv")

#Rela��o entre vari�veis chave
ggplot(aes(x=log_renda,y=ipvs),data=df) + geom_point()
cor(df$log_renda,df$ipvs)

ggplot(aes(x=Distrito,y=sort(log_renda)),data=df) + geom_point()
ggplot(aes(x=Distrito,y=sort(ipvs)),data=df) + geom_point()

#1� Modelo
#THRESHOLD = 60_anos
df_ricos <- df %>%
    filter(log_renda >= 8.305727)
#n = 48
#Bem robusto com rela��o a altera��es no limite do ipvs, testando no limite
#com zero toler�ncia no ipvs ainda retorna resultados significativos
df_ricos_ig <- df_ricos%>%
  filter(ipvs <= 14.5)

#ggplot(aes(x=log_renda,y=ipvs),data=df_ricos_ig) + geom_point()

df_2 <- df %>%
  filter(log_renda < 8.305727)
df_main <- rbind(df_2,df_ricos_ig)

#ggplot(aes(x=log_renda,y=ipvs),data=df_main) + geom_point()

df_main['excedente_60'] <- df_main %>%
  select(excedente_mortes_0_9,excedente_mortes_10_19,excedente_mortes_20_29,
         excedente_mortes_30_39,excedente_mortes_40_49,excedente_mortes_50_59) %>%
  rowSums()

df_main['pop_total_60'] <- df_main %>%
  select(populacao_2017_total_00_09_anos,populacao_2017_total_10_19_anos,
         populacao_2017_total_20_29_anos,populacao_2017_total_30_39_anos,
         populacao_2017_total_40_49_anos,populacao_2017_total_50_59_anos) %>%
  rowSums()

df_main['excedente_60_cap'] <- (df_main['excedente_60'] / df_main['pop_total_60'])*100000

model_m1 <- lm(excedente_t ~ votos_2018_Bolsonaro_1_percentual, data = df_main)
model_m2 <- lm(excedente_t ~ votos_2018_Bolsonaro_1_percentual + log_renda, data = df_main)
model_m3 <- lm(excedente_t ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df_main)

stargazer(model_m1,model_m2,model_m3,
          dep.var.caption = "Vari�vel dependente",
          dep.var.labels = "Excedente de mortos em 2021",
          covariate.labels = c("Votos no Bolsonaro (em %)","Log da Renda","IPVS","Constante"),
          notes.label = "N�veis de signific�ncia",
          title = 'Regress�es',out = "Apoio_p_18_COVID19_/regressoes.tex")

#1-B� Modelo
#THRESHOLD = 50_anos
df_ricos <- df %>%
  filter(log_renda >= 8.305727)
#n = 48
#Bem robusto com rela��o a altera��es no limite do ipvs, testando no limite
#com zero toler�ncia no ipvs ainda retorna resultados significativos
df_ricos_ig <- df_ricos%>%
  filter(ipvs <= 14.5)

#ggplot(aes(x=log_renda,y=ipvs),data=df_ricos_ig) + geom_point()

df_2 <- df %>%
  filter(log_renda < 8.305727)
df_main <- rbind(df_2,df_ricos_ig)

#ggplot(aes(x=log_renda,y=ipvs),data=df_main) + geom_point()

df_main['excedente_50'] <- df_main %>%
  select(excedente_mortes_0_9,excedente_mortes_10_19,excedente_mortes_20_29,
         excedente_mortes_30_39,excedente_mortes_40_49) %>%
  rowSums()

df_main['pop_total_50'] <- df_main %>%
  select(populacao_2017_total_00_09_anos,populacao_2017_total_10_19_anos,
         populacao_2017_total_20_29_anos,populacao_2017_total_30_39_anos,
         populacao_2017_total_40_49_anos) %>%
  rowSums()

df_main['excedente_50_cap'] <- (df_main['excedente_50'] / df_main['pop_total_50'])*100000

model_m1 <- lm(excedente_t ~ votos_2018_Bolsonaro_1_percentual, data = df_main)
model_m2 <- lm(excedente_t ~ votos_2018_Bolsonaro_1_percentual + log_renda, data = df_main)
model_m3 <- lm(excedente_t ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df_main)

stargazer(model_m1,model_m2,model_m3,
          dep.var.caption = "Vari�vel dependente",
          dep.var.labels = "Excedente de mortos em 2021",
          covariate.labels = c("Votos no Bolsonaro (em %)","Log da Renda","IPVS","Constante"),
          notes.label = "N�veis de signific�ncia",
          title = 'Regress�es',out = "Apoio_p_18_COVID19_/regressoes_2.tex")

#Qui�� modelo mais interessante, pq?
#A - Consideramos s� pessoas eleg�veis ao voto em 2018, com uma probabilidade maior 
#de serem influenciadas pelo discurso do Bolsonaro
#B - Ajustado pela desigualdade (via % de ipvs)
#1-C� Modelo
#THRESHOLD = 20_60_anos
df_ricos <- df %>%
  filter(log_renda >= 8.305727)
#n = 48
#Bem robusto com rela��o a altera��es no limite do ipvs, testando no limite
#com zero toler�ncia no ipvs ainda retorna resultados significativos
df_ricos_ig <- df_ricos%>%
  filter(ipvs <= 14.5) #Mostrar com ipvs <= 5 e ipvs = 0

#ggplot(aes(x=log_renda,y=ipvs),data=df_ricos_ig) + geom_point()

df_2 <- df %>%
  filter(log_renda < 8.305727)
df_main <- rbind(df_2,df_ricos_ig)

#ggplot(aes(x=log_renda,y=ipvs),data=df_main) + geom_point()

df_main['excedente_60_votante'] <- df_main %>%
  select(excedente_mortes_20_29,
         excedente_mortes_30_39,excedente_mortes_40_49,excedente_mortes_50_59) %>%
  rowSums()

df_main['pop_total_60_votante'] <- df_main %>%
  select(
         populacao_2017_total_20_29_anos,populacao_2017_total_30_39_anos,
         populacao_2017_total_40_49_anos,populacao_2017_total_50_59_anos) %>%
  rowSums()

df_main['excedente_60_votante'] <- (df_main['excedente_60_votante'] / df_main['pop_total_60_votante'])*100000

model_m1 <- lm(excedente_t ~ votos_2018_Bolsonaro_1_percentual, data = df_main)
model_m2 <- lm(excedente_t ~ votos_2018_Bolsonaro_1_percentual + log_renda, data = df_main)
model_m3 <- lm(excedente_t ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df_main)

stargazer(model_m1,model_m2,model_m3,
          dep.var.caption = "Vari�vel dependente",
          dep.var.labels = "Excedente de mortos em 2021",
          covariate.labels = c("Votos no Bolsonaro no 1� Turno (em %)","Log da Renda","IPVS","Constante"),
          notes.label = "N�veis de signific�ncia",
          title = 'Regress�o 3',out = "Apoio_p_18_COVID19_/regressoes_3.tex")

model_m1 <- lm(excedente_50_cap ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df_main)
model_m2<- lm(excedente_60_cap ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df_main)
model_m3 <- lm(excedente_60_votante ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df_main)

stargazer(model_m1, model_m2, model_m3,
          dep.var.caption = "Excedente de mortos em 2021",
          dep.var.labels = c('0-50 anos','0-60 anos','20-60 anos'),
          covariate.labels = c("Votos no Bolsonaro no 1� Turno (em %)","Log da Renda","IPVS","Constante"),
          notes.label = "N�veis de signific�ncia",
          title = 'Regress�o 17',out = "Apoio_p_18_COVID19_/regressoes_17.tex")

model1 <- lm(excedente_50_cap ~ votos_2018_Bolsonaro_1_percentual, data = df_main)
model2 <- lm(excedente_50_cap ~ votos_2018_Bolsonaro_1_percentual + log_renda, data = df_main)
model3 <- lm(excedente_50_cap ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df_main)
model4 <- lm(excedente_60_cap ~ votos_2018_Bolsonaro_1_percentual, data = df_main)
model5 <- lm(excedente_60_cap ~ votos_2018_Bolsonaro_1_percentual + log_renda, data = df_main)
model6 <- lm(excedente_60_cap~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df_main)
model7 <- lm(excedente_60_votante ~ votos_2018_Bolsonaro_1_percentual, data = df_main)
model8 <- lm(excedente_60_votante ~ votos_2018_Bolsonaro_1_percentual + log_renda, data = df_main)
model9 <- lm(excedente_60_votante~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df_main)

stargazer(model1,model2,model3,model4,model5,model6,model7,model8,model9,
          dep.var.caption = "Excedente de mortos em 2021",
          dep.var.labels = c('0-50 anos','0-60 anos','20-60 anos',
                             '0-50 anos','0-60 anos','20-60 anos',
                             '0-50 anos','0-60 anos','20-60 anos'),
          covariate.labels = c("Votos no Bolsonaro no 1� Turno (em %)","Log da Renda","IPVS","Constante"),
          notes.label = "N�veis de signific�ncia",
          title = 'Regress�o 1',out = "Apoio_p_18_COVID19_/regressoes_main_1.tex")

#Regress�o com todos os distritos
model1 <- lm(excedente_50_cap ~ votos_2018_Bolsonaro_1_percentual, data = df)
model2 <- lm(excedente_50_cap ~ votos_2018_Bolsonaro_1_percentual + log_renda, data = df)
model3 <- lm(excedente_50_cap ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df)
model4 <- lm(excedente_60_cap ~ votos_2018_Bolsonaro_1_percentual, data = df)
model5 <- lm(excedente_60_cap ~ votos_2018_Bolsonaro_1_percentual + log_renda, data = df)
model6 <- lm(excedente_60_cap~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df)
model7 <- lm(excedente_20_60_cap ~ votos_2018_Bolsonaro_1_percentual, data = df)
model8 <- lm(excedente_20_60_cap ~ votos_2018_Bolsonaro_1_percentual + log_renda, data = df)
model9 <- lm(excedente_20_60_cap ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df)

stargazer(model1,model2,model3,model4,model5,model6,model7,model8,model9,
          dep.var.caption = "Excedente de mortos em 2021",
          dep.var.labels = c('0-50 anos','0-60 anos','20-60 anos',
                             '0-50 anos','0-60 anos','20-60 anos',
                             '0-50 anos','0-60 anos','20-60 anos'),
          covariate.labels = c("Votos no Bolsonaro no 1� Turno (em %)","Log da Renda","IPVS","Constante"),
          notes.label = "N�veis de signific�ncia",
          title = 'Regress�o 1',out = "Apoio_p_18_COVID19_/regressoes_main_4.tex")

#4� Modelo
#THRESHOLD = 60_anos
df['excedente_60'] <- df %>%
  select(excedente_mortes_0_9,excedente_mortes_10_19,excedente_mortes_20_29,
         excedente_mortes_30_39,excedente_mortes_40_49,excedente_mortes_50_59) %>%
  rowSums()

df['pop_total_60'] <- df %>%
  select(populacao_2017_total_00_09_anos,populacao_2017_total_10_19_anos,
         populacao_2017_total_20_29_anos,populacao_2017_total_30_39_anos,
         populacao_2017_total_40_49_anos,populacao_2017_total_50_59_anos) %>%
  rowSums()

df['excedente_60_cap'] <- (df['excedente_60'] / df['pop_total_60'])*100000

model_m1 <- lm(excedente_t ~ votos_2018_Bolsonaro_1_percentual, data = df)
model_m2 <- lm(excedente_t ~ votos_2018_Bolsonaro_1_percentual + log_renda, data = df)
model_m3 <- lm(excedente_t ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df)

stargazer(model_m1,model_m2,model_m3,
          dep.var.caption = "Vari�vel dependente",
          dep.var.labels = "Excedente de mortos em 2021",
          covariate.labels = c("Votos no Bolsonaro (em %)","Log da Renda","IPVS","Constante"),
          notes.label = "N�veis de signific�ncia",
          title = 'Regress�o 4',out = "Apoio_p_18_COVID19_/regressoes_4.tex")

#5� Modelo
#THRESHOLD = 50_anos
df['excedente_50'] <- df %>%
  select(excedente_mortes_0_9,excedente_mortes_10_19,excedente_mortes_20_29,
         excedente_mortes_30_39,excedente_mortes_40_49) %>%
  rowSums()

df['pop_total_50'] <- df %>%
  select(populacao_2017_total_00_09_anos,populacao_2017_total_10_19_anos,
         populacao_2017_total_20_29_anos,populacao_2017_total_30_39_anos,
         populacao_2017_total_40_49_anos) %>%
  rowSums()

df['excedente_50_cap'] <- (df['excedente_50'] / df['pop_total_50'])*100000

model_m1 <- lm(excedente_t ~ votos_2018_Bolsonaro_1_percentual, data = df)
model_m2 <- lm(excedente_t ~ votos_2018_Bolsonaro_1_percentual + log_renda, data = df)
model_m3 <- lm(excedente_t ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df)

stargazer(model_m1,model_m2,model_m3,
          dep.var.caption = "Vari�vel dependente",
          dep.var.labels = "Excedente de mortos em 2021",
          covariate.labels = c("Votos no Bolsonaro no 1� Turno (em %)","Log da Renda","IPVS","Constante"),
          notes.label = "N�veis de signific�ncia",
          title = 'Regress�o 5',out = "Apoio_p_18_COVID19_/regressoes_5.tex")

#6� Modelo
#THRESHOLD = 20_60_anos
df['excedente_20_60'] <- df %>%
  select(excedente_mortes_20_29,
         excedente_mortes_30_39,excedente_mortes_40_49,excedente_mortes_50_59) %>%
  rowSums()

df['pop_total_20_60'] <- df %>%
  select(
         populacao_2017_total_20_29_anos,populacao_2017_total_30_39_anos,
         populacao_2017_total_40_49_anos,populacao_2017_total_50_59_anos) %>%
  rowSums()

df['excedente_20_60_cap'] <- (df['excedente_20_60'] / df['pop_total_20_60'])*100000

model_m1 <- lm(excedente_t ~ votos_2018_Bolsonaro_1_percentual, data = df)
model_m2 <- lm(excedente_t ~ votos_2018_Bolsonaro_1_percentual + log_renda, data = df)
model_m3 <- lm(excedente_t ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df)

stargazer(model_m1,model_m2,model_m3,
          dep.var.caption = "Vari�vel dependente",
          dep.var.labels = "Excedente de mortos em 2021",
          covariate.labels = c("Votos no Bolsonaro no 1� Turno (em %)","Log da Renda","IPVS","Constante"),
          notes.label = "N�veis de signific�ncia",
          title = 'Regress�o 6',out = "Apoio_p_18_COVID19_/regressoes_6.tex")

model_m1 <- lm(excedente_50_cap ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df)
model_m2<- lm(excedente_60_cap ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df)
model_m3 <- lm(excedente_20_60_cap ~ votos_2018_Bolsonaro_1_percentual + log_renda + ipvs, data = df)

stargazer(model_m1, model_m2, model_m3,
          dep.var.caption = "Excedente de mortos em 2021",
          dep.var.labels = c('0-50 anos','0-60 anos','20-60 anos'),
          covariate.labels = c("Votos no Bolsonaro no 1� Turno (em %)","Log da Renda","IPVS","Constante"),
          notes.label = "N�veis de signific�ncia",
          title = 'Regress�o 18',out = "Apoio_p_18_COVID19_/regressoes_18.tex")



#2� Modelo
#THRESHOLD = 60_anos
df_ricos <- df %>%
  filter(renda >= 5259.31)
#n = 28
df_ricos_ig <- df_ricos%>%
  filter(ipvs <= 14.5)

ggplot(aes(x=log_renda,y=ipvs),data=df_ricos_ig) + geom_point()

df_2 <- df %>%
  filter(renda < 5259.31)
df_main <- rbind(df_2,df_ricos_ig)

ggplot(aes(x=log_renda,y=ipvs),data=df_main) + geom_point()

df_main['excedente_60'] <- df_main %>%
  select(excedente_mortes_0_9,excedente_mortes_10_19,excedente_mortes_20_29,
         excedente_mortes_30_39,excedente_mortes_40_49,excedente_mortes_50_59) %>%
  rowSums()

df_main['pop_total_60'] <- df_main %>%
  select(populacao_2020_total_00_09_anos,populacao_2020_total_10_19_anos,
         populacao_2020_total_20_29_anos,populacao_2020_total_30_39_anos,
         populacao_2020_total_40_49_anos,populacao_2020_total_50_59_anos) %>%
  rowSums()

df_main['excedente_t'] <- (df_main['excedente_60'] / df_main['pop_total_60'])*100000

model_m1 <- lm(excedente_t ~ Votos_1, data = df_main)
model_m2 <- lm(excedente_t ~ Votos_1 + log_renda, data = df_main)
model_m3 <- lm(excedente_t ~ Votos_1 + log_renda + ipvs, data = df_main)

#3� Modelo
#THRESHOLD = 60_anos
df_ricos <- df %>%
  filter(renda >= 5665.66)
#n = 28
df_ricos_ig <- df_ricos%>%
  filter(ipvs <= 14.5)

ggplot(aes(x=log_renda,y=ipvs),data=df_ricos_ig) + geom_point()

df_2 <- df %>%
  filter(renda < 5665.66)
df_main <- rbind(df_2,df_ricos_ig)

ggplot(aes(x=log_renda,y=ipvs),data=df_main) + geom_point()

df_main['excedente_60'] <- df_main %>%
  select(excedente_mortes_0_9,excedente_mortes_10_19,excedente_mortes_20_29,
         excedente_mortes_30_39,excedente_mortes_40_49,excedente_mortes_50_59) %>%
  rowSums()

df_main['pop_total_60'] <- df_main %>%
  select(populacao_2020_total_00_09_anos,populacao_2020_total_10_19_anos,
         populacao_2020_total_20_29_anos,populacao_2020_total_30_39_anos,
         populacao_2020_total_40_49_anos,populacao_2020_total_50_59_anos) %>%
  rowSums()

df_main['excedente_t'] <- (df_main['excedente_60'] / df_main['pop_total_60'])*100000

model_m1 <- lm(excedente_t ~ Votos_1, data = df_main)
model_m2 <- lm(excedente_t ~ Votos_1 + log_renda, data = df_main)
model_m3 <- lm(excedente_t ~ Votos_1 + log_renda + ipvs, data = df_main)