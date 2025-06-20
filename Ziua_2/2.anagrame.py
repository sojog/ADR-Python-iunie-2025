# "sua" -> "sau"

def sunt_anagrame_v1(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False



def sunt_anagrame(s1, s2):
    return sorted(s1) == sorted(s2)


print("Sunt anagrame? - ", sunt_anagrame("sua", "sau"))


