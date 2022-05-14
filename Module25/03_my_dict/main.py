class Dict(dict):

    def get(self, key):
        if key in self:
            return self[key]
        return 0


my_dict = Dict()
my_dict['Один'] = 1
my_dict['Два'] = 2
my_dict['Три'] = 3
print(my_dict.get('Один'))
