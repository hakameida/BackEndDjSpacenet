from django.db import models
import uuid

AGE_CHOICES = [
    ('جديد', 'جديد'),
    ('مستعمل', 'مستعمل'),
    ('اوبن بوكس', 'اوبن بوكس'),
]

# ============ Computer Type (like ProductType but for computers only) ============
class ComputerType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

# ============ Accessory Type (like ProductType but for accessories only) ============
class AccessoryType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

# ============ Laptop Model (NO type, has fixed hardware fields) ============
class Laptop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    discount = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.CharField(max_length=20, choices=AGE_CHOICES)
    status = models.BooleanField(default=True)
    count = models.IntegerField(default=0)
    
    # Fixed hardware fields for Laptop
    cpu = models.CharField(max_length=255, blank=True)
    gpu = models.CharField(max_length=255, blank=True)
    ram = models.CharField(max_length=100, blank=True)
    hard = models.CharField(max_length=255, blank=True)
    screen = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=50, blank=True)
    os = models.CharField(max_length=100, blank=True)
    
    # URL fields for external images
    url1 = models.URLField(blank=True)
    url2 = models.URLField(blank=True)
    url3 = models.URLField(blank=True)
    url4 = models.URLField(blank=True)
    url5 = models.URLField(blank=True)
    
    # Local image upload fields
    image1 = models.ImageField(upload_to="laptops/", blank=True, null=True)
    image2 = models.ImageField(upload_to="laptops/", blank=True, null=True)
    image3 = models.ImageField(upload_to="laptops/", blank=True, null=True)
    image4 = models.ImageField(upload_to="laptops/", blank=True, null=True)
    image5 = models.ImageField(upload_to="laptops/", blank=True, null=True)
    
    def __str__(self):
        return f"Laptop - {self.name}"

# ============ Computer Model (HAS ComputerType, NO fixed hardware fields) ============
class Computer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    discount = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.ForeignKey(ComputerType, on_delete=models.CASCADE, related_name='computers', null=True, blank=True)
    age = models.CharField(max_length=20, choices=AGE_CHOICES)
    status = models.BooleanField(default=True)
    count = models.IntegerField(default=0)
    
    # URL fields for external images
    url1 = models.URLField(blank=True)
    url2 = models.URLField(blank=True)
    url3 = models.URLField(blank=True)
    url4 = models.URLField(blank=True)
    url5 = models.URLField(blank=True)
    
    # Local image upload fields
    image1 = models.ImageField(upload_to="computers/", blank=True, null=True)
    image2 = models.ImageField(upload_to="computers/", blank=True, null=True)
    image3 = models.ImageField(upload_to="computers/", blank=True, null=True)
    image4 = models.ImageField(upload_to="computers/", blank=True, null=True)
    image5 = models.ImageField(upload_to="computers/", blank=True, null=True)
    
    def __str__(self):
        return f"Computer - {self.name}"

# ============ Accessory Model (HAS AccessoryType, has fixed basic fields) ============
class Accessory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    discount = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.ForeignKey(AccessoryType, on_delete=models.CASCADE, related_name='accessories', null=True, blank=True)
    age = models.CharField(max_length=20, choices=AGE_CHOICES)
    status = models.BooleanField(default=True)
    count = models.IntegerField(default=0)
    
    # Fixed basic fields for Accessory
    brand = models.CharField(max_length=100, blank=True)
    model_number = models.CharField(max_length=100, blank=True)
    compatibility = models.CharField(max_length=255, blank=True)
    
    # URL fields for external images
    url1 = models.URLField(blank=True)
    url2 = models.URLField(blank=True)
    url3 = models.URLField(blank=True)
    url4 = models.URLField(blank=True)
    url5 = models.URLField(blank=True)
    
    # Local image upload fields
    image1 = models.ImageField(upload_to="accessories/", blank=True, null=True)
    image2 = models.ImageField(upload_to="accessories/", blank=True, null=True)
    image3 = models.ImageField(upload_to="accessories/", blank=True, null=True)
    image4 = models.ImageField(upload_to="accessories/", blank=True, null=True)
    image5 = models.ImageField(upload_to="accessories/", blank=True, null=True)
    
    def __str__(self):
        return f"Accessory - {self.name}"

# ============ Dynamic Spec Models (Key-Value pairs) ============

# For Laptop - extra dynamic fields beyond the fixed ones
class LaptopDynamicSpec(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name='dynamic_specs')
    key = models.CharField(max_length=255)
    value = models.TextField(blank=True)
    
    class Meta:
        unique_together = ('laptop', 'key')
    
    def __str__(self):
        return f"{self.key}: {self.value}"

# For Computer - ALL specs are dynamic (no fixed hardware fields)
class ComputerDynamicSpec(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, related_name='dynamic_specs')
    key = models.CharField(max_length=255)
    value = models.TextField(blank=True)
    
    class Meta:
        unique_together = ('computer', 'key')
    
    def __str__(self):
        return f"{self.key}: {self.value}"

# For Accessory - extra dynamic fields beyond the fixed ones
class AccessoryDynamicSpec(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    accessory = models.ForeignKey(Accessory, on_delete=models.CASCADE, related_name='dynamic_specs')
    key = models.CharField(max_length=255)
    value = models.TextField(blank=True)
    
    class Meta:
        unique_together = ('accessory', 'key')
    
    def __str__(self):
        return f"{self.key}: {self.value}"

# ============ Offer Model ============
class Offer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    
    product_module = models.CharField(
        max_length=20,
        choices=[
            ('laptop', 'Laptop'),
            ('computer', 'Computer'),
            ('accessory', 'Accessory'),
        ],
        default='computer'
    )
    product_id = models.UUIDField(null=True, blank=True)
    def __str__(self):
        return f"{self.product_module} - {self.product_id} - ${self.price}"  # Fixed this line

# ============ Dollar Price Model ============
class DollarPrice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dollar_price = models.FloatField()
    
    def __str__(self):
        return f"${self.dollar_price}"

# ============ YouTube Links Model ============
class YouTubeLinks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    youtubeUrl = models.URLField(blank=True)
    
    def __str__(self):
        return self.youtubeUrl