# The following list is given:



# filenames = ['view.jpg', 'bear.jpg', 'ball.png']


# Add the file 'phone.jpg' to this list at the beginning. Then delete the file 'ball.png'. In response, print the filenames list to the console.


filenames = ['view.jpg', 'bear.jpg', 'ball.png']

filenames = ['phone.jpg']+filenames

list = []

for file in filenames:
    if file != 'ball.png':
        list.append(file)
print(list)