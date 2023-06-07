def join_me(name_list):
    if not name_list:
        return "Me"
    titles = map(lambda name: name.title(), name_list)
    if len(name_list) == 1:
        return f"{titles[0]} and me"
    else:
        
        output = ", ".join(titles) +", and me"
        return output
    
print(join_me(['steve', 'rick', 'al', 'betty']))

