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
    slug="mango-anthracnose",
    name="Mango Anthracnose",
    short_desc="A fungal disease causing dark lesions on leaves, flowers, and fruit. It spreads rapidly in humid conditions and affects mango yield and postharvest quality.",
    image_url="images/mango anthracnoce spot.jpg",
    full_description=(
        "Mango anthracnose is caused by the fungus *Colletotrichum gloeosporioides* "
        "(teleomorph: *Glomerella cingulata*), including its variant *C. gloeosporioides var. minor* "
        "(Pitkethley & Conde, 2007). It is one of the most destructive mango diseases in tropical and "
        "subtropical climates, affecting leaves, flowers, stems, and fruits. Yield losses typically range "
        "from 30–60%, but can reach 100% under very humid or rainy conditions (Paudel et al., 2022).\n\n"
        "A unique risk of this disease is its latent infection capability. The fungus infects green fruits "
        "while still on the tree and remains dormant until ripening. Once activated, it causes rapid rotting, "
        "making postharvest control difficult. The fungus spreads via rain, wind, and irrigation and thrives "
        "in high humidity (≥95%) and temperatures between 25–30°C, especially during flowering and fruit "
        "development (Paudel et al., 2022).\n\n"
        "Recent research by Li et al. (2024) explores eco-friendly control strategies, such as using edible "
        "coatings with Chitosan (CTS) and Iturin A (IA). These coatings inhibit fungal growth, enhance the "
        "fruit’s natural defences, and prolong shelf life by reducing lesion development by 69%, retaining "
        "sugar and acidity levels, and limiting respiration."
    ),
    symptoms="""\
<ul>
  <li><strong>Leaves:</strong> Tan to dark brown spots, especially near edges; semi-circular lesions on new flushes exposed to rain (Pitkethley & Conde, 2007; Paudel et al., 2022).</li>
  <li><strong>Flowers (Panicles):</strong> Tiny black or brown spots, leading to poor fruit set and flower drop (Paudel et al., 2022).</li>
  <li><strong>Fruits:</strong> 
    <ul>
      <li>Young fruits: Large sunken black lesions, often oozing.</li>
      <li>Ripening fruits: Grey to black slightly sunken lesions with pink-orange spore masses (Pitkethley & Conde, 2007).</li>
    </ul>
  </li>
  <li><strong>Twigs and Shoots:</strong> Dark lesions under high humidity starting from shoot tips, potentially causing defoliation and latent infections (Pitkethley & Conde, 2007).</li>
</ul>""",
    treatment="""\
<ul>
  <li><strong>Cultural Control:</strong> Remove infected plant parts, prune for airflow, and avoid planting in damp areas (Paudel et al., 2022).</li>
  <li><strong>Chemical Control:</strong> 
    <ul>
      <li>Mancozeb: Every 14 days from flowering to harvest.</li>
      <li>Prochloraz: For green fruits with careful use to avoid resistance.</li>
      <li>Copper-based fungicides: Effective and safe with only a 1-day withholding period (Pitkethley & Conde, 2007).</li>
    </ul>
  </li>
  <li><strong>Postharvest Treatments:</strong> 
    <ul>
      <li>Hot water dip at 55°C for 5 minutes.</li>
      <li>Cold prochloraz sprays and hot benomyl dips for storage protection (Pitkethley & Conde, 2007).</li>
    </ul>
  </li>
  <li><strong>Eco-Friendly Options:</strong> 
    <ul>
      <li>CTS + IA edible coatings: Reduced lesions by 69.1% and preserved quality for 20 days (Li et al., 2024).</li>
      <li>Other solutions: Essential oils (e.g., cinnamon, thyme), beneficial microbes like <em>Pseudomonas fluorescens</em> and <em>Candida membranifaciens</em>, and oxalic acid (Paudel et al., 2022).</li>
    </ul>
  </li>
</ul>"""
)


pest2 =MangoPestDisease(
    slug="backterial-spots",
    name="Backterial-spots",
    short_desc="A bacterial infection that causes black, cracked spots on mango leaves, fruit, and branches. It spreads through rain and tools, reducing fruit quality and yield.",
    image_url="images/mango bactarial black spot leaf.jpg",
    full_description=(
        "Mango Bacterial Black Spot (MBBS) is caused by the bacterium *Xanthomonas campestris* pv. *mangiferaeindicae*. "
        "It thrives during hot and rainy seasons and severely affects mango production, especially in susceptible "
        "cultivars like 'Kate'. Under highly favorable conditions, infection rates may reach 50–80%, causing major "
        "losses in both yield and fruit quality (Li et al., 2025).\n\n"
        "The disease was first identified in Australia's Northern Territory in 1981 and has since spread across most "
        "Top End mango regions. While damage is usually limited due to a dry fruiting season, unseasonal rain can cause "
        "serious outbreaks (Pitkethley, 2006).\n\n"
        "MBBS affects both external and internal plant health. It disrupts the microbial balance, increasing harmful "
        "bacteria like *Pseudomonas*, *Burkholderia*, and *Diaporthe*, and decreasing beneficial microbes such as "
        "*Penicillium*, *Fusarium*, and *Alternaria*. However, increases in beneficial bacteria like *Paenibacillus* "
        "show promise for biological control (Li et al., 2025).\n\n"
        "MBBS can be transmitted silently through infected seedlings or budwood, often without visible symptoms. It spreads "
        "via wind-driven rain and contaminated tools, making prevention and monitoring essential."
    ),
    symptoms="""\
<ul>
  <li><strong>Leaves:</strong> Small water-soaked spots that turn black or brown and ulcerated, often angular due to vein boundaries. Severe cases lead to premature leaf drop (Pitkethley, 2006; Li et al., 2025).</li>
  <li><strong>Fruits:</strong> Sunken black-brown spots with water-soaked edges and star-shaped cracks. Lesions may merge into large ulcerated areas, causing premature fruit drop.</li>
  <li><strong>Twigs and Branches:</strong> Cracked black lesions that become long-term infection sources and may lead to branch dieback.</li>
  <li><strong>Disease Spread:</strong> Wind-driven rain, wounds on the plant surface, and contaminated equipment are major pathways. Wind damage increases vulnerability. Windbreaks can reduce spread (Pitkethley, 2006).</li>
</ul>""",
    treatment="""\
<ul>
  <li><strong>Cultural Management:</strong> 
    <ul>
      <li>Remove infected plant parts and sterilize pruning tools.</li>
      <li>Improve airflow through pruning and avoid waterlogged planting sites.</li>
      <li>Use certified disease-free planting materials and establish windbreaks.</li>
    </ul>
  </li>
  <li><strong>Chemical Control:</strong> 
    <ul>
      <li>Copper-based bactericides are widely used.</li>
      <li>In the Northern Territory: 
        <ul>
          <li>Copper oxychloride (500 g/kg): 250 g per 100 L of water or 4 kg/ha.</li>
          <li>Copper oxide (400 g/L): 300–400 mL per 100 L.</li>
        </ul>
      </li>
      <li>Spray every four weeks from flowering to fruit set. Withholding period: 1 day (Pitkethley, 2006).</li>
    </ul>
  </li>
  <li><strong>Biological Control:</strong> 
    <ul>
      <li>Beneficial microbes like <em>Paenibacillus</em>, <em>Bacillus subtilis</em>, and <em>Pseudomonas fluorescens</em> suppress the disease and support plant health.</li>
      <li>MBBS triggers plant defense systems, including amino acid metabolism and energy transport, which may help long-term resistance (Li et al., 2025).</li>
    </ul>
  </li>
</ul>"""
)

pest3 = MangoPestDisease(
    slug="mango-leafhoppers",
    name="Mango Leafhoppers",
    short_desc="Sap-sucking insects that damage mango flowers and reduce yield.",
    image_url="images/Mango leafhopper img7.jpeg",
     # Citation:(Smith & Brown 2014)
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
     #Citation: Weinert et al. (n.d.)
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
    # Citation: Conde et al. (2007)
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
    slug="fruit-flies",
    name="Fruit Flies",
    short_desc="Fruit-flies lay eggs on mangoes, causing damage to the fruit and crop.",
    image_url="images/fruitflies.png",
    full_description=
    ("Fruit flies are labelled as one of the major pests in the Northern Territory due to their negative effects on a variety of fruit crops, particularly mangoes."
     " The two main species of fruit flies include Bactocera tyroni (left of figure above) and Bactocera jarvisi (right of figure above) and they both have negative effects on the harvest of mangoes (E. S. C. Smith and H. Brown, 2014)."
     " There appearance is simliar to a common house fly in terms of their size. However they are slightly larger than houselfies and appear yellow/ brown in colour."
     " The life cycle of both of these species of flies typically ranges between 4-5 weeks within the weather in the Northern Territory; however, it can be longer in cooler areas (Smith and Brown, 2014)."
     " These flies lay eggs on the ripe mangoes and once they hatch, the larvae burrows into the fruit, causing it to rot and as a result, destroying the whole crop."
     "B.tyroni has 70+ hosts, meaning that they attack 70+ species of crops and B.jarvisi has 27 hosts, indicating that they attack 27 species of crops (Smith and Brown, 2014)."
     ),
    symptoms="""
        <ul>
            <li>Decay of fruit flesh</li>
            <li>Bruising on fruit skin</li>
            <li>sting marks</li>
            <li>Squishy/ soft areas on the mango</li>
            <li>Larvae inside mango</li>
            <li>Fruit falling off tree by itself before ripening</li>
        </ul>
    """,

    treatment="""
        <ul>
            <li>Harvest the mangoes just before ripening as the flies will tend to attack once the mango is ripe.</li>
            <li>Bait spraying (including <b>protein + malathion</b>) would allow the flies to be diverted from the mangoes and feed on the bait to avoid the fruit from being affected.</li>
            <li>Removing any ripe or overripe mangoes would prevent forming a breeding ground for these flies.</li>
            <li>Covering these mangoes with bags would prevent flies from having the opportunity to lay eggs on the mangoes.</li>
            <li>Fruit dipping can be implemented for commercial use, which kills any eggs that have been laid on the mangoes.</li>
        </ul>
""",
)

pest7 = MangoPestDisease(
    slug="mango-scale",
    name="Mango Scale",
    short_desc="Mango Scales are insects feeding on the sap of mango trees, damaging the crop",
    image_url="images/mango_scale.png",
    full_description=
    ("There are two types of mango scales: False mango scales and White mango scales (Chin et al., 2010)."
    " Male mango scales are typically smaller; however, they have wings meaning that they are able to travel within short distances. Female mango scales on the other hand are oval in shape and are stationary."
    " Mango scales are insects that consume and live off the sap from plants, feeding mainly on the protein within the sap (Owen, 2016)."
    " After consuming the sap, the overall health of the plant is damaged and the remaining sugary contents in the sap are excreted on the plant, leading to the growth of black mould (Owen, 2016)."
    " The black mold that is formed on the leaves also blocks out the sunlight from reaching the leaves. This in turn blocks the process of photosynthesis, stopping the plant from converting the sunlight to energy."
    " Mango scales can sometimes form underneath the leaves and on the stems, making them slightly harder to identify."
    " The scales can easily spread from tree to tree through the wind and other insects spreading them from tree to tree. Any tools that were used on infected trees should be sanitised before resusing as they can spread through this way also."
    ),
    symptoms="""
        <ul>
            <li>Areas on leaves may appear pale green or yellow</li>
            <li>Pink spots on the mango</li>
            <li>Mango remaining small and not developing properly</li>
            <li>Black mold growing on either the fruit or leaves</li>
            <li>Small bumps appearing on whole crop</li>
        </ul>
    """,
    treatment="""
        <ul>
            <li>Growth regulators and systematic sprays should be used for live and preferrably young scales.</li>
            <li>Apply the chemicals prior to pruning to prevent infestation.</li>
            <li>If scales are still active after pruning, use stroger mineral oils for spraying.</li>
            <li>After pruning, cut off any infected branches to avoid spreading of the scales.</li>
            <li>Dispose of any fallen branches, leaves, or fuit to avoid spreading the mango scales.</li>
        </ul>
""",
)

mango_pestdiseases = [pest1, pest2, pest3, pest4, pest5, pest6, pest7]
