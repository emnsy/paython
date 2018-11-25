import media
import fresh_tomatoes
alnabaa = media.Movie("سورة النبا","سورة النبأ بصوت احمد السيد يوسف منسي",
                      "https://i.ytimg.com/vi/RI_JBMFMKkI/maxresdefault.jpg",
                      "https://www.youtube.com/watch?v=MlTx-4IhHko&t=34s")
# print (alnabaa.storyline)
ALNAZEAT = media.Movie(" سورة النازعات ","سورة النازعات بصوت احمد السيد يوسف منسي",
                       "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBspAnOrj7szlQuqoIJsCvRwIRdlw1eZBMhLHFwycNvuEwk7ML",
                       "https://www.youtube.com/watch?v=-Y81bvuuYDo")
                       
                       
# print (ALNAZEAT.storyline)
# alnabaa.show_trailer()
movies=[alnabaa , ALNAZEAT]
fresh_tomatoes.open_movies_page(movies)
