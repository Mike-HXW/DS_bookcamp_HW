def count_vowels(word):
    count_final = 0
    list_vowel = ["a","e","i","o","u"]
    for i in range (len(word)):
        for j in list_vowel:
            if word[i] == j:
                count_final += 1
                break
    return count_final
  
