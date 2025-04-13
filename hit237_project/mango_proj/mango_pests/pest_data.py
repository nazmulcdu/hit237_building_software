class MangoPestDisease:
    def __init__(self, slug, name, short_desc, image_url, full_description, symptoms, treatment):
        self.slug = slug
        self.name = name
        self.short_desc = short_desc
        self.image_url = image_url
        self.full_description = full_description
        self.symptoms = symptoms
        self.treatment = treatment

pest1 = MangoPestDisease(
    slug="anthracnose",
    name="Anthracnose",
    short_desc="Fungal disease causing black spots on fruit.",
    image_url="images/anthracnose.jpg",
    full_description="Anthracnose is a common fungal disease in mangoes caused by *Colletotrichum gloeosporioides*...",
    symptoms="Dark, sunken lesions on fruits, stems and flowers.",
    treatment="Use copper-based fungicides. Remove and destroy infected parts."
)

pest2 =MangoPestDisease(
    slug="powdery-mildew",
    name="Powdery Mildew",
    short_desc="White powder on leaves and flowers.",
    image_url="images/powdery_mildew.jpg",
    full_description="Caused by *Oidium mangiferae*, powdery mildew reduces fruit production.",
    symptoms="White powdery substance on leaves, flowers and young fruits.",
    treatment="Sulfur-based fungicides. Improve air circulation."
)

pest3 = MangoPestDisease(
    slug="fruit-fly",
    name="Fruit Fly",
    short_desc="Insect larvae that destroy mango pulp.",
    image_url="images/fruit_fly.jpg",
    full_description="Fruit flies lay eggs inside the fruit, and the larvae feed on the pulp, causing rot.",
    symptoms="Small holes in fruit, premature drop, rotting.",
    treatment="Use traps, sanitation, and cover sprays."
)

pest4 = MangoPestDisease(
    slug="stem-borer",
    name="Stem Borer",
    short_desc="Larvae bore into mango stems.",
    image_url="images/stem_borer.jpg",
    full_description="Stem borers feed inside mango trunks, weakening the plant.",
    symptoms="Gum oozing from bark, frass near holes.",
    treatment="Inject insecticides into holes and seal with mud."
)

pest5 =MangoPestDisease(
    slug="sooty-mould",
    name="Sooty Mould",
    short_desc="Black mold on leaves from pest secretions.",
    image_url="images/sooty_mould.jpg",
    full_description="Sooty mould grows on honeydew secreted by sucking insects like aphids.",
    symptoms="Black powdery growth on leaves and stems.",
    treatment="Control the pests causing honeydew. Wash leaves."
)

pest6 =MangoPestDisease(
    slug="dieback",
    name="Dieback",
    short_desc="Fungal infection causing branch death.",
    image_url="images/dieback.jpg",
    full_description="Dieback is caused by fungi like *Botryodiplodia theobromae*, leading to the drying of twigs and branches.",
    symptoms="Wilting and drying of branches, gum discharge.",
    treatment="Prune infected parts and apply fungicides."
)

pest7 = MangoPestDisease(
    slug="red-rust",
    name="Red Rust",
    short_desc="Algae infection turning leaves rusty red.",
    image_url="images/red_rust.jpg",
    full_description="Caused by *Cephaleuros virescens*, red rust leads to poor photosynthesis and yield.",
    symptoms="Rusty patches on upper leaf surface.",
    treatment="Copper fungicides. Remove infected leaves."
)

mango_pestdiseases = [pest1, pest2, pest3, pest4, pest5, pest6, pest7]
