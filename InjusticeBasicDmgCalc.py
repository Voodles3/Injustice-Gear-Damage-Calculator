import math
char_stats = [None] * 3
def main():
      print('\nInjustice Basic Damage Gear Calculator')

      list_of_gear_tuples = get_gears()

      num_gears_to_combine = get_valid_int_input('Enter 1 for single gears, 2 for combinations of 2 gears, or 3 for combinations for 3 gears: ', [1, 2, 3])

      list_all_gears = True if get_valid_int_input('Enter 1 to display all combinations, enter 2 to only display the best combination: ', [1, 2]) == 1 else False

      num_gears = len(list_of_gear_tuples)
      num_combinations = int((math.factorial(num_gears)) / (math.factorial(num_gears - num_gears_to_combine) * math.factorial(num_gears_to_combine)))
      get_char_stats()

      if num_gears_to_combine == 1:
            gear_stats = []
            for i, gear in enumerate(list_of_gear_tuples):
                  gear_stats.append(calculate_expected_damage(gear[0], gear[1], gear[2])[0])

            calculated_gears = {k:v for (k,v) in zip(list_of_gear_tuples, gear_stats)}

            if not list_all_gears:
                  best_result_key = max(calculated_gears, key=calculated_gears.get)

                  print(f'\nBest single gear is: {best_result_key}')
                  expected_dmg = calculate_expected_damage(best_result_key[0], best_result_key[1], best_result_key[2])
                  log_final_result(expected_dmg)
            else:
                  sorted_gears = dict(sorted(calculated_gears.items(), key=lambda x: x[1], reverse=True))

                  print(f'\n{num_combinations} Results, sorted from best to worst:')
                  gears_iterator = iter(sorted_gears)
                  for _ in range(len(sorted_gears)):
                        this_gear = next(gears_iterator)
                        print(f'\n{this_gear}: ')
                        expected_dmg = calculate_expected_damage(this_gear[0], this_gear[1], this_gear[2])
                        log_final_result(expected_dmg)


      elif num_gears_to_combine == 2:
            gear_pairs = []
            for i in range(len(list_of_gear_tuples)):
                  for j in range(i+1, len(list_of_gear_tuples)):
                        gear_pairs.append((list_of_gear_tuples[i], list_of_gear_tuples[j]))

            gear_combo_stats = []
            for gear_pair in gear_pairs:
                  gear_combo_stats.append(combine_gears(gear_pair[0], gear_pair[1])[0])

            calculated_gears = {k:v for (k,v) in zip(gear_pairs, gear_combo_stats)}

            if not list_all_gears:
                  best_result_key = max(calculated_gears, key=calculated_gears.get)

                  print(f'\nBest gear combo is: {best_result_key}')
                  expected_dmg = combine_gears(best_result_key[0], best_result_key[1])
                  log_final_result(expected_dmg)
            else:
                  sorted_gears = dict(sorted(calculated_gears.items(), key=lambda x: x[1], reverse=True))

                  print(f'\n{num_combinations} Results, sorted from best to worst:')
                  gears_iterator = iter(sorted_gears)
                  for _ in range(len(sorted_gears)):
                        this_gear_pair = next(gears_iterator)
                        print (f'\n{this_gear_pair}: ')
                        expected_dmg = combine_gears(this_gear_pair[0], this_gear_pair[1])
                        log_final_result(expected_dmg)
            
            
      elif num_gears_to_combine == 3:
            gear_triplets = []
            for i in range(len(list_of_gear_tuples)):
                  for j in range(i + 1, len(list_of_gear_tuples)):
                        for k in range(j + 1, len(list_of_gear_tuples)):
                              gear_triplets.append((list_of_gear_tuples[i], list_of_gear_tuples[j], list_of_gear_tuples[k]))

            gear_combo_stats = []
            for gear_triplet in gear_triplets:
                  gear_combo_stats.append(combine_gears(gear_triplet[0], gear_triplet[1], gear_triplet[2])[0])
            
            calculated_gears = {k:v for (k,v) in zip(gear_triplets, gear_combo_stats)}

            if not list_all_gears:
                  best_result_key = max(calculated_gears, key=calculated_gears.get)

                  print(f'\nBest gear combo is: {best_result_key}')
                  expected_dmg = combine_gears(best_result_key[0], best_result_key[1], best_result_key[2])
                  log_final_result(expected_dmg)
            else:
                  sorted_gears = dict(sorted(calculated_gears.items(), key=lambda x: x[1], reverse=True))

                  print(f'\n{num_combinations} Results, sorted from best to worst:')
                  gears_iterator = iter(sorted_gears)
                  for _ in range(len(sorted_gears)):
                        this_gear_triplet = next(gears_iterator)
                        print (f'\n{this_gear_triplet}: ')
                        expected_dmg = combine_gears(this_gear_triplet[0], this_gear_triplet[1], this_gear_triplet[2])
                        log_final_result(expected_dmg)
      offer_restart()

def get_gears():
      while True:
            try:
                  gears_input_string = input('Enter your gears. Separate gear values with commas, and separate different gears with semicolons.\n')
                  list_of_gear_tuples = [tuple(map(lambda x: float(x) / 100, tpl.split(','))) for tpl in gears_input_string.split(';')]
                  return list_of_gear_tuples
            except:
                  print('\nInvalid input. Please enter valid numeric values.')

def get_valid_int_input(prompt, valid_options):
      while True:
            try:
                  user_input = int(input(prompt))
                  if user_input in valid_options:
                        return user_input
                  else:
                        print(f'\nInvalid input. Please enter one of these valid options: {valid_options}')
            except:
                  print('\nInvalid input. Please enter a valid integer.')
      
def combine_gears(gear_1, gear_2, gear_3=[0,0,0]):
      gear_dmg = gear_1[0] + gear_2[0] + gear_3[0]
      gear_crit_chance = gear_1[1] + gear_2[1] + gear_3[1]
      gear_crit_dmg = gear_1[2] + gear_2[2] + gear_3[2]

      return calculate_expected_damage(gear_dmg, gear_crit_chance, gear_crit_dmg)
        
def calculate_expected_damage(gear_dmg, gear_crit_chance, gear_crit_dmg):
      total_crit_chance = clamp(char_stats[1] + gear_crit_chance, 0, 1)
      total_crit_dmg = char_stats[2] + gear_crit_dmg
      total_non_crit_hit_dmg = char_stats[0] * (gear_dmg + 1)
      total_crit_hit_dmg = total_non_crit_hit_dmg * total_crit_dmg
      return [
            (total_crit_chance * total_crit_hit_dmg) + ((1 - total_crit_chance) * total_non_crit_hit_dmg),
              total_non_crit_hit_dmg,
              total_crit_hit_dmg
      ]

def get_char_stats():
      char_stats[0] = float(''.join(char for char in input('Please enter character base damage: ') if char.isdigit()))
      global char_base_dmg
      char_base_dmg = char_stats[0]
      char_stats[1] = float(''.join(char for char in input('Please enter character crit chance in percentage: ') if char.isdigit())) / 100
      char_stats[2] = float(''.join(char for char in input('Please enter character crit damage in percentage (min 150): ') if char.isdigit())) / 100
      return char_stats

def log_final_result(expected_damage_values):
      print(f'\nAverage expected damage is: {expected_damage_values[0]}')
      print(f'Average expected damage multiplier is: {expected_damage_values[0] / char_base_dmg}')
      print(f'Non-crit hit damage is: {expected_damage_values[1]}')
      print(f'Crit hit damage is: {expected_damage_values[2]}')

def offer_restart():
      restart = input('\nRestart? (Y/N) ')
      while restart.lower() not in ['y', 'n']:
            restart = input('Restart? (Y/N) ')

      if restart == 'y':
            print('Restarting Application...')
            main()
      else:
            print('Quitting Application...')
            quit()

def clamp(num, min_value, max_value):
      return max(min(num, max_value), min_value)

if __name__ == '__main__':
    main()