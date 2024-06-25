import pandas
nat_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nat_dict = {row.letter:row.code for (index,row) in nat_df.iterrows()}

def get_nato(l):
    return nat_dict.get(l)

user_input = input("word to phonetic: ")
nato_list = [get_nato(l.upper()) for l  in user_input if l != " "]
print(nato_list)