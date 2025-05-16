import random


class Hero:
    def __init__(self):
        self.max_HP = 15
        self.HP = 15
        self.AP = 2
        self.coins = 10
        self.protection = 0
        self.vulnerability_to_cold = True
        self.dead = False

    def get_HP(self):
        return self.HP

    def get_AP(self):
        return self.AP

    def get_vulnerability_to_cold(self):
        return self.vulnerability_to_cold

    def set_vulnerability_to_cold(self, new_status):
        self.vulnerability_to_cold = new_status

    def get_coin(self):
        return self.coins

    def set_coin(self, new_coins):
        self.coins = new_coins

    def set_AP(self, AP):
        self.AP = AP

    def set_HP(self, new_HP):
        self.HP = new_HP

    def get_dead(self):
        return self.dead

    def set_dead(self):
        self.dead = True

    def get_max_HP(self):
        return self.max_HP

    def set_max_HP(self, new_HP):
        self.max_HP = new_HP

    def get_protection(self):
        return self.protection

    def set_protection(self, new_protection):
        self.protection = new_protection


class Enemy:
    def __init__(self, HP, AP, distance):
        self.HP = HP
        self.AP = AP
        self.distance = distance
        self.dead = False

    def get_HP(self):
        return self.HP

    def set_HP(self, HP):
        self.HP = HP

    def get_AP(self):
        return self.AP

    def set_AP(self, AP):
        self.AP = AP

    def get_Dead(self):
        return self.dead

    def set_Dead(self):
        self.dead = True

    def get_distance(self):
        return self.distance

    def set_distance(self, new_distance):
        self.distance = new_distance


class The_Fallen_Guardian(Enemy):
    def __init__(self):
        self.HP = 16
        self.AP = 4
        self.distance = random.randint(1, 3)
        super().__init__(self.HP, self.AP, self.distance)

    def battle(self, attack, hero):
        if attack == 1:
            if self.get_distance() == 1:
                self.set_HP(self.get_HP() - hero.get_AP())
                result_attack = ('Ты наносишь решительный удар по Павшему Стражу сильно ранив его, но он всё ещё'
                                 ' стоит на ногах\n')
            elif self.get_distance() == 2:
                self.set_HP(self.get_HP() - (hero.AP / 2))
                hero.set_HP(hero.get_HP() - (self.get_AP() / 2))
                result_attack = ('Ты делаешь рывок в сторону Стража и насишь удар, но слишком слабый чтобы ошеломить'
                                 ' Павшего\n')
            else:
                hero.set_HP(hero.get_HP() - self.AP)
                result_attack = 'Пока ты несёшся к Стражу, он уже прицелился и попал по тебе из арбалета\n'
            if self.get_HP() <= 0:
                self.set_Dead()
                hero.set_HP(hero.max_HP)
                return ('Ты наносишь последний удар, и Страж падает на землю, его доспехи разлетаются в разные стороны.'
                        ' Он больше не может встать, его тень исчезает из этого мира.\n')
            if hero.get_HP() <= 0:
                hero.set_dead()
                return ('Ты падаешь на колени, меч скользит из твоих рук, и тёмная фигура Стража приближается.'
                        ' Его оружие холодно блескнет, а ты ощущаешь, как мир вокруг поглощается тьмой.')
            return (f"{result_attack}"
                    f"HP у вас: {hero.get_HP()}\n"
                    f"HP у Стража: {self.get_HP()}\n"
                    f"{self.set_distance_battle(random.randint(1, 3))}\n")
        elif attack == 2:
            if self.get_distance() == 2:
                self.set_HP(self.get_HP() - hero.get_AP())
                result_attack = 'Ты стреляешь из арбалета и попадаешь в слабую точку Стража\n'
            elif self.get_distance() == 3:
                self.set_HP(self.get_HP() - (hero.AP / 2))
                hero.set_HP(hero.get_HP() - (self.get_AP() / 2))
                result_attack = 'Ты долго прицеливаешся, из-за этого Страж успевает попасть по тебе, но и ты ранил его\n'
            else:
                hero.set_HP(hero.get_HP() - self.AP)
                result_attack = 'Ты пытаешся достать арбалет, но Страж откидывает тебя на несколько метров\n'
            if self.get_HP() <= 0:
                self.set_Dead()
                hero.set_HP(hero.max_HP)
                return ('Ты выстреливаешь в Стража, и его броня не выдерживает удара. Он падает на землю, и его силуэт'
                        ' растворяется в тени. Ты видишь, как его тело теряет форму.\n')
            if hero.get_HP() <= 0:
                hero.set_dead()
                return ('Твой выстрел был неудачным. Ты ощущаешь, как силы покидают тебя, и Страж медленно приближается.'
                        ' Его взгляд пуст, а руки сжаты в кулаки, готовые нанести последний удар.')
            return (f"{result_attack}"
                    f"HP у вас: {hero.get_HP()}\n"
                    f"HP у Стража: {self.get_HP()}\n"
                    f"{self.set_distance_battle(random.randint(1, 3))}\n")
        elif attack == 3:
            if self.get_distance() == 3:
                self.set_HP(self.get_HP() - hero.get_AP())
                result_attack = 'Страж пытается увернутся, но шар взрывается возле него, расплавляя его броню\n'
            elif self.get_distance() == 1:
                self.set_HP(self.get_HP() - (hero.AP / 2))
                hero.set_HP(hero.get_HP() - (self.get_AP() / 2))
                result_attack = 'Вы не успеваете отправить шар и он взрывается возле вас, нанося урон и вам, и Павшему\n'
            else:
                hero.set_HP(hero.get_HP() - self.AP)
                result_attack = ('Шар пролетает возле противника и взрывается сильно позже, давая возможность Стражу'
                                 ' нанести контр-удар\n')
            if self.get_HP() <= 0:
                self.set_Dead()
                hero.set_HP(hero.max_HP)
                return ('Огненный шар поражает Стража, и его броня плавится. '
                        'Ты видишь, как его тело исчезает в огне, и его тень больше не существует.\n')
            if hero.get_HP() <= 0:
                hero.set_dead()
                return ('Ты запускаешь огненный шар, но Страж успешно отражает его магией. Он приближается, '
                        'его глаза полны презрения. Ты не можешь больше двигаться, и он наносит последний смертельный'
                        ' удар.')
            return (f"{result_attack}"
                    f"HP у вас: {hero.get_HP()}\n"
                    f"HP у Стража: {self.get_HP()}\n"
                    f"{self.set_distance_battle(random.randint(1, 3))}\n")

    def set_distance_battle(self, new_distance):
        if self.get_distance() == new_distance:
            return f"Страж остаётся на своём месте. Дистанция до него: {new_distance}"
        elif self.get_distance() == 1:
            self.set_distance(new_distance)
            if new_distance == 2:
                return (f"Страж резко отступает, сохраняя щит перед собой."
                        f" Он готовит атаку на более удобной для себя дистанции. Дистанция до него: {new_distance}")
            else:
                return (f"Ты ожидаешь его атаки, но Страж отступает, поднимая свой щит перед собой,"
                        f" и быстро отходит назад, готовя арбалет для следующего выстрела. Дистанция до него:"
                        f" {new_distance}")
        elif self.get_distance() == 2:
            self.set_distance(new_distance)
            if new_distance == 3:
                return (f"Павший скрывает своё лицо за щитом и отступает на безопасное расстояние,"
                        f" подготавливая новую тактику для дальнего боя. Дистанция до него: {new_distance}")
            else:
                return (f"Страж ускоряет шаги и с ужасной силой бросается вперёд, пытаясь подавить твою оборону."
                        f" Дистанция до него: {new_distance}")
        elif self.get_distance() == 3:
            self.set_distance(new_distance)
            if new_distance == 2:
                return (f"Страж решает переместится поближе к тебе, предварительно приготовясь к удару. "
                        f"Дистанция до него: {new_distance}")
            else:
                return (f"Страж оставляет арбалет и стремительно приближается, его шаги тяжело звучат по земле."
                        f" Готовься — теперь его удар будет молниеносным.."
                        f" Дистанция до него: {new_distance}")


class The_Dark_Knight(Enemy):
    def __init__(self):
        self.HP = 30
        self.AP = 6
        self.distance = random.randint(1, 3)
        super().__init__(self.HP, self.AP, self.distance)

    def battle(self, attack, hero):
        if hero.get_vulnerability_to_cold():
            hero.set_HP(hero.get_HP() - 1)
        if attack == 1:
            if self.get_distance() == 1:
                self.set_HP(self.get_HP() - hero.get_AP())
                result_attack = ('Ты метишь своим мечом, и удар точно находит цель, но Тёмный рыцарь лишь сжимает зубы,'
                                 ' не давая себе ни малейшего признака боли.\n')
            elif self.get_distance() == 2:
                self.set_HP(self.get_HP() - (hero.AP / 2))
                hero.set_HP(hero.get_HP() - ((self.get_AP() - 2) / 2))
                result_attack = ('Ты пытаешься пробить защиту рыцаря, но его чёрный щит сдерживает удар,'
                                 ' и он контратакует с яростью.\n')
            else:
                hero.set_HP(hero.get_HP() - (self.get_AP() - 2))
                result_attack = ('Ты размахиваешь мечом в воздухе, но Тёмный рыцарь слишком далеко. В ответ он'
                                 ' выстреливает тёмным магическим снарядом, нанося удар по тебе.\n')
            if self.get_HP() <= 0:
                self.set_Dead()
                hero.set_HP(hero.max_HP)
                return ('Тёмный рыцарь падает от твоего удара, его броня трещит. Ты видишь, как его меч теряет свет,'
                        ' и он перестает двигаться. Ты победил его, но его смерть оставляет зловещий след.\n')
            if hero.get_HP() <= 0:
                hero.set_dead()
                return ('Твои силы истощаются, и ты падаешь на землю. Тёмный рыцарь стоит над тобой, его тяжёлый'
                        ' меч готов к последнему удару. Ты видишь, как он медленно поднимает оружие,'
                        ' и последняя тень поглощает тебя.')
            return (f"{result_attack}"
                    f"HP у вас: {hero.get_HP()}\n"
                    f"HP у Рыцаря: {self.get_HP()}\n"
                    f"{self.set_distance_battle(random.randint(1, 3))}\n")
        elif attack == 2:
            if self.get_distance() == 2:
                self.set_HP(self.get_HP() - hero.get_AP())
                result_attack = ('Ты выпустил болт, и он проникает в рыцаря. Тёмный рыцарь сдерживает боль,'
                                 ' но ты видишь, как его броня покрывается трещинами.\n')
            elif self.get_distance() == 3:
                self.set_HP(self.get_HP() - (hero.AP / 2))
                hero.set_HP(hero.get_HP() - ((self.get_AP() - 2) / 2))
                result_attack = ('Ты стреляешь из арбалета, и болт попадет в рыцаря, но он использует магическую защиту,'
                                 ' и часть урона возвращается к тебе.\n')
            else:
                hero.set_HP(hero.get_HP() - (self.get_AP() - 2))
                result_attack = ('Ты пытаешься выстрелить, но рыцарь внезапно приближается, сбивая твой прицел.'
                                 ' Тёмная магия от его щита обжигает тебя.\n')
            if self.get_HP() <= 0:
                self.set_Dead()
                hero.set_HP(hero.max_HP)
                return ('Твой выстрел пробивает Тёмного рыцаря, и его фигура теряет устойчивость. Его меч падает,'
                        ' и ты видишь, как он исчезает в темноте, оставляя только пустую броню.\n')
            if hero.get_HP() <= 0:
                hero.set_dead()
                return ('Ты попытался выстрелить, но арбалет не успевает повернуться на цель. Тёмный рыцарь ударяет'
                        ' тебя, и ты ощущаешь, как холод проникает в твои кости, а всё вокруг теряет цвет.')
            return (f"{result_attack}"
                    f"HP у вас: {hero.get_HP()}\n"
                    f"HP у Рыцаря: {self.get_HP()}\n"
                    f"{self.set_distance_battle(random.randint(1, 3))}\n")
        elif attack == 3:
            if self.get_distance() == 3:
                self.set_HP(self.get_HP() - hero.get_AP())
                result_attack = ('Ты выпускаешь огненный шар, и он сжирает рыцаря. Его черные глаза вспыхивают злобой,'
                                 ' но он выдерживает атаку, оставаясь на ногах.\n')
            elif self.get_distance() == 1:
                self.set_HP(self.get_HP() - (hero.AP / 2))
                hero.set_HP(hero.get_HP() - ((self.get_AP() - 2) / 2))
                result_attack = ('Ты выпускаешь огненный шар, и он точно задевает рыцаря. Но его тёмная аура поглощает'
                                 ' большую часть урона, и он сам наносит ответный удар.\n')
            else:
                hero.set_HP(hero.get_HP() - (self.get_AP() - 2))
                result_attack = ('Ты пытаешься атаковать, но рыцарь ловко уклоняется от огненного шара,'
                                 ' а тёмная энергия вокруг него сжигает твои силы.\n')
            if self.get_HP() <= 0:
                self.set_Dead()
                hero.set_HP(hero.max_HP)
                return ('Ты запускаешь огненный шар в Тёмного рыцаря, и его броня трещит.'
                        ' Он падает на колени, его меч соскальзывает с руки, и тёмная энергия покидает его тело.\n')
            if hero.get_HP() <= 0:
                hero.set_dead()
                return ('Ты запускаешь огненный шар, но Тёмный рыцарь отражает его своим щитом. '
                        'Его меч вонзается в тебя, а его глаза наполнены жестокой решимостью.')
            return (f"{result_attack}"
                    f"HP у вас: {hero.get_HP()}\n"
                    f"HP у Рыцаря: {self.get_HP()}\n"
                    f"{self.set_distance_battle(random.randint(1, 3))}\n")

    def set_distance_battle(self, new_distance):
        if self.get_distance() == new_distance:
            return f"Тёмный рыцарь остаётся на своём месте. Дистанция до него: {new_distance}"
        elif self.get_distance() == 1:
            self.set_distance(new_distance)
            if new_distance == 2:
                return (f"Он отходит на безопасное расстояние, тем самым усиливая свою магическую защиту."
                        f" Его взгляд не отрывается от тебя. Дистанция до него: {new_distance}")
            else:
                return (f"Он резко отступает, делая шаг назад и оставляя тебя на более дальнем расстоянии."
                        f" Он подготавливает свои магические силы для следующей атаки. Дистанция до него:"
                        f" {new_distance}")
        elif self.get_distance() == 2:
            self.set_distance(new_distance)
            if new_distance == 3:
                return (f"Он отступает назад, готовя магическую атаку, и твоя очередная атака не успевает найти цель."
                        f" Теперь он поднимет свою тёмную силу на дальнем расстоянии.: {new_distance}")
            else:
                return (f"Он не торопится, но делает шаг назад, не давая тебе времени на манёвры."
                        f" Он готовится провести свою атаку."
                        f" Дистанция до него: {new_distance}")
        elif self.get_distance() == 3:
            self.set_distance(new_distance)
            if new_distance == 2:
                return (f"Он уменьшает расстояние, его шаги становятся более уверенными. Тёмная аура всё сильнее"
                        f" окружает его.: {new_distance}")
            else:
                return (f"Вдруг он ускоряется, на глазах сокращая дистанцию. Его меч готов принять твою защиту,"
                        f" и он кидается в бой."
                        f" Дистанция до него: {new_distance}")


class The_Lich_King(Enemy):
    def __init__(self):
        self.HP = 80
        self.AP = 10
        self.marten_spell = False
        self.coof_AP_hero = 1
        self.distance = random.randint(1, 3)
        super().__init__(self.HP, self.AP, self.distance)

    def battle(self, attack, hero):
        if hero.get_vulnerability_to_cold():
            hero.set_HP(hero.get_HP() - 2)
        if attack == 1:
            if self.get_distance() == 1:
                self.set_HP(self.get_HP() - (hero.get_AP() * self.coof_AP_hero))
                result_attack = ('Ты метишь своим мечом, и удар точно находит цель, но Тёмный рыцарь лишь сжимает зубы,'
                                 ' не давая себе ни малейшего признака боли.\n')
            elif self.get_distance() == 2:
                self.set_HP(self.get_HP() - (hero.get_AP() * self.coof_AP_hero) / 2)
                hero.set_HP(hero.get_HP() - ((self.get_AP() - 2) / 2))
                result_attack = ('Ты пытаешься пробить защиту рыцаря, но его чёрный щит сдерживает удар,'
                                 ' и он контратакует с яростью.\n')
            else:
                hero.set_HP(hero.get_HP() - (self.get_AP() - 2))
                result_attack = ('Ты размахиваешь мечом в воздухе, но Тёмный рыцарь слишком далеко. В ответ он'
                                 ' выстреливает тёмным магическим снарядом, нанося удар по тебе.\n')
            if self.get_HP() <= 0:
                self.set_Dead()
                hero.set_HP(hero.max_HP)
                return ''
            if hero.get_HP() <= 0:
                hero.set_dead()
                return ('Ты пытаешься сопротивляться, но ледяная магия Лича проникает в твоё тело. Всё, что ты ощущаешь'
                        ' — холод и темные огни, когда ты теряешь сознание. Твоя душа покидает это тело.')
            return (f"{result_attack}"
                    f"HP у вас: {hero.get_HP()}\n"
                    f"HP у Лича: {self.get_HP()}\n"
                    f"{self.set_distance_battle(random.randint(1, 3))}\n")
        elif attack == 2:
            if self.get_distance() == 2:
                self.set_HP(self.get_HP() - (hero.get_AP() * self.coof_AP_hero))
                result_attack = ('Ты выпустил болт, и он проникает в рыцаря. Тёмный рыцарь сдерживает боль,'
                                 ' но ты видишь, как его броня покрывается трещинами.\n')
            elif self.get_distance() == 3:
                self.set_HP(self.get_HP() - (hero.get_AP() * self.coof_AP_hero) / 2)
                hero.set_HP(hero.get_HP() - ((self.get_AP() - 2) / 2))
                result_attack = (
                    'Ты стреляешь из арбалета, и болт попадет в рыцаря, но он использует магическую защиту,'
                    ' и часть урона возвращается к тебе.\n')
            else:
                hero.set_HP(hero.get_HP() - (self.get_AP() - 2))
                result_attack = ('Ты пытаешься выстрелить, но рыцарь внезапно приближается, сбивая твой прицел.'
                                 ' Тёмная магия от его щита обжигает тебя.\n')
            if self.get_HP() <= 0:
                self.set_Dead()
                hero.set_HP(hero.max_HP)
                return ''
            if hero.get_HP() <= 0:
                hero.set_dead()
                return ('Ты стреляешь, но твой болт не достигает цели. Лич медленно приближается, его ледяные глаза'
                        ' смотрят прямо на тебя. Ты чувствуешь, как тьма поглощает твою душу.')
            return (f"{result_attack}"
                    f"HP у вас: {hero.get_HP()}\n"
                    f"HP у Лича: {self.get_HP()}\n"
                    f"{self.set_distance_battle(random.randint(1, 3))}\n")
        elif attack == 3:
            if self.get_distance() == 3:
                self.set_HP(self.get_HP() - (hero.get_AP() * self.coof_AP_hero))
                result_attack = ('Ты выпускаешь огненный шар, и он сжирает рыцаря. Его черные глаза вспыхивают злобой,'
                                 ' но он выдерживает атаку, оставаясь на ногах.\n')
            elif self.get_distance() == 1:
                self.set_HP(self.get_HP() - (hero.get_AP() * self.coof_AP_hero) / 2)
                hero.set_HP(hero.get_HP() - ((self.get_AP() - 2) / 2))
                result_attack = ('Ты выпускаешь огненный шар, и он точно задевает рыцаря. Но его тёмная аура поглощает'
                                 ' большую часть урона, и он сам наносит ответный удар.\n')
            else:
                hero.set_HP(hero.get_HP() - (self.get_AP() - 2))
                result_attack = ('Ты пытаешься атаковать, но рыцарь ловко уклоняется от огненного шара,'
                                 ' а тёмная энергия вокруг него сжигает твои силы.\n')
            if self.get_HP() <= 0:
                self.set_Dead()
                hero.set_HP(hero.max_HP)
                return ""
            if hero.get_HP() <= 0:
                hero.set_dead()
                return ('Ты запускаешь огненный шар, но Лич его поглощает, и ты ощущаешь, как ледяные цепи сжимаются'
                        ' вокруг твоего сердца. Тёмный свет окутывает твою душу, и ты теряешь сознание.')
            return (f"{result_attack}"
                    f"HP у вас: {hero.get_HP()}\n"
                    f"HP у Лича: {self.get_HP()}\n"
                    f"{self.set_distance_battle(random.randint(1, 3))}\n")
        elif attack == 4:
            self.marten_spell = True
            self.coof_AP_hero = 1.5
            result_attack = ('Ты произносишь заклинание, и волна энергии охватывает тебя. Мартен появляется в тени,'
                             ' его светлая сила наполняет тебя, придавая уверенности и защиты от темных чар Лича.\n')
            return (f"{result_attack}"
                    f"HP у вас: {hero.get_HP()}\n"
                    f"HP у Лича: {self.get_HP()}\n"
                    f"{self.set_distance_battle(random.randint(1, 3))}\n")
        elif attack == 5:
            self.set_HP(self.get_HP() - 20)
            result_attack = ('Ты усиливаешь заклинание, концентрируя всё своё внимание на магии. Мощная энергия проходит'
                             ' через твои руки, и ты чувствуешь, как твоё тело наполняется силой,'
                             ' готовой сломать ледяную защиту Лича.\n')
            if self.get_HP() <= 0:
                self.set_Dead()
                return ""
            return (f"{result_attack}"
                    f"HP у вас: {hero.get_HP()}\n"
                    f"HP у Лича: {self.get_HP()}\n"
                    f"{self.set_distance_battle(random.randint(1, 3))}\n")

    def set_distance_battle(self, new_distance):
        if self.get_distance() == new_distance:
            return f"Тёмный рыцарь остаётся на своём месте. Дистанция до него: {new_distance}"
        elif self.get_distance() == 1:
            self.set_distance(new_distance)
            if new_distance == 2:
                return (f"Он отходит на безопасное расстояние, тем самым усиливая свою магическую защиту."
                        f" Его взгляд не отрывается от тебя. Дистанция до него: {new_distance}")
            else:
                return (f"Он резко отступает, делая шаг назад и оставляя тебя на более дальнем расстоянии."
                        f" Он подготавливает свои магические силы для следующей атаки. Дистанция до него:"
                        f" {new_distance}")
        elif self.get_distance() == 2:
            self.set_distance(new_distance)
            if new_distance == 3:
                return (f"Он отступает назад, готовя магическую атаку, и твоя очередная атака не успевает найти цель."
                        f" Теперь он поднимет свою тёмную силу на дальнем расстоянии.: {new_distance}")
            else:
                return (f"Он не торопится, но делает шаг назад, не давая тебе времени на манёвры."
                        f" Он готовится провести свою атаку."
                        f" Дистанция до него: {new_distance}")
        elif self.get_distance() == 3:
            self.set_distance(new_distance)
            if new_distance == 2:
                return (f"Он уменьшает расстояние, его шаги становятся более уверенными. Тёмная аура всё сильнее"
                        f" окружает его.: {new_distance}")
            else:
                return (f"Вдруг он ускоряется, на глазах сокращая дистанцию. Его меч готов принять твою защиту,"
                        f" и он кидается в бой."
                        f" Дистанция до него: {new_distance}")
