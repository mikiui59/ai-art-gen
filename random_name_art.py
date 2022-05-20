import random

text_one=["A painting of a", "A pencil art sketch of a", "An illustration of a", "A photograph of a"]
text_two=["spinning","dreaming","watering","loving","sleeping","repeating","surreal","psychedelic"]
text_three=["fish","cat","horse","dog","house","door","table","tree","grass", "flower", "plant","bloom", "spanner","spider", "figurine", "statue", "car",  "monitor"]
styles=["Art Nouveau", "Camille Pissarro", "Claude Monet", "Fauvism", "Futurism", "Impressionism",
 "Picasso", "Pop Art", "Modern art", "Surreal Art", "Sandro Botticelli", "oil paints", "watercolours", "weird bananas", "strange colours",'Baroque','Abstract Expressionism','Classicism','Expressionism','Fauvism','Impressionism','Neo Impressionism','Performance Art','Pop Art','Post Impressionism']
place=['forest','sky','space','moon','ice','fire']
t=['in','on','at','into','under']
text_new=["fish","cat","horse","dog","house","table","tree","grass", "plant","bloom", "spanner","spider", "figurine", "statue", "car",  "monitor"]


text=text_one[random.randint(0,len(text_one)-1)]
if random.random()>0.4:
    text+=" " +text_two[random.randint(0,len(text_two)-1)]
    text+=" "+ text_three[random.randint(0,len(text_three)-1)]
    text+=" in the style of "+ styles[random.randint(0,len(styles)-1)] 
    if random.random()>0.5:
        text+=" and " + styles[random.randint(0,len(styles)-1)]
else:
    text=text_new[random.randint(0,len(text_new)-1)]
    text+=" "+ t[random.randint(0,len(t)-1)]
    text+=" "+ place[random.randint(0,len(place)-1)]
    if random.random()>=0.5:
        text+=" in the style of "+ styles[random.randint(0,len(styles)-1)] 
        
with open('text.txt','w') as f:
  f.write(text)
