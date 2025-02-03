# This lab introduces you to plotting in R with ggplot and GGally. GGally is an extension of ggplot2.

library(datasets)
data("iris")

library(GGally)
ggpairs(iris, mapping=ggplot2::aes(colour=Species))