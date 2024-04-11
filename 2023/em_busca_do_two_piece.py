MIN_NUMBER_OF_ELEMENTS_TO_IDENTIFY_PROGRESSION = 3

number_of_numbers = int(input())
possible_sequence = list(map(int, input().split()))

if number_of_numbers < MIN_NUMBER_OF_ELEMENTS_TO_IDENTIFY_PROGRESSION:
    print("Finalmente! O Two Piece sera meu e vou me tornar rei dos piratas!")
    exit(0)

first_term = possible_sequence[0]
second_term = possible_sequence[1]

possible_ap_common_ratio = second_term - first_term
possible_gp_common_ratio = second_term // first_term

terms_sum = sum(possible_sequence)

ap_finite_sum = (first_term + possible_sequence[number_of_numbers - 1]) * number_of_numbers // 2
if terms_sum == ap_finite_sum:
    print('Vamos la pessoal! Falta pouco, nosso destino esta ao leste!')
    exit(0)

gp_finite_sum = first_term * (possible_gp_common_ratio ** number_of_numbers - 1) // (possible_gp_common_ratio - 1)
if terms_sum == gp_finite_sum:
    print('Vamos la pessoal! Falta pouco, nosso destino esta ao sul!')
else:
    print("Finalmente! O Two Piece sera meu e vou me tornar rei dos piratas!")
