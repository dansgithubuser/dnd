from dataclasses import dataclass
import random

@dataclass
class Person:
    name: str
    gender: str
    birth_date: int
    death_date: int
    mother: 'Person'
    father: 'Person'
    children: list
    last_pregnancy_date: int

    @staticmethod
    def random_initial(name_generator, longevity):
        gender = random.choice('mf')
        return Person(
            name=name_generator(gender=gender),
            gender=gender,
            birth_date=-random.randint(0, longevity),
            death_date=None,
            mother=None,
            father=None,
            children=[],
            last_pregnancy_date=-random.randint(0, longevity),
        )

    @staticmethod
    def child(name_generator, birth_date, mother, father):
        gender = random.choice('mf')
        return Person(
            name=name_generator(gender=gender),
            gender=gender,
            birth_date=birth_date,
            death_date=None,
            mother=mother,
            father=father,
            children=[],
            last_pregnancy_date=birth_date,
        )

    def alive(self):
        return self.death_date == None

def genetic_similarity(a, b, max_depth=3):
    if any([
        not a.mother,
        not a.father,
        not b.mother,
        not b.father,
    ]):
        return 0
    if a == b:
        return 1
    if a.mother == b.mother and a.father == b.father:
        return 0.5
    if a.mother == b.mother:
        return 0.25
    if a.father == b.father:
        return 0.25
    if max_depth == 0:
        return 0
    return sum([
        genetic_similarity(a.mother, b, max_depth-1),
        genetic_similarity(a.father, b, max_depth-1),
        genetic_similarity(a, b.mother, max_depth-1),
        genetic_similarity(a, b.father, max_depth-1),
    ]) / 4

def create(
    *,
    initial_population,
    longevity,
    name_generator,
    years,
    reproductive_age_range,
    reproductive_cooldown,
    overpopulation_avoidance,
    base_death_rate,
    max_population,
    overpopulated_death_rate,
    max_genetic_similarity,
    inbreediness,
    disaster_frequency,
    disaster_severity,
    disaster_longevity,
):
    if type(initial_population) == int:
        people = [Person.random_initial(name_generator, longevity) for _ in range(initial_population)]
    else:
        people = initial_population
    alive = [person for person in people if person.alive()]
    disaster_time = 0
    disaster_death_rate = 0
    for year in years:
        # reproduction
        print(year, len(alive))
        reproductives = [
            person for person in alive
            if year - person.birth_date in reproductive_age_range
        ]
        reproductive_males = [
            person for person in reproductives
            if person.gender == 'm'
        ]
        reproductive_females = [
            person for person in reproductives
            if person.gender == 'f'
                and year - person.last_pregnancy_date > reproductive_cooldown
        ]
        random.shuffle(reproductive_males)
        random.shuffle(reproductive_females)
        for male, female in zip(reproductive_males, reproductive_females):
            if genetic_similarity(male, female) > max_genetic_similarity and random.random() > inbreediness:
                continue
            if len(alive) > max_population:
                if random.random() < overpopulation_avoidance:
                    break
            female.last_pregnancy_date = year
            child = Person.child(name_generator, year, female, male)
            male.children.append(child)
            female.children.append(child)
            people.append(child)
            alive.append(child)
        # disaster
        if random.random() < disaster_frequency:
            disaster_time = random.randint(1, disaster_longevity)
            disaster_death_rate = random.random() * disaster_severity
            print(f'disaster! death rate {disaster_death_rate}')
        if disaster_time:
            disaster_time -= 1
            if disaster_time == 0:
                print(f'good times')
        else:
            disaster_death_rate = 0
        # death
        for person in alive:
            if random.randint(0, year - person.birth_date) > longevity:
                person.death_date = year
            if random.random() < base_death_rate:
                person.death_date = year
            if random.randint(0, len(alive)) > max_population:
                if random.random() < overpopulated_death_rate:
                    person.death_date = year
            if random.random() < disaster_death_rate:
                person.death_date = year
        alive = [person for person in alive if person.alive()]
    return people

def plot(lineage, life_expectancy):
    import dansplotcore as dpc
    plot = dpc.Plot()
    for i, person in enumerate(lineage):
        person.i = i
    for person in lineage:
        if person.alive():
            r=1.0
            g=1.0
        elif person.death_date - person.birth_date < life_expectancy:
            r=1.0
            g=0.0
        else:
            r=0.0
            g=1.0
        plot.line(
            person.i, person.birth_date,
            person.i, (person.death_date or person.birth_date + life_expectancy)+1,
            r, g, 0.0, 1.0,
        )
        if person.mother:
            plot.line(
                person.mother.i, person.birth_date-1,
                person.i, person.birth_date,
                1.0, 1.0, 0.0, 0.5,
            )
        if person.father:
            plot.line(
                person.father.i, person.birth_date-1,
                person.i, person.birth_date,
                0.0, 1.0, 1.0, 0.5,
            )
    plot.show()
