insta={"vidhi","mansi","aditya","dhrumil","lalit"}
facebook={"dhruvit","megha","vidhi","aditya","dhrumil"}
snapchat={"vidhi","mansi","megha","lalit","aditya","pankti"}


# all=insta.intersection(facebook,snapchat)
# print("All app user:",all)

# insta_face=insta.intersection(facebook)
# print("Insta-Facebook user:",insta_face)

# face_snap=facebook.intersection(snapchat)
# print("Facebook-Snapchat user:",face_snap)

# snapchat=snapchat.difference(insta,facebook)
# print("Only Snapchat User:",snapchat)

insta_face=insta.intersection(facebook)
# print(insta_face)
all=insta_face.intersection(snapchat)
print("All app user:",all)

instaface=insta.intersection(facebook)
# print(instaface)
diffs=instaface.difference(snapchat)
print("Insta-Facebook User:",diffs)

facesnap=facebook.intersection(snapchat)
# print(facesnap)
diffi=facesnap.difference(insta)
print("Facebook-Snapchat User:",diffi)

faceinsta=insta.union(facebook)
# print(faceinsta)
diff=snapchat.difference(faceinsta)
print("Only snap user:",diff)