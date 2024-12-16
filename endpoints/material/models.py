from django.db import models
from django.core.validators import MinValueValidator

class Material(models.Model):
    class Category(models.TextChoices):
        METAL = "Metal", "Metal"
        WOOD = "Wood", "Wood"
        CONCRETE = "Concrete", "Concrete"
        PLASTIC = "Plastic", "Plastic"
        GLASS = "Glass", "Glass"

    class SubCategory(models.TextChoices):
        SHEET_METAL = "Sheet Metal", "Sheet Metal"
        CAST_IRON = "Cast Iron", "Cast Iron"
        HARDWOOD = "Hardwood", "Hardwood"
        PLYWOOD = "Plywood", "Plywood"
        REINFORCED_CONCRETE = "Reinforced Concrete", "Reinforced Concrete"
        THERMOPLASTIC = "Thermoplastic", "Thermoplastic"
        TEMPERED_GLASS = "Tempered Glass", "Tempered Glass"
        STEEL = "Steel", "Steel"
        ALUMINUM = "Aluminum", "Aluminum"
        SOFTWOOD = "Softwood", "Softwood"
        LAMINATED_GLASS = "Laminated Glass", "Laminated Glass"
        FROSTED_GLASS = "Frosted Glass", "Frosted Glass"

    category = models.CharField(
        max_length=50,
        choices=Category.choices,
        default=Category.METAL,
    )
    sub_category = models.CharField(
        max_length=50,
        choices=SubCategory.choices,
        default=SubCategory.SHEET_METAL,
    )
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return self.name
