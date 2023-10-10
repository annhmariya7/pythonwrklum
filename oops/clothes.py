class Clothes:
    dress_list = [
    {   
        "id":1,
        "type": "Evening Gown",
        "brand": "DesignerX",
        "color": "Blue",
        "size": "Medium",
        "price": 250.00,
        "fabric": "Silk"
    },
    {   
        "id":2,
        "type": "Casual Dress",
        "brand": "FashionY",
        "color": "Red",
        "size": "Small",
        "price": 45.99,
        "fabric": "Cotton"
    },
    {   
        "id":3,
        "type": "Cocktail Dress",
        "brand": "GlamourZ",
        "color": "Black",
        "size": "Large",
        "price": 120.00,
        "fabric": "Velvet"
    },
    {   
        "id":4,
        "type": "Maxi Dress",
        "brand": "ChicStyle",
        "color": "Green",
        "size": "Medium",
        "price": 65.50,
        "fabric": "Chiffon"
    },
    {   
        "id":5,
        "type": "Summer Dress",
        "brand": "SunnyDays",
        "color": "Yellow",
        "size": "Medium",
        "price": 35.00,
        "fabric": "Linen"
    },
    {   
        "id":6,
        "type": "Wedding Dress",
        "brand": "EleganceBride",
        "color": "Ivory",
        "size": "Large",
        "price": 800.00,
        "fabric": "Lace"
    },
    {   
        "id":7,
        "type": "Party Dress",
        "brand": "PartyQueen",
        "color": "Silver",
        "size": "Small",
        "price": 55.99,
        "fabric": "Sequin"
    },
    {   
        "id":8,
        "type": "Boho Dress",
        "brand": "FreeSpirit",
        "color": "Multicolor",
        "size": "Medium",
        "price": 60.00,
        "fabric": "Rayon"
    },
    {   
        "id":9,
        "type": "Business Dress",
        "brand": "ProfessionalLook",
        "color": "Navy Blue",
        "size": "Medium",
        "price": 110.00,
        "fabric": "Wool"
    },
    {   
        "id":10,
        "type": "Midi Dress",
        "brand": "ModernChic",
        "color": "Pink",
        "size": "Small",
        "price": 48.50,
        "fabric": "Polyester"
    }
]
    
    #return all clothes records  (list)
    def get(self,*args,**kwargs):       
        return self.data
    

    #cloths detail              (detail)
    def retrieve(self,*args,**kwargs):
        id=kwargs.get("id")
        record=[c for clo in self.data if clo.get("id")==id]     #[list comprehension]
        return record
    
    #add clothes                 (create)
    def create(self,*args,**kwargs):         #self must used inside the class
        self.data.append(kwargs)             #kwargs used to display in dictonary format


    
    #delete
    def destroy(self,*args,**kwargs):
        id=kwargs.get("id")
        obj=[e for e in self.data if e.get("id")==id].pop()
        self.data.remove(obj)

   
obj=Clothes()
print(obj.get())

print(obj.retrieve(id=4))

obj.create(id=7,name="ann",dept="hr",salary=24000)
print(obj.get())        

obj.destroy(id=4)
print(obj.get())    