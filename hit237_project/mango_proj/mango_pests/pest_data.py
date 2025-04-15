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
    slug="backterial-spots",
    name="Backterial-spots",
    short_desc="White powder on leaves and flowers.",
    image_url="images/powdery_mildew.jpg",
    full_description="Caused by *Oidium mangiferae*, powdery mildew reduces fruit production.",
    symptoms="White powdery substance on leaves, flowers and young fruits.",
    treatment="Sulfur-based fungicides. Improve air circulation."
)

pest3 = MangoPestDisease(
    slug="mango-leafhoppers",
    name="Mango Leafhoppers",
    short_desc="Sap-sucking insects that damage mango flowers and reduce yield.",
    image_url="images/leafhopper.jpg",  # Consider updating to an actual mango leafhopper image
    full_description=(
        "Mango leafhoppers are serious pests found throughout mango-growing regions in India, South-East Asia, "
        "Papua New Guinea, and northern Australia including Darwin, Palmerston, Pine Creek, and Katherine. "
        "These small, wedge-shaped insects damage mango trees by feeding on sap and laying eggs in flower stems and leaves. "
        "They are most damaging during the flowering season, potentially reducing yields by up to 50% if uncontrolled. "
        "Their feeding and egg-laying activity leads to distorted leaves, flower abortion, fruit drop, and sooty mould formation "
        "due to honeydew excretion. Certain mango cultivars like Kensington Pride and Irwin may be more affected."
    ),
    symptoms=(
        "• Curling and distortion of young leaves\n"
        "• Sooty mould on older leaves due to honeydew\n"
        "• Numerous punctures in flower stems leading to flower drop\n"
        "• Sap-sucking damage on vegetative flush\n"
        "• Presence of small, wedge-shaped adult insects or fast-moving nymphs on flush and flowers"
    ),
    treatment=(
        "• Apply two cover sprays of dimethoate or carbaryl seven days apart before flowering\n"
        "• Target pests before flowering to reduce damage and protect pollinators\n"
        "• Use the same timing and methods as redbanded thrips control\n"
        "• Encourage natural predators such as native lacewing larvae\n"
        "• Monitor mango trees regularly, especially during flowering and fruiting seasons"
    )
)


pest4 = MangoPestDisease(
    slug="mango-seed-weevil",
    name="Mango Seed-Weevil",
    short_desc="Internal pest that damages mango seeds and limits market access.",
    image_url="images/stem_borer.jpg",  # You may want to replace this with an actual seed-weevil image
    full_description=(
        "The mango seed weevil is a serious internal pest that affects the seed of mango fruit. "
        "Its presence reduces market options and disqualifies fruit from entry into key export destinations "
        "like Western Australia, China, Korea, the USA, and the UAE. Weevils spread through infested seed, "
        "flight between trees, unmanaged orchards, and discarded fruit piles. Adults shelter under rough bark "
        "and become active at dawn and dusk, feeding on new flush growth. Eggs are laid when fruit reach around 30mm "
        "in size, and hatching larvae bore into the seed. Development occurs entirely inside the fruit, and adult weevils "
        "can emerge from fruit left on the ground after rain or irrigation."
    ),
    symptoms=(
        "• Presence of egg-laying scars on fruit\n"
        "• Feeding damage on new flushes\n"
        "• Gum exudation or frass near holes in bark\n"
        "• Larvae found inside cut fruit or seeds\n"
        "• Adults found under bark during winter"
    ),
    treatment=(
        "• Remove all fruit from orchards, including fallen fruit\n"
        "• Destroy or remove reject fruit and fruit dumps from the farm\n"
        "• Mulch fallen fruit and prunings before weevils emerge\n"
        "• Target adults using insecticides during emergence, flowering, flushing, and on tree trunks\n"
        "• Use systemic insecticides to target larvae in fruit\n"
        "• Monitor by inspecting for adults under bark and signs of damage on new growth"
    )
)

pest5 = MangoPestDisease(
    slug="mango-scab",
    name="Mango Scab",
    short_desc="Fungal disease causing scabby lesions on mango fruit and leaves.",
    image_url="images/mango_scab.jpg",
    full_description="Mango scab is caused by the fungus *Elsinoë mangiferae*. It affects young mango tissue, particularly in humid and wet environments. Initially mistaken for anthracnose, it causes scabby lesions and can severely scar fruit, especially in nursery plants.",
    symptoms=(
        " Small black lesions on young fruit\n"
        " Corky, scarred tissue with central scabs\n"
        " Brown haloed spots and leaf distortion\n"
        " Elongated lesions on midrib and stem"
    ),
    treatment=(
        " Apply copper fungicide sprays from flowering to half fruit size.\n"
        " Weekly copper sprays in nurseries during wet weather.\n"
        " Prune infected leaves, twigs, and dead plant matter.\n"
        " Avoid mixing copper with zinc fertilizers due to phyto-toxicity risks."
    )
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
