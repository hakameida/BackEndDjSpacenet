# schema.py - Complete file

import graphene
from graphene_django.types import DjangoObjectType
from .models import (
    Laptop, LaptopDynamicSpec,
    Computer, ComputerType, ComputerDynamicSpec,
    Accessory, AccessoryType, AccessoryDynamicSpec,
    DollarPrice, Offer, YouTubeLinks
)

# ============ YouTube Type ============
class YouTubeType(DjangoObjectType):
    class Meta:
        model = YouTubeLinks
        fields = ("id", "youtubeUrl")

# ============ Dollar Price Type ============
class DollarPriceType(DjangoObjectType):
    class Meta:
        model = DollarPrice
        fields = ("id", "dollar_price")

# ============ Dynamic Spec Types ============
class LaptopDynamicSpecType(DjangoObjectType):
    class Meta:
        model = LaptopDynamicSpec
        fields = ("id", "key", "value")

class ComputerDynamicSpecType(DjangoObjectType):
    class Meta:
        model = ComputerDynamicSpec
        fields = ("id", "key", "value")

class AccessoryDynamicSpecType(DjangoObjectType):
    class Meta:
        model = AccessoryDynamicSpec
        fields = ("id", "key", "value")

# ============ Computer Type Type (for Computer types) ============
class ComputerTypeType(DjangoObjectType):
    class Meta:
        model = ComputerType
        fields = ("id", "name")

# ============ Accessory Type Type (for Accessory types) ============
class AccessoryTypeType(DjangoObjectType):
    class Meta:
        model = AccessoryType
        fields = ("id", "name")

# ============ Laptop Type ============
class LaptopType(DjangoObjectType):
    class Meta:
        model = Laptop
        fields = "__all__"
    
    dynamic_specs = graphene.List(LaptopDynamicSpecType)
    
    def resolve_dynamic_specs(self, info):
        return self.dynamic_specs.all()

# ============ Computer Type ============
class ComputerType(DjangoObjectType):
    class Meta:
        model = Computer
        fields = "__all__"
    
    dynamic_specs = graphene.List(ComputerDynamicSpecType)
    type_info = graphene.Field(ComputerTypeType)
    
    def resolve_dynamic_specs(self, info):
        return self.dynamic_specs.all()
    
    def resolve_type_info(self, info):
        return self.type

# ============ Accessory Type ============
class AccessoryType(DjangoObjectType):
    class Meta:
        model = Accessory
        fields = "__all__"
    
    dynamic_specs = graphene.List(AccessoryDynamicSpecType)
    type_info = graphene.Field(AccessoryTypeType)
    
    def resolve_dynamic_specs(self, info):
        return self.dynamic_specs.all()
    
    def resolve_type_info(self, info):
        return self.type

# ============ Offer Type (UPDATED) ============
class OfferType(DjangoObjectType):
    class Meta:
        model = Offer
        fields = ("id", "product_id", "price", "status", "product_module")
    
    # Rename to camelCase for GraphQL convention
    productId = graphene.String()
    productModule = graphene.String()
    
    def resolve_productId(self, info):
        return str(self.product_id) if self.product_id else None
    
    def resolve_productModule(self, info):
        return self.product_module.upper() if self.product_module else None
    
    def resolve_price(self, info):
        return str(self.price)

# ============ Input Types ============
class DynamicSpecInput(graphene.InputObjectType):
    key = graphene.String(required=True)
    value = graphene.String()

class LaptopInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    description = graphene.String()
    discount = graphene.String()
    price = graphene.String(required=True)
    age = graphene.String()
    status = graphene.Boolean()
    count = graphene.Int()
    cpu = graphene.String()
    gpu = graphene.String()
    ram = graphene.String()
    hard = graphene.String()
    screen = graphene.String()
    color = graphene.String()
    os = graphene.String()
    dynamic_specs = graphene.List(DynamicSpecInput)
    url1 = graphene.String()
    url2 = graphene.String()
    url3 = graphene.String()
    url4 = graphene.String()
    url5 = graphene.String()

class ComputerInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    description = graphene.String()
    discount = graphene.String()
    price = graphene.String(required=True)
    type_id = graphene.ID()
    age = graphene.String()
    status = graphene.Boolean()
    count = graphene.Int()
    dynamic_specs = graphene.List(DynamicSpecInput)
    url1 = graphene.String()
    url2 = graphene.String()
    url3 = graphene.String()
    url4 = graphene.String()
    url5 = graphene.String()

class AccessoryInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    description = graphene.String()
    discount = graphene.String()
    price = graphene.String(required=True)
    type_id = graphene.ID()
    age = graphene.String()
    status = graphene.Boolean()
    count = graphene.Int()
    brand = graphene.String()
    model_number = graphene.String()
    compatibility = graphene.String()
    dynamic_specs = graphene.List(DynamicSpecInput)
    url1 = graphene.String()
    url2 = graphene.String()
    url3 = graphene.String()
    url4 = graphene.String()
    url5 = graphene.String()

class ComputerTypeInput(graphene.InputObjectType):
    name = graphene.String(required=True)

class AccessoryTypeInput(graphene.InputObjectType):
    name = graphene.String(required=True)

# ============ Mutations ============

# Computer Type Mutations
class CreateComputerType(graphene.Mutation):
    class Arguments:
        input = ComputerTypeInput(required=True)
    
    computer_type = graphene.Field(ComputerTypeType)
    
    def mutate(self, info, input):
        computer_type = ComputerType(name=input.name)
        computer_type.save()
        return CreateComputerType(computer_type=computer_type)

class DeleteComputerType(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    success = graphene.Boolean()
    
    def mutate(self, info, id):
        try:
            ComputerType.objects.get(pk=id).delete()
            return DeleteComputerType(success=True)
        except:
            return DeleteComputerType(success=False)

# Accessory Type Mutations
class CreateAccessoryType(graphene.Mutation):
    class Arguments:
        input = AccessoryTypeInput(required=True)
    
    accessory_type = graphene.Field(AccessoryTypeType)
    
    def mutate(self, info, input):
        accessory_type = AccessoryType(name=input.name)
        accessory_type.save()
        return CreateAccessoryType(accessory_type=accessory_type)

class DeleteAccessoryType(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    success = graphene.Boolean()
    
    def mutate(self, info, id):
        try:
            AccessoryType.objects.get(pk=id).delete()
            return DeleteAccessoryType(success=True)
        except:
            return DeleteAccessoryType(success=False)

# Laptop Mutations
class CreateLaptop(graphene.Mutation):
    class Arguments:
        input = LaptopInput(required=True)
    
    laptop = graphene.Field(LaptopType)
    
    def mutate(self, info, input):
        laptop = Laptop(
            name=input.name,
            description=input.get('description', ''),
            discount=input.get('discount', ''),
            price=input.price,
            age=input.get('age', 'جديد'),
            status=input.get('status', True),
            count=input.get('count', 0),
            cpu=input.get('cpu', ''),
            gpu=input.get('gpu', ''),
            ram=input.get('ram', ''),
            hard=input.get('hard', ''),
            screen=input.get('screen', ''),
            color=input.get('color', ''),
            os=input.get('os', ''),
            url1=input.get('url1', ''),
            url2=input.get('url2', ''),
            url3=input.get('url3', ''),
            url4=input.get('url4', ''),
            url5=input.get('url5', ''),
        )
        laptop.save()
        
        if input.get('dynamic_specs'):
            for spec in input.dynamic_specs:
                LaptopDynamicSpec.objects.create(
                    laptop=laptop,
                    key=spec.key,
                    value=spec.value
                )
        
        return CreateLaptop(laptop=laptop)

class UpdateLaptop(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = LaptopInput(required=True)
    
    laptop = graphene.Field(LaptopType)
    
    def mutate(self, info, id, input):
        laptop = Laptop.objects.get(pk=id)
        
        for key, value in input.items():
            if key not in ['dynamic_specs'] and value is not None:
                setattr(laptop, key, value)
        laptop.save()
        
        if input.get('dynamic_specs'):
            laptop.dynamic_specs.all().delete()
            for spec in input.dynamic_specs:
                LaptopDynamicSpec.objects.create(
                    laptop=laptop,
                    key=spec.key,
                    value=spec.value
                )
        
        return UpdateLaptop(laptop=laptop)

class DeleteLaptop(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    success = graphene.Boolean()
    
    def mutate(self, info, id):
        try:
            Laptop.objects.get(pk=id).delete()
            return DeleteLaptop(success=True)
        except:
            return DeleteLaptop(success=False)

# Computer Mutations
class CreateComputer(graphene.Mutation):
    class Arguments:
        input = ComputerInput(required=True)
    
    computer = graphene.Field(ComputerType)
    
    def mutate(self, info, input):
        computer = Computer(
            name=input.name,
            description=input.get('description', ''),
            discount=input.get('discount', ''),
            price=input.price,
            type_id=input.get('type_id'),
            age=input.get('age', 'جديد'),
            status=input.get('status', True),
            count=input.get('count', 0),
            url1=input.get('url1', ''),
            url2=input.get('url2', ''),
            url3=input.get('url3', ''),
            url4=input.get('url4', ''),
            url5=input.get('url5', ''),
        )
        computer.save()
        
        if input.get('dynamic_specs'):
            for spec in input.dynamic_specs:
                ComputerDynamicSpec.objects.create(
                    computer=computer,
                    key=spec.key,
                    value=spec.value
                )
        
        return CreateComputer(computer=computer)

class UpdateComputer(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = ComputerInput(required=True)
    
    computer = graphene.Field(ComputerType)
    
    def mutate(self, info, id, input):
        computer = Computer.objects.get(pk=id)
        
        for key, value in input.items():
            if key not in ['dynamic_specs'] and value is not None:
                setattr(computer, key, value)
        computer.save()
        
        if input.get('dynamic_specs'):
            computer.dynamic_specs.all().delete()
            for spec in input.dynamic_specs:
                ComputerDynamicSpec.objects.create(
                    computer=computer,
                    key=spec.key,
                    value=spec.value
                )
        
        return UpdateComputer(computer=computer)

class DeleteComputer(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    success = graphene.Boolean()
    
    def mutate(self, info, id):
        try:
            Computer.objects.get(pk=id).delete()
            return DeleteComputer(success=True)
        except:
            return DeleteComputer(success=False)

# Accessory Mutations
class CreateAccessory(graphene.Mutation):
    class Arguments:
        input = AccessoryInput(required=True)
    
    accessory = graphene.Field(AccessoryType)
    
    def mutate(self, info, input):
        accessory = Accessory(
            name=input.name,
            description=input.get('description', ''),
            discount=input.get('discount', ''),
            price=input.price,
            type_id=input.get('type_id'),
            age=input.get('age', 'جديد'),
            status=input.get('status', True),
            count=input.get('count', 0),
            brand=input.get('brand', ''),
            model_number=input.get('model_number', ''),
            compatibility=input.get('compatibility', ''),
            url1=input.get('url1', ''),
            url2=input.get('url2', ''),
            url3=input.get('url3', ''),
            url4=input.get('url4', ''),
            url5=input.get('url5', ''),
        )
        accessory.save()
        
        if input.get('dynamic_specs'):
            for spec in input.dynamic_specs:
                AccessoryDynamicSpec.objects.create(
                    accessory=accessory,
                    key=spec.key,
                    value=spec.value
                )
        
        return CreateAccessory(accessory=accessory)

class UpdateAccessory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = AccessoryInput(required=True)
    
    accessory = graphene.Field(AccessoryType)
    
    def mutate(self, info, id, input):
        accessory = Accessory.objects.get(pk=id)
        
        for key, value in input.items():
            if key not in ['dynamic_specs'] and value is not None:
                setattr(accessory, key, value)
        accessory.save()
        
        if input.get('dynamic_specs'):
            accessory.dynamic_specs.all().delete()
            for spec in input.dynamic_specs:
                AccessoryDynamicSpec.objects.create(
                    accessory=accessory,
                    key=spec.key,
                    value=spec.value
                )
        
        return UpdateAccessory(accessory=accessory)

class DeleteAccessory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    success = graphene.Boolean()
    
    def mutate(self, info, id):
        try:
            Accessory.objects.get(pk=id).delete()
            return DeleteAccessory(success=True)
        except:
            return DeleteAccessory(success=False)

# ============ Query ============
class Query(graphene.ObjectType):
    # Laptop queries
    all_laptops = graphene.List(LaptopType, status=graphene.Boolean())
    laptop_by_id = graphene.Field(LaptopType, id=graphene.ID())
    search_laptops = graphene.List(LaptopType, word=graphene.String())
    
    # Computer queries
    all_computers = graphene.List(ComputerType, type_name=graphene.String(), status=graphene.Boolean())
    computer_by_id = graphene.Field(ComputerType, id=graphene.ID())
    search_computers = graphene.List(ComputerType, word=graphene.String())
    computer_types = graphene.List(ComputerTypeType)
    
    # Accessory queries
    all_accessories = graphene.List(AccessoryType, type_name=graphene.String(), status=graphene.Boolean())
    accessory_by_id = graphene.Field(AccessoryType, id=graphene.ID())
    search_accessories = graphene.List(AccessoryType, word=graphene.String())
    accessory_types = graphene.List(AccessoryTypeType)
    
    # Other queries
    all_offers = graphene.List(OfferType, status=graphene.Boolean())
    offer_by_id = graphene.Field(OfferType, id=graphene.ID())
    dollar_price_by_pk = graphene.Field(DollarPriceType, id=graphene.UUID(required=True))
    youtube_links = graphene.List(YouTubeType)
    
    # Laptop resolvers
    def resolve_all_laptops(self, info, status=None):
        qs = Laptop.objects.all()
        if status is not None:
            qs = qs.filter(status=status)
        return qs
    
    def resolve_laptop_by_id(self, info, id):
        try:
            return Laptop.objects.get(pk=id)
        except Laptop.DoesNotExist:
            return None
    
    def resolve_search_laptops(self, info, word=None):
        if word:
            return Laptop.objects.filter(name__icontains=word)
        return Laptop.objects.none()
    
    # Computer resolvers
    def resolve_all_computers(self, info, type_name=None, status=None):
        qs = Computer.objects.all()
        if type_name:
            qs = qs.filter(type__name=type_name)
        if status is not None:
            qs = qs.filter(status=status)
        return qs
    
    def resolve_computer_by_id(self, info, id):
        try:
            return Computer.objects.get(pk=id)
        except Computer.DoesNotExist:
            return None
    
    def resolve_search_computers(self, info, word=None):
        if word:
            return Computer.objects.filter(name__icontains=word)
        return Computer.objects.none()
    
    def resolve_computer_types(self, info):
        return ComputerType.objects.all()
    
    # Accessory resolvers
    def resolve_all_accessories(self, info, type_name=None, status=None):
        qs = Accessory.objects.all()
        if type_name:
            qs = qs.filter(type__name=type_name)
        if status is not None:
            qs = qs.filter(status=status)
        return qs
    
    def resolve_accessory_by_id(self, info, id):
        try:
            return Accessory.objects.get(pk=id)
        except Accessory.DoesNotExist:
            return None
    
    def resolve_search_accessories(self, info, word=None):
        if word:
            return Accessory.objects.filter(name__icontains=word)
        return Accessory.objects.none()
    
    def resolve_accessory_types(self, info):
        return AccessoryType.objects.all()
    
    # Other resolvers
    def resolve_all_offers(self, info, status=None):
        qs = Offer.objects.all()
        if status is not None:
            qs = qs.filter(status=status)
        return qs
    
    def resolve_offer_by_id(self, info, id):
        try:
            return Offer.objects.get(pk=id)
        except Offer.DoesNotExist:
            return None
    
    def resolve_dollar_price_by_pk(self, info, id):
        try:
            return DollarPrice.objects.get(pk=id)
        except DollarPrice.DoesNotExist:
            return None
    
    def resolve_youtube_links(self, info):
        return YouTubeLinks.objects.all()

# ============ Mutation ============
class Mutation(graphene.ObjectType):
    # Computer type mutations
    create_computer_type = CreateComputerType.Field()
    delete_computer_type = DeleteComputerType.Field()
    
    # Accessory type mutations
    create_accessory_type = CreateAccessoryType.Field()
    delete_accessory_type = DeleteAccessoryType.Field()
    
    # Laptop mutations
    create_laptop = CreateLaptop.Field()
    update_laptop = UpdateLaptop.Field()
    delete_laptop = DeleteLaptop.Field()
    
    # Computer mutations
    create_computer = CreateComputer.Field()
    update_computer = UpdateComputer.Field()
    delete_computer = DeleteComputer.Field()
    
    # Accessory mutations
    create_accessory = CreateAccessory.Field()
    update_accessory = UpdateAccessory.Field()
    delete_accessory = DeleteAccessory.Field()

# ============ Schema ============
schema = graphene.Schema(query=Query, mutation=Mutation)