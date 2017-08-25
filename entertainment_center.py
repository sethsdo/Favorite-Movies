import media
import fresh_tomatoes

'''
This var = madia.Movie and atributes the information 
to the different ojects to the fuction media.Movie.
'''
toy_story = media.Movie("Toy Story", 
	"A story of a boy and his toys that came to life",
	"http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

'''
This var = madia.Movie and atributes the information 
to the different ojects to the fuction media.Movie.
'''
avatar = media.Movie("Avatar", 
	"A marine on an alien planet",
	"http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp", #noqu
	"www.youtube.com/watch?v=8KAtG68bIUc")

'''
This var = madia.Movie and atributes the information 
to the different ojects to the fuction media.Movie.
'''
finding_nemo = media.Movie("Finding Nemo", 
	"A fish who lost his son and tries to find him.",
	"https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
	"https://www.youtube.com/watch?v=wZdpNglLbt8")

'''
This var = madia.Movie and atributes the information 
to the different ojects to the fuction media.Movie.
'''
zootopia = media.Movie("Zootopia", 
	"A bunny whose dream it is to become a Police Officer",
	"https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
	"www.youtube.com/watch?v=WWFB-zrxn7o")

'''
This var = madia.Movie and atributes the information 
to the different ojects to the fuction media.Movie.
'''
harry_potter_and_the_prisoner_of_azkaban = media.Movie("Harry Potter and the Prisoner of Azkaban", 
	"The third movie in the Harry Potter set",
	"http://www.warnerbros.com/sites/default/files/harry_potter_prisoner_of_azkaban_keyart.jpg", # noqu
	"https://www.youtube.com/watch?v=lAxgztbYDbs")

'''
This var = madia.Movie and atributes the information 
to the different ojects to the fuction media.Movie.
'''
despicable_me = media.Movie("Despicable Me", 
	"A master vilian and adopts three kids, and how he came to love them",
	"https://upload.wikimedia.org/wikipedia/en/d/db/Despicable_Me_Poster.jpg",
	"https://www.youtube.com/watch?v=nVwae09eSpo")

#creates a list and stores it in movies
movies = (toy_story, avatar, finding_nemo, zootopia, harry_potter_and_the_prisoner_of_azkaban, despicable_me)

fresh_tomatoes.open_movies_page(movies)

avatar.show_trailer()



