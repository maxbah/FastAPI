from tasks import add, print_hello, create_new_file

name = "Maks"
filename = "HelloFile"
text = "New HelloFile.txt created"

add.delay(4, 4)
print("Start add function..")

#print_hello.apply_async(args=[name], ignore_result=True)
print_hello.delay("Maks")
print("Start printing hello name in background....")

#create_new_file.apply_async(args=[filename, text], ignore_result=True)
create_new_file("HelloFile","Privet epta")
print("Start creation HelloFile.txt in background....")
