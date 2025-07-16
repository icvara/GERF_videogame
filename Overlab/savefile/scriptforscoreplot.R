#analyse score

data <- read.delim("C:\\Users\\Administrator\\Desktop\\GERF_videogame\\GERF_version\\savefile\\save_score.txt",header=F,sep=":")


View(data)


names(data) <- c("names","score")


library("ggplot2")


nrow(data)

p1 <-  ggplot(data,aes(x=data$score)) + geom_bar(fill="#009999") + theme_classic()  + xlab("Score") 
p1

ggsave("score.pdf",path="C:\\Users\\Administrator\\Desktop\\GERF_videogame\\GERF_version\\savefile\\")


p1 <-  ggplot(data,aes(y=data$score)) + geom_boxplot(fill="#009999") + theme_classic()  + xlab("Score")
p1