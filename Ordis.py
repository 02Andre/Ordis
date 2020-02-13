import chbot # The chatbot
import files # File manager

#gives user the option to use a different memory.txt file
print('before you can start talking please type what memory you want the bot to have.')
print('options: default or Ordis')
memory_type = input('type:')
#the user will be in a while loop until they type the correct memory option
while memory_type != 'default' and memory_type != 'Ordis':
    print('no such memory exsits please choose from the options or check if its spelled right.')
    memory_type = input('type: ')
#if user want the default memory this will activate
if memory_type == ('default'):
    chbot.chatbot('memory.txt')
#this is the other memory option
elif memory_type == ('Ordis'):
    chbot.chatbot('Ordis.txt')
