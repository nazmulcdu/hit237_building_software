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
    image_url="images/Mango leafhopper img1.jpeg",
    full_description=(
        "Mango leafhoppers are serious pests found throughout mango-growing regions in:\n"
        "• India\n"
        "• South-East Asia\n"
        "• Papua New Guinea\n"
        "• Northern Australia (including Darwin, Palmerston, Pine Creek, and Katherine)\n\n"
        "These small, wedge-shaped insects damage mango trees by:\n"
        "• Feeding on sap\n"
        "• Laying eggs in flower stems and leaves\n\n"
        "Key impacts:\n"
        "• Most damaging during the flowering season\n"
        "• Potentially reduce yields by up to 50% if uncontrolled\n"
        "• Cause distorted leaves, flower abortion, fruit drop, and sooty mould formation due to honeydew excretion\n"
        "• Certain mango cultivars like Kensington Pride and Irwin may be more affected"
    ),
    symptoms="""\
<ul>
  <li>Curling and distortion of young leaves</li>
  <li>Sooty mould on older leaves due to honeydew</li>
  <li>Numerous punctures in flower stems leading to flower drop</li>
  <li>Sap-sucking damage on vegetative flush</li>
  <li>Presence of small, wedge-shaped adult insects or fast-moving nymphs on flush and flowers</li>
</ul>""",
    treatment="""\
<ul>
  <li>Apply two cover sprays of dimethoate or carbaryl seven days apart before flowering</li>
  <li>Target pests before flowering to reduce damage and protect pollinators</li>
  <li>Use the same timing and methods as redbanded thrips control</li>
  <li>Encourage natural predators such as native lacewing larvae</li>
  <li>Monitor mango trees regularly, especially during flowering and fruiting seasons</li>
</ul>"""
)




pest4 = MangoPestDisease(
    slug="mango-seed-weevil",
    name="Mango Seed-Weevil",
    short_desc="Internal pest that damages mango seeds and limits market access.",
    image_url="images/Mango seed weevil img3(inside seed).jpg",
    full_description=(
        "The mango seed weevil is a serious internal pest that affects the seed of mango fruit. Its presence:\n"
        "• Reduces market options\n"
        "• Disqualifies fruit from entry into key export destinations like Western Australia, China, Korea, the USA, and the UAE\n\n"
        "Weevils spread through:\n"
        "• Infested seed\n"
        "• Flight between trees\n"
        "• Unmanaged orchards\n"
        "• Discarded fruit piles\n\n"
        "Adult behavior and lifecycle:\n"
        "• Adults shelter under rough bark and become active at dawn and dusk\n"
        "• Feed on new flush growth\n"
        "• Eggs laid when fruit reach around 30mm in size\n"
        "• Larvae bore into the seed and develop entirely inside the fruit\n"
        "• Adults can emerge from fruit left on the ground after rain or irrigation"
    ),
    symptoms="""\
<ul>
  <li>Presence of egg-laying scars on fruit</li>
  <li>Feeding damage on new flushes</li>
  <li>Gum exudation or frass near holes in bark</li>
  <li>Larvae found inside cut fruit or seeds</li>
  <li>Adults found under bark during winter</li>
</ul>""",
    treatment="""\
<ul>
  <li>Remove all fruit from orchards, including fallen fruit</li>
  <li>Destroy or remove reject fruit and fruit dumps from the farm</li>
  <li>Mulch fallen fruit and prunings before weevils emerge</li>
  <li>Target adults using insecticides during emergence, flowering, flushing, and on tree trunks</li>
  <li>Use systemic insecticides to target larvae in fruit</li>
  <li>Monitor by inspecting for adults under bark and signs of damage on new growth</li>
</ul>"""
    )


pest5 = MangoPestDisease(
    slug="mango-scab",
    name="Mango Scab",
    short_desc="Fungal disease causing scabby lesions on mango fruit and leaves.",
    image_url="images/Mango scab img2.jpg",
    full_description=(
        "Mango scab is a fungal disease caused by *Elsinoë mangiferae*, which primarily affects young mango tissue. "
        "It thrives in humid and wet environments, making it a common issue in nurseries and regions with frequent rainfall.\n\n"
        "Key facts about mango scab:\n"
        "• Often mistaken for anthracnose in early stages\n"
        "• Causes scabby lesions that lead to severe fruit scarring\n"
        "• Most damaging to nursery plants and young fruit\n"
        "• Can distort leaves and reduce fruit marketability"
    ),
   symptoms="""\
<ul>
  <li>Small black lesions on young fruit</li>
  <li>Corky, scarred tissue with central scabs</li>
  <li>Brown haloed spots and leaf distortion</li>
  <li>Elongated lesions on midrib and stem</li>
</ul>
""",
treatment="""\
<ul>
  <li>Apply copper fungicide sprays from flowering to half fruit size</li>
  <li>Use weekly copper sprays in nurseries during wet weather</li>
  <li>Prune infected leaves, twigs, and dead plant matter</li>
  <li>Avoid mixing copper with zinc fertilizers due to phyto-toxicity risks</li>
</ul>
""",
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
