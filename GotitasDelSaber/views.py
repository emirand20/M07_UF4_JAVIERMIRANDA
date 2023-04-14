from django.template import Context, loader
from django.shortcuts import render
from django.http import HttpResponse

teachers = [
    {
        'id': '1',
        'name': 'Raul',
        'surname': 'Rufo',
        'age': 19
    },
    {
        'id': '2',
        'name': 'Luis',
        'surname': 'Garcia',
        'age': 23
    },
     {
        'id': '3',
        'name': 'Garcia',
        'surname': 'Marquez',
        'age': 64
    },
]

alumns = [
    {
        "name": "Alexis",
        "id": "alexis",
        "age": 26,
        "birthplace": "Sonora",
        "status": "active",
        "gendre": "h",
        "bio": "Guapo y sensible, sin embargo sabe que debe confiar mas en si mismo para que no le afecten las opiniones de los demas. Esta soltero y busca a la mujer de su vida. Consentido por su familia y trae lo nortenio en la sangre. Se define como un gran admirador del mitico Joan Sebastian."
    },
    {
        "name": "Azucena",
        "id": "azucena",
        "age": "31",
        "birthplace": "Jalisto",
        "status": "active",
        "gendre": "m",
        "bio": "Mujer luchadora que con esfuerzo y con coraje ha sacado, sola, a sus dos hijos pequenios adelante. No ha tenido suerte en el amor, sin embargo es una chica con muchas amistades. Gracias a la musica ha salido de situaciones dificiles. Le gusta hacer deporte y se identifica con la pelicula de Hercules."
    },
    {
        "name": "Chucho",
        "id": "chucho",
        "age": "14",
        "birthplace": "Mazatlan, Sinaloa",
        "status": "active",
        "gendre": "h",
        "bio": "Es el alumno mas joven en la historia de La Academia. A su corta edad ya es todo un galan que enamora a todas las mujeres. Con su simpatia, ternura y extraordinaria voz conquistara el corazon de la audiencia."
    },
    {
        "name": "Diana",
        "id": "diana",
        "age": "21",
        "birthplace": "Veracruz",
        "status": "active",
        "gendre": "m",
        "bio": "Es una mujer de ideas y metas muy claras. Proviene de una familia de musicos, en donde todo reconocen su talento. Su sonrisa, simpatia y humildad son sus senias de identidad. Consciente de que su voz no sera eterna, quiere sacar su maximo rendimiento dentro de La Academia 10."
    },
    {
        "name": "Erik",
        "id": "erik",
        "age": "26",
        "birthplace": "Puebla",
        "status": "active",
        "gendre": "h",
        "bio": "Se define como el no tipico galan de telenovela. Es de origen humilde, sencilla personalidad y a punto de convertirse en padre por segunda vez en su vida. Pretende que el nacimiento de su hijo y su entrada en La Academia 10, rubriquen un anio de exitos.",
    },
    {
        "name": "Freddy",
        "id": "freddy",
        "age": "35",
        "birthplace": "Michoacan",
        "status": "active",
        "gendre": "h",
        "bio": "Es divertido, sincero, amigable y lleno de energia. En distintas ocasiones ha estado cerca de lograr sus suenios, pero no ha sido hasta su entrada en La Academia 10 que ha podido alcanzarlos.",
    },
    {
        "name": "Gaba",
        "id": "gaba",
        "age": "29",
        "birthplace": "Monterrey",
        "status": "active",
        "gendre": "m",
        "bio": "Felizmente casada y orgullosa de haberse forjado un futuro ella sola. Entra en La Academia con el suenio de convertirse en una gran artista de baladas de la talla de Rocio Durcal y Amanda Miguel. Para ello, cuenta con su unico amuleto que es Dios y su familia. ",
    },
    {
        "name": "Hacib",
        "id": "hacib",
        "age": "29",
        "birthplace": "DF",
        "status": "active",
        "gendre": "h",
        "bio": "Es carinioso, gracioso, divertido Es muy creyente y sus origenes musicales nacieron en la iglesia catolica de Oaxaca . Siempre porta un escapulario como amuleto.Espera que durante su estancia en la Academia 10 pueda reforzar la confianza en su talento.",
    },
    {
        "name": "Lizzebeth y Marzabel",
        "id": "lizzbeth",
        "age": "34 y 14",
        "birthplace": "Baja California",
        "status": "active",
        "gendre": "m",
        "bio": "Lizzeth: La madurez y la responsabilidad con sus hijos son su cualidad mas destacada. Esta simpatica gordita, risuenia y gritona, enfrenta la vida con humor y alegria a pesar de las adversidades. Marzabal: Es otra de las pequenias promesas de La Academia 10, de hecho el la chica mas joven que ha cursado estudios en La Academia. Su alegria, sensibilidad y humildad la hacen tener un espiritu positivo. Le encanta bailar ballet. Ella y su madre lucharan unidas contra el resto de participantes.",
    },
    {
        "name": "Manuel",
        "id": "manuel",
        "age": "25",
        "birthplace": "Veracruz",
        "status": "active",
        "gendre": "h",
        "bio": "Es el amigo de todos. Alegre, sonriente y diferente. Le gusta la aventura e intentar cosas nuevas que le cambien la vida y le conviertan en el nuevo artista del momento.",
    },
    {
        "name": "Maru",
        "id": "maru",
        "age": "32",
        "birthplace": "DF",
        "status": "active",
        "gendre": "m",
        "bio": "Su personalidad madura hace que tenga las cosas muy claras en la vida. El amor es su estandarte y es capaz de dejarlo todo por un amor verdadero. Una de sus principales virtudes es la inteligencia, la persistencia y su fuerza como mujer. Ademas de su talentosa voz cultiva otras areas de las artes plasticas.",
    },
    {
        "name": "Paco",
        "id": "pako",
        "age": "31",
        "birthplace": "Mochis, Sinaloa",
        "status": "active",
        "gendre": "h",
        "bio": "Maduro, inteligente y emprendedor. Tratara de ayudar a sus companieros en su crecimiento personal y profesional. Tiene un espiritu solidario y exitoso por lo que esta seguro que pronto va a triunfar.",
    },
    {
        "name": "Rubi",
        "id": "rubi",
        "age": "19",
        "birthplace": "Sinaloa",
        "status": "active",
        "gendre": "m",
        "bio": "Joven, bonita, dulce y soniadora, pero con un caracter rebelde e impetuoso. Es una chica despierta, trabajadora e independiente. Le dara toque de simpatia y frescura a La Academia 10.",
    },
    {
        "name": "Sandra",
        "id": "sandra",
        "age": "29",
        "birthplace": "DF",
        "status": "active",
        "gendre": "m",
        "bio": "Es la guapa, la coqueta, la sensual y la glamorosa. Entra en La Academia para demostrar todo su encanto, reforzar todas sus cualidades como artista y conseguir la fuerza para ganarse al publico.",
    },
    {
        "name": "Santana",
        "id": "santana",
        "age": "21",
        "birthplace": "Tamaulipas",
        "status": "active",
        "gendre": "h",
        "bio": "Viene de familia de musicos y va a poner toda la sensibilidad que lleva dentro tanto en la convivencia con sus companieros como en la interpretacion de sus canciones, entregando toda su pasion en cada concierto.",
    },
    {
        "name": "Sel",
        "id": "sel",
        "age": "23",
        "birthplace": "Baja Califirnia",
        "status": "active",
        "gendre": "m",
        "bio": "Sabe que es bonita, agradable y simpatica. Estas son sus huellas de identidad mas destacadas. Esta en La Academia 10 porque quiere representar la fuerza de la mujer mexicana y demostrar que puede cumplir sus suenios.",
    },
    {
        "name": "Yara",
        "id": "yara",
        "age": "27",
        "birthplace": "Cuba",
        "status": "active",
        "gendre": "m",
        "bio": "Se siente feliz con su sobrepeso. Su caracter seguro la hace ser una lider nata. Es ocurrente, alegre y una bomba al desprender todo su encanto cubano. Vendio su coche y dejo su trabajo por perseguir el suenio de ser parte de La Academia 10. ",
    },
    {
        "name": "Kevin",
        "id": "kevin",
        "age": "20",
        "birthplace": "Guatemala",
        "status": "active",
        "gendre": "h",
        "bio": "Es el representante de Guatemala. No solo tiene un gran talento musical, tambien es un gran deportista. A pesar de su corta edad, es un padre responsable y amoroso. Es jovial, distraido e inquieto. Su pasatiempo principal es convivir con su familia, amigos y disfrutar de su gran pasion: la musica.",
    },
    {
        "name": "Gabriela",
        "id": "gabriela",
        "age": "41",
        "birthplace": "Argentina",
        "status": "active",
        "gendre": "m",
        "bio": "Provine de Argentina, esta casada y es una mujer sencilla que no sabe vivir sin el amor. Ha tocado el exito gracias a su impresionante voz. Se siente orgullosa del esfuerzo realizado para lograr sus objetivos. Admira a Jose Carreras. ",
    },
    {
        "name": "Mario",
        "id": "mario",
        "age": "18",
        "birthplace": "El Salvador",
        "status": "active",
        "gendre": "h",
        "bio": "Mario comenzo a cantar desde los 10, desde entonces su madre lo ha apoyado incondicionalmente. Desde pequenio ha participaba en distintos programas de television de su pais. Se considera un joven con mucha energia, disciplinado, timido y con muchas ganas de triunfar.",
    }
]

    
def proff(request, tc):
    teachers_Obj = None
    for i in teachers:
        if i['id'] == tc:
            teachers_Obj = i
    context = {'tcs': teachers_Obj}
    return render(request, 'proff.html', context)


def proffs(request):
    context = {'tcs': teachers}
    return render(request, 'proffs.html', context)


def student(request, st):
    alumn_Obj = None
    for i in alumns:
        if i['id'] == st:
            alumn_Obj = i
    context = {'std': alumn_Obj}
    return render(request, 'student.html', context)


def students(request):
    context = {'std': alumns}
    return render(request, 'students.html', context)

def users(request, pk):
    persons = ClaseA.object.get(id=pk)
    context = {'persons':persons}
    return  render(request, )
