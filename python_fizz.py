class Solution:
    def fizzBuzz(self, n):
        for i in range(1, n + 1):
            texto_a_imprimir = ""
            no_es_multiplo = True
            
            if self.is_multiple_of_three(i):
                texto_a_imprimir += "Fizz"
                no_es_multiplo = False

            if self.is_multiple_of_five(i):
                texto_a_imprimir += "Buzz"
                no_es_multiplo = False

            if no_es_multiplo:
                texto_a_imprimir = str(i)

            print(texto_a_imprimir)
        
        
    def is_multiple_of_three(self, n):
        if (n % 3 == 0):
            return True
        else:
            return False
        
    def is_multiple_of_five(self, n):
        if(n % 5 == 0):
            return True
        else:
            return False

solution = Solution();

solution.fizzBuzz(10000)