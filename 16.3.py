clothes = ["socks", "shirt", "skirt", "scarf"]

def insert_element(new_cloth, index=0):
    clothes.insert(index, new_cloth)
#with 2 arguments, where the index is a positive value and new_cloth='hat'

insert_element("hat", 2)
print(clothes)

#with 2 arguments, where the index is a negative value and new_cloth has any value
insert_element("jeans", -2)
print(clothes)

#with 1 argument - new_cloth that has any value
insert_element("dress")
print(clothes)