library(ggplot2)

#Load and format data

data  <- read.table("PredatorPreyAlphaGammaChi-find_cyles-means.csv", sep=",", header = T)

#Histogram of averages

pdfFile <-c("PredatorPreyAlphaGammaChi-Hist.pdf")
pdf(pdfFile)
a <- ggplot(data, aes(x=meansteps)) + geom_histogram(binwidth=10)
a
dev.off()

#Scatterplot average by alpha and gamma
library(scatterplot3d)

pdfFile <-c("PredatorPreyAlphaGammaChi-3dplotAG.pdf")
pdf(pdfFile)
with(data, {
  scatterplot3d(alpha,   # x axis
                gamma,     # y axis
                meansteps,    # z axis
                pch=19,
                highlight.3d=TRUE,
                main="Average number of steps by alpha and gamma")
})
dev.off()