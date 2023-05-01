participants = ['(Moderator)']
participant = input('Введите  название   игры (0 - остановить ввод):')
while participant != '0':
  if participant in participants:
      print('такая игра уже есть!!!')
  else:
      participants.append(participant)
  participant = input('Введите  название игры (0 - остановить ввод):')
participants.sort()
print('спсок игр набран:', participants)