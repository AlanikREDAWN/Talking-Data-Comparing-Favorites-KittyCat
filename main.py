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
print(favMovie + " is rated " + str(47 - min) + " points higher than the lowest rated movie.")
print()

#find max
max = scienceFictionMovieData["audience_rating"].max()
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated " + str(max - 47) + " points lower than the highest rated movie.")
print()

#find mean
mean = scienceFictionMovieData["audience_rating"].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " is lower than the mean movie rating.")

#find median
median = scienceFictionMovieData["audience_rating"].median()
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " is lower than the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 6 Create graphs
#Create histogram
plt.hist(scienceFictionMovieData["audience_rating"], range = (0, 100), bins = 20)

#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Science Fiction Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Science Fiction Movies")

#Prints interpretation of histogram
print(
  "According to the histogram, there are less than 20 movies with the highest possible rating. Most of the movies are rated around less than 60. Most are the movies are rated somewhere in the upper to middle range, forming a very curved looking histogram"
)
print("Close the graph by pressing the 'X' in the top right corner.")
print()

#Show histogram
plt.show()

#Create scatterplot
plt.scatter(data = scienceFictionMovieData, x = "audience_rating", y = "critic_rating")

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Rating versus Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
print(
  "According to the scatter plot, there is a positive correlation. Their is a pattern going to the top right, however there are a few outliers, with the middle of the graph being a bit scattered, but concentrated in the middle."
)
print()

print("Close the graph by pressing the 'X' in the top right corner.")

#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")
