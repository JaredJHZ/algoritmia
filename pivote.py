# def comparacion(numero_uno, numero_dos):
#     return numero_uno == numero_dos
# def get_suma(slice_del_array,index, res):
#     if index >= len(slice_del_array):
#         return res
#     else:
#         return get_suma(slice_del_array, index+1 , res + slice_del_array[index])
# def conteo(index, array):
#     if index >= len(array):
#         print(-1)
#         return False
#     if comparacion(get_suma(array[0:index+1],0,0), get_suma(array[index:] ,0,0)):
#         print(index)
#         return True
#     else:
#         return conteo(index+1, array)
# def print_pivote(array):
#     conteo(0, array)
# print_pivote([1, 7, 3, 6, 5, 6])

class Solution:
    def comparacion(self,numero_uno, numero_dos):
        return numero_uno == numero_dos
    def get_suma(self,slice_del_array,index, res):
        if index >= len(slice_del_array):
            return res
        else:
            return self.get_suma(slice_del_array, index+1 , res + slice_del_array[index])
    def conteo(self,index, array):
        if index >= len(array):
            print(-1)
            return -1
        if self.comparacion(self.get_suma(array[0:index+1],0,0), self.get_suma(array[index:] ,0,0)):
            return index
        else:
            return self.conteo(index+1, array)
    def pivotIndex(self,array):
        return self.conteo(0, array)
solution = Solution()

print(solution.pivotIndex([1,7,3,6,5,6]))