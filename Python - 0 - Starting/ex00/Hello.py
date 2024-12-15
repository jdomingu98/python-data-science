ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# List: change index
ft_list[1] = "World!"

# Tuple: Inmutable. Create a new one and assign it to the variable
ft_tuple = ("Hello", "Spain!")

# Set: discard unnecessary element and add a new one
ft_set.discard("tutu!")
ft_set.add("Málaga!")

# Dict: change value of key
ft_dict["Hello"] = "42 Málaga!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
