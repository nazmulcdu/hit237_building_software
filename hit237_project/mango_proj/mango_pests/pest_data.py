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
    slug="fruit-flies",
    name="Fruit Flies",
    short_desc="Fruit-flies lay eggs on mangoes, causing damage to the fruit and crop.",
    image_url="images/fruitflies.png",
    full_description=
    "Fruit flies are labelled as one of the major pests in the Northern Territory due to their negative effects on a variety of fruit crops, particularly mangoes. The two main species of fruit flies include Bactocera tyroni and Bactocera jarvisi and they both have negative effects on the harvest of mangoes (E. S. C. Smith and H. Brown, 2014).",
    symptoms="•Decay of fruit flesh •Bruising on fruit skin, and sting marks",
    treatment="•Bait spraying to divert the flies to feed on the bait • Cover mangoes with bags so they are not reachable • Fruit dipping would kill any eggs on the fruits • Remove any ripe/overripe mangose or just before they ripe so that the flies do not get a chance to lay eggs."
)

pest7 = MangoPestDisease(
    slug="mango-scale",
    name="Mango Scale",
    short_desc="Mango Scales are insects feeding on the sap of mango trees, damaging the crop",
    image_url="images/mangoscale.png",
    full_description="There are two types of mango scales: False mango scales and White mango scales (Chin et al., 2010). Mango scales are insects that consume and live off the sap from plants, feeding mainly on the protein within the sap (Owen, 2016). After consuming the sap, the overall health of the plant is damaged and the remaining sugary contents in the sap are excreted on the plant, leading to the growth of black mould (Owen, 2016).",
    symptoms="•Areas on leaves may appear pale green or yellow • Pink spots on the mango",
    treatment="•Growth regulators and systematic sprays should be used for live and preferrably young scales. • Apply the chemicals prior to pruning to prevent infestation. • If scales are still active after pruning, use stroger mineral oils for spraying. • After pruning, cut off any infected branches to avoid spreading of the scales."
)

mango_pestdiseases = [pest1, pest2, pest3, pest4, pest5, pest6, pest7]
