class Hero:
    def __init__(self, HP, MN, close_combat_skil, long_range_combat_skil, magic_skil):
        self.HP = HP
        self.MN = MN
        self.first_weapon_slot = Weapon
        self.second_weapon_slot = Weapon
        self.armor = Armor
        self.potions = {'small_XP': 0, 'medium_XP': 0, 'heavy_XP': 0, 'small_MN': 0, 'medium_MN': 0, 'heavy_MN': 0}
        self.close_combat_skil = close_combat_skil
        self.long_range_combat_skil = long_range_combat_skil
        self.magic_skil = magic_skil
        self.dead = False

    def get_skil_close_combat(self):
        return self.close_combat_skil

    def get_skil_long_range_combat(self):
        return self.long_range_combat_skil

    def get_skil_magic(self):
        return self.magic_skil

    def get_first_weapon(self):
        return self.first_weapon_slot

    def get_second_weapon(self):
        return self.second_weapon_slot

    def set_first_weapon(self, weapon):
        self.first_weapon_slot = weapon

    def set_second_weapon(self, weapon):
        self.second_weapon_slot = weapon

    def get_HP(self):
        return self.HP

    def get_potions(self, potion):
        return self.potions.get(potion)

    def set_potions(self, potion, new_count):
        self.potions[potion] = new_count

    def set_HP(self, new_HP):
        self.HP = new_HP

    def get_MN(self):
        return self.MN

    def set_MN(self, new_MN):
        self.MN = new_MN

    def get_dead(self):
        return self.dead

    def set_dead(self):
        self.dead = True

    def get_armor(self):
        return self.armor

    def set_armor(self, new_armor):
        self.armor = new_armor

    def attack(self, enemy, slot):
        if slot == 1:
            weapon = self.first_weapon_slot
        else:
            weapon = self.second_weapon_slot

        self.set_MN(self.get_MN() - weapon.get_MN_consumption())
        if enemy.get_HP() <= 0:
            enemy.set_Dead()
        else:
            self.set_HP(self.get_HP() - self)
            if self.get_HP():
                self.set_dead()


class Mag(Hero):
    def __init__(self):
        self.HP = 100
        self.MN = 200
        self.close_combat_skil = False
        self.long_range_combat_skil = False
        self.magic_skil = True
        super().__init__(self.HP, self.MN, self.close_combat_skil, self.long_range_combat_skil, self.magic_skil)
        self.set_armor(Armor(8, 5, 5, 45))


class Archer(Hero):
    def __init__(self):
        self.HP = 100
        self.MN = 150
        self.close_combat_skil = False
        self.long_range_combat_skil = True
        self.magic_skil = False
        super().__init__(self.HP, self.MN, self.close_combat_skil, self.long_range_combat_skil, self.magic_skil)


class Warrior(Hero):
    def __init__(self):
        self.HP = 200
        self.MN = 100
        self.close_combat_skil = True
        self.long_range_combat_skil = False
        self.magic_skil = False
        super().__init__(self.HP, self.MN, self.close_combat_skil, self.long_range_combat_skil, self.magic_skil)


class Enemy:
    def __init__(self, HP, AP, RCC, RLC, RMC):
        self.HP = HP
        self.AP = AP
        self.resistance_CC = RCC
        self.resistance_LC = RLC
        self.resistance_MC = RMC
        self.dead = False

    def get_HP(self):
        return self.HP

    def set_HP(self, HP):
        self.HP = HP

    def get_AP(self):
        return self.AP

    def get_resistance_CC(self):
        return self.resistance_CC

    def set_resistance_CC(self, new_resistance):
        self.resistance_CC = new_resistance

    def get_resistance_LC(self):
        return self.resistance_CC

    def set_resistance_LC(self, new_resistance):
        self.resistance_LC = new_resistance

    def get_resistance_MC(self):
        return self.resistance_CC

    def set_resistance_MC(self, new_resistance):
        self.resistance_MC = new_resistance

    def set_AP(self, AP):
        self.AP = AP

    def get_Dead(self):
        return self.dead

    def set_Dead(self):
        self.dead = True


class Item:
    def __init__(self, type_item):
        self.regen_HP = 0
        self.regen_MN = 0
        self.clas_uses = ''
        self.destination = ''
        self.weight = 0
        self.type = self.specifications_item(type_item)

    def specifications_item(self, type_item):
        if 1 <= type_item <= 3:
            if type_item == 1:
                self.set_regen_HP(50)
                self.destination = 'regen_XP'
                self.clas_uses = 'All'
                return type_item
            elif type_item == 2:
                self.set_regen_HP(100)
                self.destination = 'regen_XP'
                self.clas_uses = 'All'
                return type_item
            elif type_item == 3:
                self.set_regen_HP(150)
                self.destination = 'regen_XP'
                self.clas_uses = 'All'
                return type_item
        elif 4 <= type_item <= 6:
            if type_item == 4:
                self.set_regen_MN(50)
                self.destination = 'regen_MN'
                self.clas_uses = 'All'
                return type_item
            elif type_item == 5:
                self.set_regen_MN(100)
                self.destination = 'regen_MN'
                self.clas_uses = 'All'
                return type_item
            elif type_item == 6:
                self.set_regen_MN(150)
                self.destination = 'regen_MN'
                self.clas_uses = 'All'
                return type_item
        elif 7 <= type_item <= 9:
            if type_item == 7:
                self.destination = 'light_armor'
                self.clas_uses = 'All'
                self.set_weight(5)
                return type_item
            elif type_item == 8:
                self.destination = 'medium_armor'
                self.clas_uses = 'All'
                self.set_weight(15)
                return type_item
            elif type_item == 9:
                self.destination = 'heavi_armor'
                self.clas_uses = 'All'
                self.set_weight(15)
                return type_item
        elif 10 <= type_item <= 12:
            if type_item == 10:
                self.destination = 'CC_weapon'
                self.clas_uses = 'Warrior'
                return type_item
            elif type_item == 11:
                self.destination = 'LC_weapon'
                self.clas_uses = 'Archer'
                return type_item
            elif type_item == 12:
                self.destination = 'MC_weapon'
                self.clas_uses = 'Mag'
                return type_item

    def get_regen_HP(self):
        return self.regen_HP

    def set_regen_HP(self, new_regen):
        self.regen_HP = new_regen

    def get_weight(self):
        return self.weight

    def set_weight(self, new_weight):
        self.weight = new_weight

    def get_regen_MN(self):
        return self.regen_MN

    def set_regen_MN(self, new_regen):
        self.regen_MN = new_regen

    def get_clas(self):
        return self.clas_uses

    def set_clas(self, new_class):
        self.clas_uses = new_class

    def get_destination(self):
        return self.destination

    def set_destination(self, new_destination):
        self.destination = new_destination


class Armor(Item):
    def __init__(self, tipe, RCC, RLC, RMC):
        self.resistance_CC = RCC
        self.resistance_LC = RLC
        self.resistance_MC = RMC
        self.destination = ''
        self.weight = 0
        self.type = self.specifications_item(tipe)

        super().__init__(self.type)


class Weapon(Item):
    def __init__(self, tipe, AP, MN_consumption):
        self.AP = AP
        self.MN_consumption = MN_consumption
        self.clas_uses = ''
        self.destination = ''
        self.type = self.specifications_item(tipe)
        super().__init__(self.type)

    def get_AP(self):
        return self.AP

    def set_AP(self, new_AP):
        self.AP = new_AP

    def get_MN_consumption(self):
        return self.MN_consumption

    def set_MN_consumption(self, new_MN_consumption):
        self.MN_consumption = new_MN_consumption


class Regen(Item):
    def __init__(self, tipe):
        self.regen_HP = 0
        self.regen_MN = 0
        self.type = self.specifications_item(tipe)
        self.destination = ''
        super().__init__(self.type)


hero = Mag()
armor = hero.get_armor()
print(armor.get_weight())
print(hero.set_potions('small_MN', 2))
