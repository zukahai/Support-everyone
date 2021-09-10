########
#read data
#dataset in packages

data()

iris

d <- iris

dim(iris)

dim(d)

str(d)

#xem 6 dong dau
head(d)

#Xem ten
names(d)

Orange

#read data/ dataset on PC

d <- read.csv("D://dataset/OnlineRetail.csv")
dim(d)
str(d)
View(d)
edit(d)

d <- read.csv("D://dataset/OnlineRetail.csv", sep = ".", header = F)

d

d <- read.csv("D://dataset/adult.txt")
dim(d)

d <- read.csv("D://dataset/breast-cancer.txt", sep = ",", header = F)
dim(d)
d


#read data/dataset on interner

ad <- read.csv("http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv")
dim(ad)

d <- read.csv("https://www.kaggle.com/bumba5341/advertisingcsv?select=Advertising.csv")
dim(d)

education <- read.csv("https://vincentarelbundock.github.io/Rdatasets/csv/robustbase/education.csv", stringsAsFactors = FALSE)
dim(education)

data=read.table(file="http://www.sthda.com/upload/decathlon.txt", header=T, row.names=1, sep="\t")
dim(data)

#xoa cac bien da lua
rm(list=ls())

install.packages("dplyr")
library("dplyr")

install.packages("xlsx")
library("xlsx")
data <- read.xlsx("input.xlsx", sheetIndex = 1)
print(data)

#luu du lieu sau khi xu ly
write.csv(d, file = "D://dataset//my_data.csv")
