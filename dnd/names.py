from . import base

import random

vowels='aeiouy'
friendly_consonants='bcdfghjklmnprstvwz'
soft='aefhilorsuvwyz'

def is_vowel(l):
    try: return l in vowels
    except: return False

def transmute(name, bad, good):
    import random
    for i in bad:
        random.shuffle(good)
        name=name.replace(i, good[0])
    return name

def transform(name, kernel):
    import inspect
    result=''
    for i in range(len(name)):
        a=len(inspect.getfullargspec(kernel).args)
        if   a==1: result+=kernel(name[i])
        elif a==2: result+=kernel(name, i)
        elif a==3: result+=kernel(
            None if i==0 else name[i-1],
            name[i],
            None if i==len(name)-1 else name[i+1]
        )
    return result

def kernel_triplets(last, current, next, replacement):
    if all(is_vowel(i) for i in [last, current, next]): return replacement
    if last==current==next: return replacement
    return current

def remove_weird_vowels(name, replacement=''):
    def kernel_pairs(last, current, next):
        if '{}{}'.format(last, current) in [
            'aa', 'ae', 'ao', 'ii', 'iu', 'oa', 'ue', 'uo', 'uu',
            'iw', 'uw', 'iy', 'uy',
        ]: return ''
        return current
    while True:
        old=name
        name=transform(name, lambda a, b, c: kernel_triplets(a, b, c, replacement))
        name=transform(name, kernel_pairs)
        if old==name: return name

def remove_weird(name, replacement=''):
    def kernel_pairs(last, current, next):
        if '{}{}'.format(last, current) in [
            'aa', 'ae', 'ao',
            'bc', 'bd', 'bf', 'bg', 'bj', 'bk', 'bm', 'bp', 'bq', 'bt', 'bv', 'bw', 'bx', 'bz',
            'cb', 'cc', 'cd', 'cf', 'cg', 'cj', 'cm', 'cn', 'cp', 'cq', 'cv', 'cw', 'cx', 'cz',
            'db', 'dc', 'df', 'dg', 'dk', 'dm', 'dn', 'dp', 'dq', 'dt', 'dx', 'dz',
            'ew',
            'fb', 'fc', 'fd', 'fg', 'fh', 'fj', 'fk', 'fm', 'fn', 'fp', 'fq', 'fv', 'fw', 'fx', 'fz',
            'gb', 'gc', 'gd', 'gf', 'gj', 'gk', 'gm', 'gp', 'gq', 'gt', 'gv', 'gw', 'gx', 'gz',
            'hb', 'hc', 'hd', 'hf', 'hg', 'hh', 'hj', 'hk', 'hl', 'hm', 'hn', 'hp', 'hq', 'hr', 'hs', 'ht', 'hv', 'hw', 'hx', 'hz',
            'ii', 'iu', 'iw', 'iy',
            'jb', 'jc', 'jd', 'jf', 'jg', 'jh', 'jj', 'jk', 'jl', 'jm', 'jn', 'jp', 'jq', 'jr', 'js', 'jt', 'jv', 'jw', 'jx', 'jy', 'jz',
            'kb', 'kc', 'kd', 'kf', 'kg', 'kj', 'kk', 'km', 'kn', 'kp', 'kq', 'kr', 'kt', 'kv', 'kw', 'kx', 'kz',
            'lc', 'lf', 'lh', 'lj', 'lq', 'lr', 'lw', 'lx', 'lz',
            'mc', 'md', 'mf', 'mg', 'mj', 'mk', 'ml', 'mp', 'mq', 'mv', 'mw', 'mx', 'mz',
            'nb', 'nf', 'nj', 'np', 'nq', 'nr', 'nv', 'nw', 'nx', 'nz',
            'oa',
            'pb', 'pc', 'pd', 'pf', 'pg', 'pj', 'pk', 'pq', 'pv', 'pw', 'px', 'pz',
            'qb', 'qc', 'qd', 'qf', 'qg', 'qh', 'qj', 'qk', 'ql', 'qm', 'qn', 'qp', 'qq', 'qr', 'qs', 'qt', 'qv', 'qw', 'qx', 'qy', 'qz',
            'rj',
            'sb', 'sd', 'sf', 'sg', 'sj', 'sr', 'sx', 'sz',
            'tb', 'tc', 'td', 'tf', 'tg', 'tj', 'tk', 'tm', 'tn', 'tp', 'tq', 'tv', 'tw', 'tx', 'tz',
            'ue', 'uo', 'uu', 'uw', 'uy',
            'vb', 'vc', 'vd', 'vf', 'vg', 'vh', 'vj', 'vk', 'vl', 'vm', 'vn', 'vp', 'vq', 'vr', 'vs', 'vt', 'vv', 'vw', 'vx', 'vz',
            'wb', 'wc', 'wd', 'wf', 'wg', 'wj', 'wm', 'wp', 'wq', 'wu', 'ww', 'wx', 'wz',
            'xb', 'xc', 'xd', 'xf', 'xg', 'xh', 'xj', 'xk', 'xl', 'xm', 'xn', 'xp', 'xr', 'xs', 'xv', 'xw', 'xx', 'xz',
            'yb', 'yc', 'yd', 'yf', 'yg', 'yh', 'yj', 'yk', 'yp', 'yq', 'yv', 'yw', 'yy', 'yz',
            'zb', 'zc', 'zd', 'zf', 'zg', 'zj', 'zk', 'zm', 'zn', 'zp', 'zq', 'zr', 'zs', 'zt', 'zv', 'zw', 'zx',
        ]: return ''
        return current
    while True:
        old=name
        name=transform(name, lambda a, b, c: kernel_triplets(a, b, c, replacement))
        name=transform(name, kernel_pairs)
        if old==name: return name

def remove_dupes(name):
    def kernel(last, current, next):
        if last==current: return ''
        return current
    while True:
        old=name
        name=transform(name, kernel)
        if old==name: return name

def vowelify(name, vowels):
    def kernel(last, current, next):
        if is_vowel(current) and base.maybe(): return base.pick(vowels)
        return current
    return transform(name, kernel)

def misspell(name, source):
    def kernel(last, current, next):
        if(not is_vowel(current) and base.maybe(4) and(
            not last and is_vowel(next)
            or
            not next and is_vowel(last)
            or
            is_vowel(last) and is_vowel(next)
        )): return base.pick(source)
        return current
    return transform(name, kernel)

def vowel_start(name):
    indices=[]
    for i in range(len(name)):
        if is_vowel(name[i]):
            indices.append(i)
    return name[base.pick(indices):]

def soft_ending(name):
    indices=[]
    for i in range(len(name)):
        if name[i] in soft:
                indices.append(i)
    return name[:base.pick(indices)+1]

def humanify(name, vowel, misspelling_source):
    if vowel:
        if base.rn(3): name=vowelify(name, vowel)
    if base.rn(3): name=misspell(name, misspelling_source)
    return remove_weird_vowels(name)

def unpack_qs(name): return name.replace('q', 'qu').replace('uu', 'ua').replace('uy', 'ui')

human_last=[
    'alpha', 'anton', 'armand', 'alvaro', 'abatelli', 'abbott', 'abbyss', 'abel',
    'ackerman', 'adams', 'adolthine', 'agnolo', 'ainsley', 'alders', 'alderwick',
    'aldred', 'althorpe', 'ambler', 'ambrose', 'anderson', 'arblaster',
    'aronowitz', 'ashcroft', 'atkinson', 'aurelius', 'almanzar',
    'boyce', 'benton', 'bradford', 'bell', 'bones', 'boot', 'brown', 'baal',
    'balthasar', 'berkley', 'bathurst', 'beardsley', 'bearman', 'beasley',
    'beau', 'bedford', 'beers', 'bonnor', 'bolt', 'boddington', 'blumfield',
    'bisset', 'barry', 'brahms', 'brannigan', 'bridges', 'buckley',
    'colton', 'cortez', 'clark', 'cole', 'corner', 'cresswell', 'crouch',
    'corbin', 'caddock', 'caesar', 'cornell', 'costello', 'church', 'cantor',
    'cisco', 'cranston', 'creighton', 'crockford', 'cromar', 'colville',
    'cumberbatch', 'cyphus', 'capulong',
    'deangelo', 'del', 'delbert', 'davies', 'dempster', 'daingerfield', 'doyle',
    'drake', 'dalrymple', 'dethloff', 'drysdale', 'darington', 'duff',
    'dumberrill', 'dunderdale',
    'eldridge', 'erasmo', 'euler', 'eldin', 'elderbrant', 'essex', 'esterbrook',
    'elrick', 'etchingham', 'ethersey', 'edison', 'exeter', 'eggins', 'engels',
    'filiberto', 'fausto', 'felton', 'figg', 'finnigan', 'flint', 'fletcher',
    'ferrari', 'fonzone', 'forbes', 'fahrenbacher', 'flaherty', 'feron',
    'foxley', 'farmer', 'farnsworth', 'fitzpatrick', 'flockhart', 'flynn',
    'fraxedas',
    'granville', 'genesis', 'goldstein', 'galbraith', 'gainsborough', 'gozney',
    'gozard', 'graves', 'glass', 'gatsby',
    'hobert', 'harland', 'hayden', 'hadcock', 'hixley', 'haddock', 'hodgins',
    'hattersley', 'hoffman', 'hammerberger', 'heaviside', 'hubbard', 'handy',
    'hanning', 'heinemann', 'heinz', 'harvard',
    'isidro', 'inez', 'inkles', 'ion', 'ixer',
    'jared', 'jayne', 'johnson', 'jordan', 'jacobi', 'jennings', 'jenkins',
    'jickles',
    'kendrick', 'kerry', 'kane', 'klimmek', 'klug', 'kloster', 'kowalski',
    'kipling', 'kunzelmann',
    'lynwood', 'latonia', 'lizette', 'lithgow', 'loadsman', 'longman', 'lovejoy',
    'luchelli', 'lillecrap', 'lindenberg',
    'marcellus', 'mcmaster', 'marsh', 'montague', 'melville', 'macbeth',
    'merryweather', 'mays', 'macfadden', 'mcgee', 'metcalfe', 'macknight',
    'magrannell', 'mcfall', 'monk', 'margach', 'moulding', 'mclucky', 'mcphail',
    'mulcaster', 'mulberry', 'murdoch', 'murphy', 'mycock', 'million',
    'nolan', 'nicola', 'nesbitt', 'nolleth', 'netherclift', 'normandale',
    'newdick', 'noseworthy', 'nunnerly', 'node', 'nutty',
    'orville', 'oneida', 'ozella', "o'brian", "o'connell", "o'hederscoll", 'ohm',
    'orr', 'oakley', 'ortega', "o'leary", 'osgood', 'oldrey', "o'neill",
    'oxford', "o'hara",
    'porter', 'providencia', 'parkinson', 'pascal', 'pape', 'penrose', 'plank',
    'pocklington', 'pogg', 'petrakov', 'pontefract', 'popov', 'pfeffle',
    'philcox', 'philips', 'pauli', 'pickles', 'prevost', 'prettyjohn', 'pringle',
    'pinor',
    'qeen', 'qinn', 'qade', 'qimby', 'qigg', 'qixley',
    'rey', 'rolf', 'robins', 'rookwell', 'roscoe', 'rosenberg', 'rosenblatt',
    'rosenvasser', 'richley', 'rutherford', 'rankine', 'rosso', 'ravenscraft',
    'rizzotto', 'robinson', 'rodriguez', 'renn',
    'sherwood', 'salvatore', 'smith', 'shepherd', 'spicer', 'sherbourne',
    'sherlock', 'spooner', 'salomon', 'shucksmith', 'savage', 'simco', 'saxon',
    'scamwell', 'stetson', 'schmidt', 'schneider', 'stockwell', 'schultz',
    'skurray', 'stotherfield', 'sedgwick', 'selwyn', 'shadbolt', 'souza', 'swift',
    'tyron', 'tomas', 'tilley', 'templar', 'tubbles', 'thexton', 'turing', 'thor',
    'thonger', 'thorald', 'twigg', 'twycross', 'tyndall',
    'un', 'ute', 'ubsdale', 'umbers', 'umfrey', 'upton', 'urlich', 'underwood',
    'valene', 'valentine', 'vertigan', 'vance', 'vandrill', 'vern', 'varnham',
    'winford', 'warner', 'waltraud', 'wood', 'witherby', 'walsh', 'wolfendell',
    'woodrow', 'watt', 'widmore', 'wiggins', 'wordsworth', 'wozencraft', 'weber',
    'wyldbore',
    'xylmore', 'xebec', 'ximenez',
    'yael', 'young', 'yakobovitz', 'yegorchenkov', 'yonge', 'yarr', 'yeardsley',
    'zada', 'zetta', 'zena', 'zmitrovich', 'zambon', 'zimmerman', 'zylberdik',
]

human_first_male=[
    'abner', 'albert', 'alfonso', 'arnold', 'abraham', 'anthony', 'augustus', 'adam',
    'barney', 'boris', 'benedict', 'bartholomew', 'barnaby', 'benjamin',
    'constantine', 'cornelius', 'craig', 'cedrick', 'cid', 'claude', 'colin',
    'clyde', 'cameron', 'chad', 'caleb','cadmus', 'clarence',
    'dennis', 'dimitri', 'david', 'douglas', 'dexter', 'dedalus',
    'edward', 'edmund', 'ezekiel', 'edison', 'elliot', 'emilio', 'ernie',
    'fernando', 'finn', 'frank', 'felix',
    'gabe', 'gary', 'gregor', 'gregory', 'gaston', 'garth', 'guadalupe', 'graham',
    'harry', 'herbert', 'hugo', 'harvey',
    'ian', 'indira', 'ivan', 'isaac', 'irving', 'ignacio',
    'john', 'jarret', 'jordan', 'justin', 'james',
    'kenneth', 'kevin', 'kermit',
    'luigi', 'lincoln', 'lee',
    'marcel', 'malcolm', 'milhous', 'michael', 'marcus', 'marvin', 'martin',
    'nathaniel', 'neville', 'nigel',
    'oswald', 'octavio', 'ogden', 'osmund',
    'pierre', 'percy', 'patrick', 'peter', 'phineas',
    'qentin', 'qincy',
    'raymond', 'reginald', 'roger', 'rabastan', 'rudolph', 'rodolphus', 'robert',
    'rufus', 'ralph', 'rupert',
    'stephen', 'sebastian', 'stuart', 'sylvester', 'stanley', 'seamus',
    'tony', 'terence', 'theodore',
    'ulysses', 'ulrike',
    'virgilio', 'vince', 'vincent',
    'wally', 'william', 'wesley', 'wilhelm', 'wolfgang', 'wilfrid',
    'xavier', 'xeno',
    'yuri', 'yolando',
    'zachary',
]

human_first_female=[
    'alison', 'anastasia', 'agnes', 'amelia', 'angelina', 'angela', 'alice', 'abigail',
    'aurora', 'alicia',
    'barbara', 'betty', 'bernice', 'bertha', 'belcalis',
    'carol', 'clara', 'carri', 'cecilia', 'chelsea',
    'dorothy', 'doris', 'darlene', 'delilah', 'dolores',
    'evelyn', 'emily', 'edna', 'eleanor', 'esther', 'emma', 'eva', 'eve',
    'felicia', 'faye', 'fannie',
    'genevieve', 'gretchen', 'gwendolyn',
    'heidi', 'helen', 'harriet', 'hannah', 'helga', 'helena', 'hilary',
    'ingrid', 'ida', 'irma', 'iris', 'isabelle', 'imogene', 'imelda',
    'joyce', 'judith', 'josephine',
    'katerina', 'kendra', 'kelsey', 'katie',
    'lisa', 'lillian', 'lucille', 'lorraine', 'lily',
    'marla', 'margaret', 'martha', 'mildred', 'marjorie', 'mabel', 'meredith',
    'mary', 'molly', 'marlenis',
    'nancy', 'norma', 'nutmeg',
    'olga', 'olivia', 'olympia', 'omega', 'odelia', 'oretha', 'ouranos',
    'patricia', 'phyllis', 'penelope', 'poppy',
    'ruth', 'regina', 'rita',
    'sophie', 'sandra', 'sherry', 'sheila', 'shirley',
    'thelma', 'tammy',
    'ursula', 'ultima',
    'veronica', 'virginia', 'violet', 'velma',
    'wendolyn', 'wilma', 'winifred', 'willow', 'winona',
    'xena', 'xenia',
    'yvonne', 'yasmin',
    'zoe', 'zelda',
]

human_first_unisex = [
    'eden',
    'happy',
]

def human(gender=None, normal=False):
    if gender==None: gender=random.choice('mf')
    if gender=='m':
        first=human_first_male
    else:
        first=human_first_female
    first=base.pick(first+human_first_unisex)
    if not normal:
        if gender=='m':
            first=humanify(first, 'o', friendly_consonants)
        else:
            first=humanify(first, 'ai', 'ai')
    last=base.pick(human_last)
    if not normal: last=humanify(last[:-1], base.pick('aeiou'), friendly_consonants)+last[-1]
    if base.maybe(32): last=base.pick(['van', 'von'])+' '+last
    return unpack_qs(first.capitalize()+' '+last.capitalize())

def elf():
    words=[
        'arc', 'autumn', 'air', 'aura', 'amber', 'arrow', 'apple', 'almond', 'acorn',
        'bell', 'bud', 'bulb', 'bark', 'bolt', 'born', 'blink', 'bloom',
        'cast', 'caw', 'cat', 'clap', 'claw', 'crest', 'creed', 'chord', 'cedar', 'candle',
        'deep', 'dawn', 'dune', 'dust', 'dove', 'dusk', 'deer', 'day', 'delta', 'dance',
        'eve', 'edge', 'emote', 'ember', 'eagle', 'earth', 'elder',
        'free', 'fir', 'fox', 'fawn', 'flux', 'fold', 'ford', 'fire', 'fur', 'flint',
        'guard', 'glow', 'gray', 'glade', 'glean', 'glaze', 'grand', 'glory', 'goose',
        'hill', 'hop', 'hum', 'hue', 'hive', 'howl', 'hike', 'hawk', 'horn', 'hope',
        'image', 'ivy', 'ice', 'iota', 'if',
        'jet', 'joy', 'jump', 'judge',
        'kite', 'key',
        'leaf', 'love', 'light', 'lux', 'lee', 'lime', 'lake', 'land', 'live', 'loon',
        'mist', 'mire', 'moth', 'mint', 'mind', 'merry', 'mood', 'moral', 'music',
        'name', 'new', 'nova', 'navy', 'next', 'nimbus', 'nymph',
        'old', 'oak', 'owl', 'otter', 'open', 'olive', 'order',
        'pine', 'pond', 'poem', 'pure', 'pluck',
        'qest', 'qick', 'qake', 'qill', 'qail',
        'rain', 'ridge', 'ray', 'ram', 'red', 'ray', 'reef', 'ride', 'rise', 'rhyme',
        'song', 'sight', 'spider', 'silk', 'seed', 'see', 'say', 'sky', 'sage', 'slim',
        'thorn', 'tree', 'tune', 'tone', 'true', 'terra', 'tide', 'trust', 'think',
        'under', 'union',
        'vision', 'vim', 'vigor', 'vine', 'view', 'vibe', 'voice',
        'wisp', 'willow', 'wind', 'wild', 'warm', 'wise',
        'xylo',
        'yes',
        'zest', 'zeal',
    ]
    first1, first2, last1, last2=base.pick(words, 4)
    first1=soft_ending(first1)
    if not any([is_vowel(i) for i in first1]): first1=base.pick('aei')+first1
    if base.maybe(): first2=vowel_start(first2)
    if base.maybe(): last1=soft_ending(last1)
    if first1[-1]==first2[0]: first1=first1[:-1]
    if base.maybe(): first1=vowelify(first1, 'i')
    if base.maybe(): first2=vowelify(first2, base.pick('ei'))
    first=first1+first2
    bad_endings=[
        'age', 'ase', 'b', 'c', 'd', 'de', 'g', 'j', 'k', 'm', 'o', 'p', 'q', 't', 'u', 'v', 'w', 'x', 'z',
        'be', 'ke', 'me', 'ne', 'pe', 'qe', 'te', 've', 'we',
    ]
    if any(first.endswith(i) for i in bad_endings):
        first+=base.pick('ei')+base.pick(['l', 'th'])
    first=transmute(first, ['j', 'k', 'p', 'x'], ['l', 'th'])
    first=transmute(first, ['u', 'w', 'oo'], ['i'])
    first=first.replace('ei', 'ie')
    first=remove_weird(first)
    last =remove_weird(last1+last2)
    return unpack_qs(first.capitalize()+' '+last.capitalize())

def dwarf(gender=None):
    if gender==None: gender=random.choice('mf')
    if gender=='m':
        first1=[
            'ad', 'alber',
            'ba', 'bar', 'brot', 'brue',
            'da', 'dar', 'del',
            'eb', 'ein', 'far',
            'flin',
            'gar',
            'har',
            'kil',
            'mor',
            'or', 'os',
            'ran',
            'ru',
            'tak', 'thora', 'thor', 'tor', 'trau', 'tra',
            'ulf',
            've',
            'von',
        ]
        first2=[
            'bek', 'bon',
            'dain', 'drak', 'din', 'dek', 'dal',
            'ern', 'endd', 'eg', 'erk',
            'grim', 'gran', 'gar',
            'in', 'it',
            'kil', 'kar',
            'linn',
            'nor',
            'rik', 'rich', 'rak',
            'sik',
            'tor',
            'vok',
        ]
    else:
        first1=[
            'am', 'ar', 'aud',
            'bar',
            'dag', 'die',
            'eld',
            'falk', 'finel',
            'gunn', 'gur',
            'hel',
            'kath', 'kris',
            'il',
            'lift',
            'mar',
            'ris',
            'san',
            'tor', 'torg',
            'vis',
        ]
        first2=[
            'ber', 'bera',
            'dryn', 'dis', 'de', 'dred',
            'eth',
            'ga',
            'hild',
            'ja',
            'len', 'loda', 'lin',
            'nal',
            'runn', 'ra', 'rasa',
            'sa',
            'tin', 'tryd', 'tra',
            'wynn',
        ]
    last1=[
        'abysso', 'angle',
        'bed', 'brine', 'bronze', 'brass', 'battle', 'brawn',
        'cave', 'copper',
        'dark', 'diamond', 'dank',
        'earth', 'emerald',
        'far', 'fix',
        'granite', 'gold', 'gore',
        'hang', 'hall',
        'inner', 'iron',
        'jack',
        'kraken', 'kit',
        'lawful', 'lode',
        'moss', 'musk',
        'nor', 'nix',
        'old',
        'pack', 'phase',
        'qarry', 'qartz',
        'rock', 'ruby', 'rune', 'rum',
        'stone', 'strong', 'stal',
        'tin', 'tungsten',
        'under', 'ultra',
        'vole', 'vast',
        'wax', 'well',
        'yest', 'yam',
    ]
    last2=[
        'anvill',
        'beard', 'bring', 'brow',
        'cutt', 'chuck', 'chin',
        'dwell', 'dirk', 'dig',
        'foot', 'fair', 'fix', 'forge', 'fist',
        'grott',
        'haus', 'hamm', 'hold', 'heim',
        'jutt',
        'knuckle',
        'lord',
        'mite', 'mine',
        'nix',
        'panz',
        'rock',
        'seek', 'stone', 'stock',
        'tite',
        'vole',
        'walk',
        'yard',
        'zone',
    ]
    first=base.pick(first1)+base.pick(first2)
    last1=base.pick(last1)
    while True:
        x=base.pick(last2)
        if x!=last1: last2=x; break
    if last2=='i': import pdb; pdb.set_trace()
    last=last1+last2+base.pick(['', 'er'])
    if last.endswith('eer'): last=last[:-2]+last[-1]
    return unpack_qs(first.capitalize()+' '+last.capitalize())

def tiefling(gender=None): return human(gender, normal=True)

def gnome(gender=None):
    return base.pick([
        'al', 'alfo',
        'bo',
        'chum',
        'nick',
        'rump',
        'smol',
        'thump',
        'watt', 'wink',
    ]).capitalize()+base.pick([
        'ba', 'ber',
        'el',
        'gas',
        'zo',
    ])+' '+base.pick([
        'bogden', 'boddle',
        'dergel', 'dodder', 'dunder',
        'folko',
        'gogo',
        'humperdink',
        'jumper',
        'knackle',
        'nackle', 'ningel',
        'pumpkin',
        'ramble',
        'scheppen', 'stiltskin',
        'tinkle',
        'virgil', 'vosso',
        'wackle',
        'yacko',
        'zozo',
    ]).capitalize()

def dragonborn(gender=None):
    result=''
    if base.maybe(): result+=base.pick('cdfhklmnprstvyz')
    syllables=[
        'ar', 'aur', 'ax',
        'ex',
        'ian', 'id', 'il', 'ith', 'ix',
        'us',
    ]
    result+=''.join(base.pick_n(syllables, base.rn((2, 5))))
    return result.capitalize()

def goblin():
    a=[
        'al',
        'bog', 'brod', 'brown',
        'drizz',
        'ear',
        'gor', 'grip', 'gnar', 'grin', 'grizz', 'grins',
        'mez',
        'pig',
        'rag',
        'snizz', 'shizz',
        'tur',
        'nag',
        'ug',
    ]
    b=[
        '',
        'bat', 'bot', 'bart', 'bort', 'bag', 'barg', 'borg', 'bog',
        'dag',
        'ek',
        'guff', 'grod', 'git', 'gott',
        'hook',
        'lak', 'ler', 'let',
        'nuk', 'nok', 'nak',
        'rod', 'rig',
        'tooth',
    ]
    return base.pick(a).capitalize()+base.pick(b)

def dwarf_town():
    prefixes=[
        'copper',
        'alber',
        'glas', 'gold',
        'ham',
        'odin',
        'silver',
    ]
    infixes=[
        'ar',
        'cal',
        'fer',
        'il',
        'kin',
        's',
        'tin',
    ]
    suffixes=[
        'bard', 'burg',
        'den', 'ding',
        'gin',
        'helm', 'hill',
        'lock',
        'mine',
        'ness',
        'rig', 'rock',
        'stone',
        'ton',
        'vein',
    ]
    result=base.pick(prefixes).capitalize()
    if base.maybe(4): result+=base.pick(infixes)
    result+=base.pick(suffixes)
    return result

def gnome_town():
    prefixes=[
        'chumba',
        'humper',
        'smolgas',
        'rumpel',
        'thimble', 'tinker', 'toddle', 'trundle', 'tuber',
        'wagga', 'wattle', 'winkle', 'wollon', 'woy',
    ]
    suffixes=[
        'bed', 'burrow',
        'dink',
        'garden',
        'lawn',
        'pillow',
        'shire',
    ]
    return base.pick(prefixes).capitalize()+base.pick(suffixes)

def tavern():
    def adjective(): return random.choice([
        'admirable', 'all-seeing',
        'babbling', 'blind', 'bottomless', 'black',
        "captain's", 'conniving', 'crafty', 'calm', 'cool',
        'daring', 'dining', 'dirty', 'disasterous', 'drunken',
        'eerie', 'elegant',
        'furry', 'fuzzy', 'fluffy', 'flopping',
        'gentle', 'gobbling',
        'healthy', 'handsome',
        'intelligent', 'interesting',
        'jumping', 'jealous',
        'kempt', 'keen', 'kingly', 'knightly',
        'lazy', 'leaping', 'leaky',
        'magic', 'mellow', 'muddled', 'mysterious',
        'naked', 'naughty',
        'opportune', 'one-eyed',
        'pleasant', 'punctual',
        'quiet', 'quaint', 'questionable',
        'rotten', 'rowdy', 'raunchy',
        'salty', 'spring', 'steady', 'stoic', 'singing', 'sultry',
        'timely', 'timid', 'tipsy', 'twisted', 'talking', 'thirsty',
        'unique', 'unkempt',
        'virtuous', 'virgin',
        'well-mannered', 'wild', 'wishful', 'woken', 'wintry',
        'yawning', 'youthful',
        'zealous', 'zesty',
    ]).capitalize()
    def animal(): return random.choice([
        'aardvark', 'ant', 'alchemist',
        'bard', 'bagder', 'bat', 'boar',
        'chicken', 'coyote', 'cardinal', 'crow',
        'dingo', 'dog', 'dragon', 'duck', 'devil', 'demon',
        'elephant', 'eel', 'eagle',
        'fox', 'frog', 'falcon', 'fish',
        'goose', 'gander', 'gosling',
        'hare', 'hog', 'hawk', 'hound',
        'iguana',
        'jackal', 'jackalope', 'jellyfish', 'jester',
        'kingfisher', 'knight',
        'llama', 'lion', 'lizard', 'lady',
        'mole', 'monkey', 'moose', 'mouse',
        'narwhal', 'nautilus', 'newt', 'nightingale',
        'octopus', 'ostrich', 'ox', 'oyster',
        'parrot', 'peacock', 'penguin', 'pheasant', 'philosopher', 'pigeon', 'pirate',
        'quail', 'quetzal',
        'rabbit', 'raccoon', 'ram', 'rat', 'raven', 'rooster',
        'seahorse', 'serpent', 'snake', 'sorcerer', 'spider',
        'thief', 'tortoise', 'turtle', 'toad',
        'unicorn',
        'vole', 'vulture', 'victor',
        'walrus', 'warthog', 'weasel', 'whale', 'witch', 'wizard', 'warlock',
        'yak',
        'zebra', 'zealot', 'zombie',
    ]).capitalize()
    def place(): return random.choice([
        'abbey', 'alehouse', 'attic',
        'bar', 'brewhouse',
        'club', 'canteen',
        'den', 'drinkery',
        'meadhouse',
        'pub',
        'saloon',
        'tavern',
        'watering hole',
    ]).capitalize()
    def object(): return random.choice([
        'apple', 'acorn',
        'bottle', 'bucket', 'bassoon', 'broomstick', 'bastard',
        'cello', 'cauldron', 'carnation', 'cucumber', 'chair',
        'dandelion', 'daffodil',
        'empire',
        'flower', 'fig', 'fiddle', 'feather', 'folly',
        'grape', 'garden',
        'horn', 'harp', 'head',
        'instrument',
        'joke',
        'kelp',
        'lily', 'lotus', 'lyre', 'lute',
        'moon',
        'niche', 'nest',
        'oboe', 'olive',
        'pipe', 'pumpkin', 'peach', 'pear', 'pickle', 'plum', 'promise',
        'quirk',
        'rose', 'roost',
        'sunflower', 'secret', 'spring',
        'tooth', 'teapot', 'tulip', 'toadstool', 'trumpet', 'trombone', 'tuba',
        'undoing',
        'viola', 'vine',
        'wish', 'well',
        'xylophone',
        'youth',
        'zithern', 'zodiac',
    ]).capitalize()
    def maybe_adjective(arg):
        if base.maybe(): arg=adjective()+' '+arg
        return arg
    def one_of(*args):
        return random.choice(args)()
    return one_of(
        lambda: '{}'.format(maybe_adjective(one_of(animal, object))),
        lambda: "{}'s {}".format(maybe_adjective(animal()), object()),
        lambda: '{} and the {}'.format(animal(), one_of(animal, object)),
        lambda: '{} {}s'.format(random.randint(3, 7), one_of(animal, object)),
    )

def dog():
    prefixes = [
        'axe-',
        'bear',
        'crimson',
        'deep-',
        'eagle-', 'ember',
        'fury-', 'fire-', 'fast', 'fox',
        'grit-', 'good', 'grey',
        'hawk',
        'ice-',
        'joust',
        'keep-',
        'lance-', 'long',
        'mace-',
        'nettle-',
        'opal',
        'pale',
        'quick',
        'ring', 'round', 'rex',
        'storm', 'shadow', 'spark', 'spike-', 'silver', 'strong', 'sky', 'sight',
        'timber',
        'ultra',
        'vile',
        'willow',
        'yellow',
    ]
    suffixes=[
        'amble',
        'bark', 'bite',
        'claw', 'call', 'canter',
        'doodle',
        'ear', 'eye',
        'fur', 'fisher',
        'gallop',
        'howl', 'hulk', 'hunter', 'hound',
        'lope',
        'mouth',
        'nose',
        'paw',
        'snout', 'sprint',
        'tail', 'toe', 'tongue', 'tooth', 'trot',
        'wolf', 'walker',
    ]
    return ' '.join([
        random.choice(human_first_male+human_first_female).capitalize(),
        random.choice(prefixes).capitalize()+random.choice(suffixes),
    ])

def potty():
    prefixes = [
        'ball', 'big-',
        'dirt', 'dingle', 'dunce', 'dim',
        'fug',
        'little-',
        'nip', 'nim', 'nit', 'nin',
        'ug',
    ]
    affixes = [
        'ass',
        'boner', 'barf', 'butt', 'block', 'bum', 'bottom',
        'crap', 'cock', 'crotch', 'clam', 'crud', 'cud', 'corn', 'crum',
        'dick',
        'fart', 'fondle',
        'gobble',
        'jerk', 'jam', 'junk',
        'piss',
        'rod',
        'shit', 'snot', 'suck', 'slop',
        'turd', 'thunder', 'toss', 'trash',
        'wank',
    ]
    suffixes = [
        'balls', 'bag', 'bagger', 'bucket', 'bowl', 'belch', 'berry',
        'crapper', 'chunk', 'compoop',
        'dicker', 'dong', 'dope',
        'farter', 'fondler',
        'guzzler',
        'hole', 'head',
        'munch',
        'nugget',
        'sucker', 'shitter', 'smear', 'sniffer', 'scratch', 'spank', 'smack',
        'wad', 'wit', 'wipe',
    ]
    postfixes = [
        'o',
        's',
        'us',
    ]
    result=random.choice(prefixes+affixes)+random.choice(affixes+suffixes)
    result=result.replace('sss', 'ss-s')
    result=result.replace('ttt', 'tt-t')
    if random.random() < 0.5:
        result += random.choice(postfixes)
    return result.capitalize()

def bird_town():
    prefixes=[
        'breeze',
        'crow',
        'feather',
        'gaggle',
        'murder',
        'pretty',
        'raven', 'raptor',
        'talon', 'tit', 'touca',
        'wind', 'wing',
    ]
    suffixes=[
        'cliff',
        'dive',
        'fly', 'fall',
        'haven', 'home', 'heights',
        'inwing',
        'loft',
        'nest',
        'perch', 'peak', 'port',
        'roost', 'rocca',
        'tower', 'tree',
        'underwing',
        'view',
        'wing',
    ]
    return base.pick(prefixes).capitalize()+base.pick(suffixes)

def half_orc(gender=None):
    if random.random() < 0.5:
        return human(gender)
    if gender==None: gender=random.choice('mf')
    if gender == 'm':
        return random.choice([
            'Dench',
            'Feng',
            'Gell',
            'Henk',
            'Holg',
            'Imsh',
            'Keth',
            'Krusk',
            'Mhurren',
            'Ront',
            'Shump',
            'Thokk',
        ])
    else:
        return random.choice([
            'Baggi',
            'Emen',
            'Engong',
            'Kansif',
            'Myev',
            'Neega',
            'Ovak',
            'Ownka',
            'Shautha',
            'Sutha',
            'Vola',
            'Volen',
            'Yevelda',
        ])
