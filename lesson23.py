nums = [10, 20, 30, 40]
nums.append(50)
nums.insert(1, 15)
print(nums)
fruits = ["ვაშლი", "მსხალი", "ბალი", "ატამი", "მსხალი"]
pos = fruits.index("მსხალი")
cnt = fruits.count("მსხალი")
print("პოზიცია:", pos)
print("ხელმეორედ რამდენჯერ:", cnt)
letters = ["კ", "ბ", "ა", "გ", "დ"]
letters.sort()
letters.remove("გ")
print(letters)
text = "python is fun"
upper_text = text.upper()
lower_text = upper_text.lower()
print(upper_text)
print(lower_text)
nums = [5, 10, 15, 20, 25]
removed = nums.pop()
print("წაიშალა:", removed)
nums.insert(2, 100)
print(nums)
