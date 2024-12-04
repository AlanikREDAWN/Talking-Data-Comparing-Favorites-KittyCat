#Part 2 Setting up the program
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "Captain Marvel"

print("My favorite movie is  " + favMovie)


#Part 3 Investigate the data
# print(movieData.head())
# print(movieData["movie_title"])


#Part 4 Filter data
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information
favMovieBooleanList = movieData["movie_title"] == favMovie
# print(favMovieBooleanList)

favMovieData = movieData.loc[favMovieBooleanList]
print(favMovieData)





print("\n\n")

#Create a new variable to store a new data set with a certain genre
scienceFictionMovieBooleanList = movieData["genres"].str.contains("Science Fiction")

scienceFictionMovieData = movieData.loc[scienceFictionMovieBooleanList]

numOfMovies = scienceFictionMovieData.shape[0]

print("We will be comparing " + favMovie +
      " to other movies under the genre Science Fiction in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Science Fiction.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

#Part 5 Describe data
#min
min = scienceFictionMovieData["audience_rating"].min()
print("The min audience rating of the data set is: " + str(min))
print(favMovie + " is rated" + (min - 47) + "points higher than the lowest rated movie.")
print()

#find max
max = scienceFictionMovieData["audience_rating"].max()
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated" + (max - 47) + "points lower than the highest rated movie.")
print()

#find mean
mean = 0
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " [is higher than/lower than/the same as] the mean movie rating.")

#find median
median = 0
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " [is higher than/lower than/the same as] the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 6 Create graphs
#Create histogram


#Adds labels and adjusts histogram
plt.grid(True)
plt.title("")
plt.xlabel("")
plt.ylabel("")

#Prints interpretation of histogram
print(
  "According to the histogram, ..."
)
print("Close the graph by pressing the 'X' in the top right corner.")
print()

#Show histogram
plt.show()

#Create scatterplot


#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("")
plt.xlabel("")
plt.ylabel("")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
print(
  "According to the scatter plot, ..."
)
print()

print("Close the graph by pressing the 'X' in the top right corner.")

#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")
