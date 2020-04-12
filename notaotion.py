def user_input():
  user = input('Что-бы реализовать польскую нотацию введите знак операции и через пробел два числа \n(Пример: + 2 2) \n')
  return  user

def calc(self):
  function_length = len(self.split())
  sign = self.split()[0]


  if function_length != 3:
    print('Не верный ввод! Повторите!')
    print(len(self.split()))
    main()
 
  


  try:
    number_one = int (self.split ()[1])
    number_two = int (self.split ()[2])
    
    assert int(self.split ()[1]) >= 0 and int (self.split ()[2]) >= 0, 'Ошибка! Вводите только положительные числа!'

    assert sign in ['+', '-', '/', '*'], 'Не верный знак операции!'

    if sign == '+':
      return number_one + number_two
    elif sign == '-':
      return number_one - number_two
    elif sign == '/':
      return round((number_one / number_two), 2)
    elif sign == '*':
      return number_one * number_two
    elif function_length != 3: 
     return 'Можно вводить только два числа!' 
  except ZeroDivisionError:
    return 'Делить на ноль НЕЛЬЗЯ!'
  except ValueError:
    return  'Строка и число не совместимы!'
  except Exception as e:
    return f'Ошибка, повторите ввод! {e}'

  

def main():
  print(calc(user_input()))

if __name__ == '__main__':
  while True:
    main()