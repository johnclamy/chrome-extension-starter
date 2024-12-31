from django.shortcuts import render


movies = [
  {
    'id': 1, 'title': 'Mufasa: The Lion King', 'price': 18,
    'descr': '"Mufasa: The Lion King" enlists Rafiki to relay the legend of Mufasa to young lion cub Kiara, daughter of Simba and Nala, with Timon and Pumbaa lending their signature schtick. Told in flashbacks, the story introduces Mufasa as an orphaned cub, lost and alone until he meets a sympathetic lion named Taka--the heir to a royal bloodline. The chance meeting sets in motion an expansive journey of an extraordinary group of misfits searching for their destiny--their bonds will be tested as they work together to evade a threatening and deadly foe.'
  },
  {
    'id': 2, 'title': 'Sonic the Hedgehog 3', 'price': 20,
    'descr': 'Sonic the Hedgehog returns to the big screen this holiday season in his most thrilling adventure yet. Sonic, Knuckles, and Tails reunite against a powerful new adversary, Shadow, a mysterious villain with powers unlike anything they have faced before. With their abilities outmatched in every way, Team Sonic must seek out an unlikely alliance in hopes of stopping Shadow and protecting the planet.'
  },
  {
    'id': 3, 'title': 'The Brutalist', 'price': 20,
    'descr': 'Scaping post-war Europe, visionary architect László Toth arrives in America to rebuild his life, his work, and his marriage to his wife Erzsébet after being forced apart during wartime by shifting borders and regimes. On his own in a strange new country, László settles in Pennsylvania, where the wealthy and prominent industrialist Harrison Lee Van Buren recognizes his talent for building. But power and legacy come at a heavy cost....'
  },
  {
    'id': 4, 'title': 'Nosferatu', 'price': 16,
    'descr': 'Robert Eggers\' NOSFERATU is a gothic tale of obsession between a haunted young woman and the terrifying vampire infatuated with her, causing untold horror in its wake.'
  },
  {
    'id': 5, 'title': 'Wicked', 'price': 20,
    'descr': 'Wicked, the untold story of the witches of Oz. A young woman, misunderstood because of her unusual green skin, who has yet to discover her true power, and Grammy-winning, multi-platinum recording artist and global superstar Ariana Grande as Glinda, a popular young woman, gilded by privilege and ambition, who has yet to discover her true heart. The two meet as students at Shiz University in the fantastical Land of Oz and forge an unlikely but profound friendship. Following an encounter with The Wonderful Wizard of Oz, their friendship reaches a crossroads and their lives take very different paths. Glinda\'s unflinching desire for popularity sees her seduced by power, while Elphaba\'s determination to remain true to herself, and to those around her, will have unexpected and shocking consequences on her future. Their extraordinary adventures in Oz will ultimately see them fulfill their destinies as Glinda the Good and the Wicked Witch of the West.'
  },
  {
    'id': 6, 'title': 'A Complete Unknown', 'price': 18,
    'descr': 'New York, 1961. Against the backdrop of a vibrant music scene and tumultuous cultural upheaval, an enigmatic 19-year-old from Minnesota arrives with his guitar and revolutionary talent, destined to change the course of American music. He forges intimate relationships with music icons of Greenwich Village on his meteoric rise, culminating in a groundbreaking and controversial performance that reverberates worldwide. Timothée Chalamet stars and sings as Bob Dylan in James Mangold\'s A COMPLETE UNKNOWN, the electric true story behind the rise of one of the most iconic singer-songwriters in history.'
  },
]


def index(request):
  template_data = {}
  template_data['title'] = 'Movies'
  template_data['movies'] = movies

  return render(request, 'movies/index.html', {'template_data': template_data})


def show(request, id):
  movie = movies[id - 1]
  template_data = {}
  template_data['title'] = movie['title']
  template_data['movie'] = movie

  return render(request, 'movies/show.html', {'template_data': template_data})
