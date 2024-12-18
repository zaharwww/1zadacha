import random
import time

class Fighter:
    def __init__(self, name: str, health: float, damage: list[float, float], attack_speed: list[float, float]):
        self.name = name
        self.health = health
        self.damage = damage
        self.attack_speed = attack_speed

    def __sub__(self, other):
        damage = random.uniform(other.damage[0], other.damage[1])
        self.health -= damage
        return round(damage, 2)

    def delay(self):
        return random.uniform(self.attack_speed[0], self.attack_speed[1])

def fight(fighter1: Fighter, fighter2: Fighter):
    start_time = time.time()
    with open("logger.txt", "w") as log_file:
        log_file.write("Начало сражения\n")

        next_attack_f1 = start_time + fighter1.delay()
        next_attack_f2 = start_time + fighter2.delay()

        while fighter1.health > 0 and fighter2.health > 0:
            current_time = time.time()

            if current_time >= next_attack_f1:
                damage = fighter2 - fighter1
                log_file.write(f"[{round(current_time - start_time, 2)}s] "
                               f"{fighter1.name} наносит {damage} урона. "
                               f"{fighter2.name}: {round(fighter2.health, 2)} HP\n")
                next_attack_f1 = current_time + fighter1.delay()

            if current_time >= next_attack_f2:
                damage = fighter1 - fighter2
                log_file.write(f"[{round(current_time - start_time, 2)}s] "
                               f"{fighter2.name} наносит {damage} урона. "
                               f"{fighter1.name}: {round(fighter1.health, 2)} HP\n")
                next_attack_f2 = current_time + fighter2.delay()

            time.sleep(0.01)

        winner = fighter1.name if fighter1.health > 0 else fighter2.name
        log_file.write(f"Победитель: {winner}!\n")
        print(f"Победитель: {winner}!")

if __name__ == "__main__":
    fighter1 = Fighter("Воин", 10, [5, 10], [1, 2])
    fighter2 = Fighter("Рыцарь", 10, [6, 9], [1.5, 2.5])
    fight(fighter1, fighter2)
